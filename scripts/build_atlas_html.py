#!/usr/bin/env python3
"""Generate a crawlable HTML projection of the Principia Symbolica atlas.

The JSON atlas remains canonical. The generated HTML follows src/main.tex order,
recursively follows nested TeX inputs, and keeps every page comfortably below
crawler byte limits.
"""
from __future__ import annotations

import hashlib
import html
import json
import re
import shutil
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
ATLAS_JSON = ROOT / "principia_atlas.json"
ATLAS_TXT = ROOT / "principia_atlas.txt"
MAIN_TEX = SRC / "main.tex"
OUT = ROOT / "atlas"
BASE = "https://paultiffany.github.io/Principia-Symbolica"
MAX_PAGE_BYTES = 700_000
MAX_NODES = 45

INPUT_RE = re.compile(r"\\(?:input|include)\{([^}]+)\}")
CHAPTER_RE = re.compile(r"\\chapter\*?\{(.+)\}")
COMMAND_RE = re.compile(r"\\(?:texttt|emph|textbf|textit)\{([^{}]*)\}")
SLUG_RE = re.compile(r"[^a-z0-9]+")


def strip_tex(value: str) -> str:
    value = value.replace("---", "—").replace("--", "–").replace(r"\textbar{}", "|")
    previous = None
    while previous != value:
        previous = value
        value = COMMAND_RE.sub(r"\1", value)
    value = re.sub(r"\\[a-zA-Z@]+\*?", "", value)
    return re.sub(r"\s+", " ", value.replace("{", "").replace("}", "")).strip()


def slugify(value: str) -> str:
    return SLUG_RE.sub("-", value.lower().replace("—", "-").replace("–", "-")).strip("-") or "unit"


def source_name(value: str) -> str:
    value = value.strip()
    return value[:-4] if value.endswith(".tex") else value


def source_path(value: str) -> Path:
    path = SRC / value
    return path if path.suffix == ".tex" else path.with_suffix(".tex")


def main_order() -> list[tuple[str, str | None]]:
    result: list[tuple[str, str | None]] = []
    pending: str | None = None
    active = False
    for raw in MAIN_TEX.read_text(encoding="utf-8").splitlines():
        line = raw.split("%", 1)[0].strip()
        if r"\begin{document}" in line:
            active = True
            continue
        if r"\end{document}" in line:
            break
        if not active:
            continue
        match = CHAPTER_RE.search(line)
        if match:
            pending = strip_tex(match.group(1))
            continue
        for match in INPUT_RE.finditer(line):
            result.append((source_name(match.group(1)), pending))
            pending = None
    return result


def recursive_files(source: str) -> list[str]:
    ordered: list[str] = []
    seen: set[Path] = set()

    def walk(path: Path) -> None:
        path = path.resolve()
        if path in seen or not path.exists():
            return
        seen.add(path)
        ordered.append(path.name)
        for match in INPUT_RE.finditer(path.read_text(encoding="utf-8")):
            child = source_name(match.group(1))
            child_path = (path.parent / child).with_suffix(".tex")
            walk(child_path if child_path.exists() else source_path(child))

    walk(source_path(source))
    return ordered


def identity(node: dict[str, Any]) -> str:
    return str(node.get("label") or node.get("id") or f"node-{node['_atlas_index']}")


def anchor(node: dict[str, Any]) -> str:
    key = identity(node)
    return f"{slugify(key)[:64]}-{hashlib.sha1(key.encode()).hexdigest()[:10]}"


def estimate(node: dict[str, Any]) -> int:
    return len(json.dumps(node, ensure_ascii=False, sort_keys=True).encode()) + 2500


def chunks(nodes: list[dict[str, Any]]) -> list[list[dict[str, Any]]]:
    pages: list[list[dict[str, Any]]] = []
    current: list[dict[str, Any]] = []
    size = 0
    for node in nodes:
        node_size = estimate(node)
        if current and (len(current) >= MAX_NODES or size + node_size > MAX_PAGE_BYTES):
            pages.append(current)
            current, size = [], 0
        current.append(node)
        size += node_size
    if current:
        pages.append(current)
    return pages or [[]]


def fallback_title(nodes: list[dict[str, Any]], source: str) -> str:
    for subtype in ("chapter", "part", "section"):
        for node in nodes:
            if node.get("subtype") == subtype and node.get("name"):
                return strip_tex(str(node["name"]))
    for node in nodes:
        if node.get("name"):
            return strip_tex(str(node["name"]))
    return source.replace("_", " ").title()


def build_units(atlas: dict[str, Any]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    nodes = list(atlas.get("nodes") or [])
    for index, node in enumerate(nodes):
        node["_atlas_index"] = index
    assigned: set[int] = set()
    units: list[dict[str, Any]] = []
    for order, (source, explicit_title) in enumerate(main_order(), start=1):
        files = recursive_files(source)
        file_set = set(files)
        selected = []
        for node in nodes:
            index = int(node["_atlas_index"])
            if index in assigned:
                continue
            book = source_name(str(node.get("book") or ""))
            filename = Path(str(node.get("file") or "")).name
            if book == source or filename in file_set or filename == f"{source}.tex":
                selected.append(node)
                assigned.add(index)
        rank = {name: i for i, name in enumerate(files)}
        selected.sort(key=lambda n: (
            rank.get(Path(str(n.get("file") or "")).name, 10_000),
            Path(str(n.get("file") or "")).name,
            int(n.get("line") or 0),
            int(n["_atlas_index"]),
        ))
        title = explicit_title or fallback_title(selected, source)
        unit_slug = slugify(title)
        if any(unit["slug"] == unit_slug for unit in units):
            unit_slug = f"{unit_slug}-{order}"
        units.append({
            "source": source, "slug": unit_slug, "title": title, "order": order,
            "files": files, "nodes": selected, "chunks": chunks(selected),
        })
    unmatched = [node for node in nodes if int(node["_atlas_index"]) not in assigned]
    if unmatched:
        unmatched.sort(key=lambda n: (
            str(n.get("book") or ""), str(n.get("file") or ""),
            int(n.get("line") or 0), int(n["_atlas_index"]),
        ))
        units.append({
            "source": "supporting-material", "slug": "supporting-material",
            "title": "Supporting Atlas Material", "order": len(units) + 1,
            "files": sorted({Path(str(n.get("file") or "")).name for n in unmatched if n.get("file")}),
            "nodes": unmatched, "chunks": chunks(unmatched),
        })
    return units, nodes


def url_for(path: Path) -> str:
    relative = path.relative_to(ROOT).as_posix()
    if relative.endswith("index.html"):
        relative = relative[:-10]
    return f"{BASE}/{relative}"


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def fallback_links() -> str:
    return f'''<aside class="fallback" aria-label="Canonical atlas resources">
<strong>Atlas sources:</strong>
<a href="{BASE}/principia_atlas.json">canonical JSON</a>
<span aria-hidden="true">·</span>
<a href="{BASE}/principia_atlas.txt">indexable text mirror</a>
<span aria-hidden="true">·</span>
<a href="{BASE}/llms.txt">machine reading guide</a>
</aside>'''


def breadcrumb(items: list[tuple[str, str]]) -> str:
    links = ' <span aria-hidden="true">/</span> '.join(
        f'<a href="{html.escape(url, quote=True)}">{html.escape(label)}</a>' for label, url in items
    )
    return f'<nav class="breadcrumbs" aria-label="Breadcrumb">{links}</nav>'


def page(title: str, description: str, canonical: str, body: str, prev: str | None = None, nxt: str | None = None) -> str:
    relations = []
    if prev:
        relations.append(f'<link rel="prev" href="{html.escape(prev, quote=True)}">')
    if nxt:
        relations.append(f'<link rel="next" href="{html.escape(nxt, quote=True)}">')
    return f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description, quote=True)}">
<meta name="robots" content="index, follow, max-snippet:-1">
<link rel="canonical" href="{html.escape(canonical, quote=True)}">
<link rel="alternate" type="application/json" href="{BASE}/principia_atlas.json" title="Canonical JSON atlas">
<link rel="alternate" type="text/plain" href="{BASE}/principia_atlas.txt" title="Indexable text mirror">
{''.join(relations)}
<link rel="stylesheet" href="{BASE}/atlas/assets/atlas.css">
<script type="application/ld+json">{{
"@context":"https://schema.org","@type":"CreativeWork","name":{json.dumps(title)},
"url":{json.dumps(canonical)},"isPartOf":{{"@type":"Book","name":"Principia Symbolica","url":"{BASE}/"}},
"author":{{"@type":"Person","name":"Paul Carver Tiffany III","url":"https://paultiffany.github.io/"}},
"encoding":[
{{"@type":"DataDownload","contentUrl":"{BASE}/principia_atlas.json","encodingFormat":"application/json"}},
{{"@type":"DataDownload","contentUrl":"{BASE}/principia_atlas.txt","encodingFormat":"text/plain"}}]}}</script>
</head><body>{body}</body></html>'''


def ref_list(title: str, values: Any, targets: dict[str, str]) -> str:
    if not values:
        return ""
    if not isinstance(values, list):
        values = [values]
    items = []
    for value in values:
        label = str(value.get("label")) if isinstance(value, dict) and value.get("label") else str(value)
        target = targets.get(label)
        content = f'<a href="{html.escape(target, quote=True)}"><code>{html.escape(label)}</code></a>' if target else f'<code>{html.escape(label)}</code>'
        items.append(f"<li>{content}</li>")
    return f'<section class="relations"><h3>{html.escape(title)}</h3><ul>{"".join(items)}</ul></section>'


def render_node(node: dict[str, Any], targets: dict[str, str]) -> str:
    node_anchor = anchor(node)
    name = str(node.get("name") or identity(node))
    body = str(node.get("latex_body") or "")
    badges = [node.get("type"), node.get("subtype"), node.get("proof_status"), node.get("matter_region")]
    badge_html = "".join(f'<span class="badge">{html.escape(str(value))}</span>' for value in badges if value)
    filename = str(node.get("file") or "")
    line = node.get("line")
    source = f"{filename}:{line}" if filename and line is not None else filename or "not recorded"
    relation_html = "".join([
        ref_list("Depends on", node.get("depends_on"), targets),
        ref_list("Cites", node.get("cites"), targets),
        ref_list("Cited by", node.get("cited_by"), targets),
        ref_list("Forward references", node.get("forward_refs"), targets),
        ref_list("Appendix teaser references", node.get("appendix_teaser_refs"), targets),
    ])
    role_rows = []
    for role in node.get("ref_roles") or []:
        if not isinstance(role, dict):
            continue
        label = str(role.get("label") or "")
        target = targets.get(label)
        rendered_label = f'<a href="{html.escape(target, quote=True)}"><code>{html.escape(label)}</code></a>' if target else f'<code>{html.escape(label)}</code>'
        role_rows.append(f'<tr><td>{rendered_label}</td><td>{html.escape(str(role.get("role") or ""))}</td><td>{"yes" if role.get("logical_support") else "no"}</td></tr>')
    role_table = ""
    if role_rows:
        role_table = f'<section class="relation-roles"><h3>Reference roles</h3><table><thead><tr><th>Target</th><th>Role</th><th>Logical support</th></tr></thead><tbody>{"".join(role_rows)}</tbody></table></section>'
    raw_record = {key: value for key, value in node.items() if not key.startswith("_atlas_")}
    complete = html.escape(json.dumps(raw_record, ensure_ascii=False, indent=2, sort_keys=True))
    latex = f'<section class="latex"><h3>Exact LaTeX body</h3><pre><code>{html.escape(body)}</code></pre></section>' if body else ""
    return f'''<article class="node" id="{node_anchor}">
<header><p class="badges">{badge_html}</p><h2>{html.escape(name)}</h2><p class="identity"><code>{html.escape(identity(node))}</code></p></header>
<dl class="metadata"><dt>Source</dt><dd>{html.escape(source)}</dd><dt>Book/unit</dt><dd>{html.escape(str(node.get("book") or "not recorded"))}</dd><dt>Role</dt><dd>{html.escape(str(node.get("role") or node.get("matter_role") or "not recorded"))}</dd></dl>
{latex}<div class="relation-grid">{relation_html}</div>{role_table}
<details class="record"><summary>Complete structured record</summary><pre><code>{complete}</code></pre></details>
<p class="permalink"><a href="#{node_anchor}">Permalink to this record</a></p></article>'''


def build() -> None:
    atlas = json.loads(ATLAS_JSON.read_text(encoding="utf-8"))
    if not ATLAS_TXT.exists() or ATLAS_TXT.read_bytes() != ATLAS_JSON.read_bytes():
        shutil.copyfile(ATLAS_JSON, ATLAS_TXT)
    units, nodes = build_units(atlas)
    if sum(len(unit["nodes"]) for unit in units) != len(nodes):
        raise RuntimeError("Atlas node assignment is incomplete or duplicated")
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "assets").mkdir(parents=True)

    pages: list[dict[str, Any]] = []
    targets: dict[str, str] = {}
    for unit in units:
        for number, group in enumerate(unit["chunks"], start=1):
            path = OUT / unit["slug"] / f"page-{number}" / "index.html"
            entry = {"unit": unit, "number": number, "nodes": group, "path": path, "url": url_for(path)}
            pages.append(entry)
            for node in group:
                target = f'{entry["url"]}#{anchor(node)}'
                for key in (node.get("id"), node.get("label")):
                    if key:
                        targets.setdefault(str(key), target)

    urls = [entry["url"] for entry in pages]
    for index, entry in enumerate(pages):
        unit, number, group = entry["unit"], entry["number"], entry["nodes"]
        prev = urls[index - 1] if index else None
        nxt = urls[index + 1] if index + 1 < len(urls) else None
        content = ''.join(render_node(node, targets) for node in group)
        body = f'''<header class="site-header">
{breadcrumb([("Principia Symbolica", f"{BASE}/"), ("Atlas", f"{BASE}/atlas/"), (unit["title"], f'{BASE}/atlas/{unit["slug"]}/')])}
<p class="eyebrow">Principia Symbolica Atlas</p><h1>{html.escape(unit["title"])} <span class="page-number">— page {number} of {len(unit["chunks"])}</span></h1>
<p class="lede">Visible HTML projection of {len(group)} structured atlas records, following the manuscript order declared in <code>src/main.tex</code>.</p>{fallback_links()}</header>
<main>{content}</main><nav class="page-nav" aria-label="Page navigation">
{f'<a rel="prev" href="{prev}">← Previous atlas page</a>' if prev else '<span></span>'}<a href="{BASE}/atlas/{unit["slug"]}/">Unit index</a>{f'<a rel="next" href="{nxt}">Next atlas page →</a>' if nxt else '<span></span>'}</nav>'''
        write(entry["path"], page(
            f'{unit["title"]} — Atlas page {number} | Principia Symbolica',
            f'Structured Principia Symbolica atlas records for {unit["title"]}, page {number}.',
            entry["url"], body, prev, nxt,
        ))

    unit_urls = []
    for unit in units:
        path = OUT / unit["slug"] / "index.html"
        unit_url = url_for(path)
        unit_urls.append(unit_url)
        cards = []
        for number, group in enumerate(unit["chunks"], start=1):
            first = str(group[0].get("name") or identity(group[0])) if group else "Empty page"
            last = str(group[-1].get("name") or identity(group[-1])) if group else "Empty page"
            cards.append(f'<li><a href="page-{number}/"><strong>Page {number}</strong></a><span>{len(group)} records · {html.escape(first)} → {html.escape(last)}</span></li>')
        body = f'''<header class="site-header">{breadcrumb([("Principia Symbolica", f"{BASE}/"), ("Atlas", f"{BASE}/atlas/")])}
<p class="eyebrow">Manuscript unit {unit["order"]}</p><h1>{html.escape(unit["title"])}</h1>
<p class="lede">{len(unit["nodes"])} atlas records across {len(unit["chunks"])} bounded HTML pages. Source unit: <code>{html.escape(unit["source"])}</code>.</p>{fallback_links()}</header>
<main class="unit-index"><h2>Pages</h2><ol>{''.join(cards)}</ol><h2>Source files</h2><ul class="source-files">{''.join(f'<li><code>{html.escape(name)}</code></li>' for name in unit["files"])}</ul></main>'''
        write(path, page(f'{unit["title"]} | Principia Symbolica Atlas', f'Searchable HTML atlas index for {unit["title"]}.', unit_url, body))

    meta = atlas.get("meta") or {}
    unit_cards = ''.join(f'<li><a href="{unit["slug"]}/"><strong>{html.escape(unit["title"])}</strong></a><span>{len(unit["nodes"])} records · {len(unit["chunks"])} pages · <code>{html.escape(unit["source"])}</code></span></li>' for unit in units)
    root_body = f'''<header class="site-header atlas-home">{breadcrumb([("Principia Symbolica", f"{BASE}/")])}
<p class="eyebrow">Searchable HTML edition</p><h1>Principia Symbolica Atlas</h1>
<p class="lede">A crawlable, bounded-page projection of the canonical machine-readable atlas, chunked in the publication order declared by <code>src/main.tex</code>.</p>{fallback_links()}
<dl class="stats"><dt>Atlas schema</dt><dd>{html.escape(str(meta.get("schema") or "not recorded"))}</dd><dt>Generated source</dt><dd>{html.escape(str(meta.get("generated_at") or "not recorded"))}</dd><dt>Total records</dt><dd>{len(nodes)}</dd><dt>HTML units</dt><dd>{len(units)}</dd><dt>HTML content pages</dt><dd>{len(pages)}</dd></dl>
<label class="search-label" for="atlas-search">Search titles, labels, types, proof status, and source files</label><input id="atlas-search" type="search" placeholder="e.g. bounded observer, theorem, book4.tex" autocomplete="off"><p id="search-status" class="search-status" aria-live="polite"></p><ul id="search-results" class="search-results"></ul></header>
<main class="atlas-index"><h2>Manuscript order</h2><ol>{unit_cards}</ol></main><script src="{BASE}/atlas/assets/search.js" defer></script>'''
    write(OUT / "index.html", page("Principia Symbolica Atlas — Searchable HTML Edition", "Searchable, crawlable HTML projection of the Principia Symbolica machine-readable atlas.", f"{BASE}/atlas/", root_body))

    search = []
    for node in nodes:
        key = identity(node)
        search.append({
            "id": key, "name": str(node.get("name") or key), "type": str(node.get("type") or ""),
            "subtype": str(node.get("subtype") or ""), "proof_status": str(node.get("proof_status") or ""),
            "book": str(node.get("book") or ""), "file": str(node.get("file") or ""), "url": targets.get(key, ""),
        })
    write(OUT / "search-index.json", json.dumps(search, ensure_ascii=False, separators=(",", ":")))

    css = ''':root{color-scheme:dark;--bg:#0b0c0b;--panel:#121412;--ink:#e9e6dc;--dim:#aaa69a;--line:#31342f;--gold:#d8b46a;--code:#d7e2cf}*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.62 Georgia,"Times New Roman",serif}a{color:var(--gold)}code,pre,input,.eyebrow,.breadcrumbs,.badge,.metadata,.fallback,.page-nav,.search-status{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}.site-header,main,.page-nav{max-width:1120px;margin:auto;padding-left:24px;padding-right:24px}.site-header{padding-top:42px;padding-bottom:34px}.breadcrumbs{font-size:.82rem;color:var(--dim);margin-bottom:30px}.eyebrow{text-transform:uppercase;letter-spacing:.16em;color:var(--dim);font-size:.78rem}h1{font-size:clamp(2.4rem,7vw,5.4rem);line-height:1.02;font-weight:400;margin:.25rem 0 1rem}h2{line-height:1.2}.page-number{font-size:.42em;color:var(--dim);white-space:nowrap}.lede{font-size:1.18rem;max-width:820px;color:var(--dim)}.fallback{border:1px solid var(--line);background:var(--panel);padding:14px 16px;margin:24px 0}.fallback a{margin:0 .35rem}.stats,.metadata{display:grid;grid-template-columns:max-content 1fr;gap:6px 18px}.stats dt,.metadata dt{color:var(--dim)}.stats dd,.metadata dd{margin:0}.node{background:var(--panel);border:1px solid var(--line);padding:24px;margin:0 0 28px;overflow-wrap:anywhere}.node h2{font-size:1.7rem;margin:.3rem 0}.badges{display:flex;gap:8px;flex-wrap:wrap}.badge{border:1px solid var(--line);padding:3px 8px;font-size:.75rem;color:var(--dim)}.identity{color:var(--dim)}pre{white-space:pre-wrap;word-break:break-word;background:#090a09;border:1px solid var(--line);padding:16px;overflow:auto;color:var(--code);font-size:.85rem}.relation-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:14px}.relations,.relation-roles{border-top:1px solid var(--line);margin-top:18px;padding-top:12px}.relations h3,.latex h3,.relation-roles h3{font-size:1rem;color:var(--dim)}.relations ul{padding-left:20px}.record{margin-top:18px}.record summary{cursor:pointer;color:var(--gold)}table{border-collapse:collapse;width:100%;font-size:.9rem}th,td{border:1px solid var(--line);text-align:left;padding:7px}.permalink{text-align:right;font-size:.82rem}.page-nav{display:grid;grid-template-columns:1fr auto 1fr;gap:16px;padding-top:20px;padding-bottom:60px}.page-nav a:last-child{text-align:right}.unit-index ol,.atlas-index ol{list-style:none;padding:0}.unit-index li,.atlas-index li{border-bottom:1px solid var(--line);padding:16px 0;display:flex;flex-direction:column;gap:4px}.unit-index li span,.atlas-index li span{color:var(--dim);font-size:.9rem}.source-files{columns:2}.search-label{display:block;margin:30px 0 8px;color:var(--dim)}#atlas-search{width:100%;padding:14px;background:#090a09;color:var(--ink);border:1px solid var(--line);font-size:1rem}.search-results{list-style:none;padding:0}.search-results li{padding:10px 0;border-bottom:1px solid var(--line)}.search-results small{display:block;color:var(--dim)}@media(max-width:640px){body{font-size:15px}.site-header,main,.page-nav{padding-left:16px;padding-right:16px}.node{padding:16px}.metadata,.stats{grid-template-columns:1fr}.source-files{columns:1}.page-nav{grid-template-columns:1fr}.page-nav a:last-child{text-align:left}}'''
    write(OUT / "assets" / "atlas.css", css + "\n")
    js = r'''(()=>{const i=document.getElementById('atlas-search');if(!i)return;const o=document.getElementById('search-results'),s=document.getElementById('search-status');let d=null,t=null;async function l(){if(d)return d;s.textContent='Loading search index…';d=await(await fetch('search-index.json')).json();s.textContent='';return d}function e(v){return String(v).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}async function q(){const v=i.value.trim().toLowerCase();o.innerHTML='';if(v.length<2){s.textContent='';return}const r=await l(),a=v.split(/\s+/),h=[];for(const x of r){const y=[x.id,x.name,x.type,x.subtype,x.proof_status,x.book,x.file].join(' ').toLowerCase();if(a.every(z=>y.includes(z)))h.push(x);if(h.length>=100)break}s.textContent=`${h.length}${h.length===100?' or more':''} matches`;o.innerHTML=h.map(x=>`<li><a href="${e(x.url)}"><strong>${e(x.name)}</strong></a><small>${e([x.type,x.proof_status,x.book,x.file].filter(Boolean).join(' · '))}</small></li>`).join('')}i.addEventListener('input',()=>{clearTimeout(t);t=setTimeout(q,120)})})();'''
    write(OUT / "assets" / "search.js", js + "\n")

    llms = ["# Principia Symbolica Atlas — HTML projection", "", "> Crawlable HTML pages generated from the canonical atlas in the publication order declared by src/main.tex.", "", "## Canonical fallbacks", "", f"- [Canonical JSON atlas]({BASE}/principia_atlas.json)", f"- [Indexable text mirror]({BASE}/principia_atlas.txt)", f"- [Book doorway]({BASE}/)", "", "## HTML units", ""]
    llms.extend(f'- [{unit["title"]}]({BASE}/atlas/{unit["slug"]}/): {len(unit["nodes"])} records across {len(unit["chunks"])} pages.' for unit in units)
    write(OUT / "llms.txt", "\n".join(llms) + "\n")

    sitemap_urls = [f"{BASE}/", f"{BASE}/main.pdf", f"{BASE}/principia_atlas.json", f"{BASE}/principia_atlas.txt", f"{BASE}/llms.txt", f"{BASE}/atlas/", f"{BASE}/atlas/llms.txt", *unit_urls, *urls]
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">', *(f'  <url><loc>{html.escape(url)}</loc></url>' for url in sitemap_urls), '</urlset>']
    write(ROOT / "sitemap.xml", "\n".join(sitemap) + "\n")
    atlas_sitemap_urls = [f"{BASE}/atlas/", f"{BASE}/atlas/llms.txt", *unit_urls, *urls]
    write(OUT / "sitemap.xml", "\n".join(['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">', *(f'  <url><loc>{html.escape(url)}</loc></url>' for url in atlas_sitemap_urls), '</urlset>']) + "\n")

    largest = max((path.stat().st_size for path in OUT.rglob("*.html")), default=0)
    if largest >= 1_500_000:
        raise RuntimeError(f"Generated HTML page exceeds safety limit: {largest} bytes")
    manifest = {
        "schema": "principia-atlas-html/1.0", "source_schema": meta.get("schema"),
        "source_generated_at": meta.get("generated_at"), "records": len(nodes),
        "units": len(units), "content_pages": len(pages), "largest_html_bytes": largest,
        "canonical_json_sha256": hashlib.sha256(ATLAS_JSON.read_bytes()).hexdigest(),
        "text_mirror_sha256": hashlib.sha256(ATLAS_TXT.read_bytes()).hexdigest(),
    }
    write(OUT / "build-manifest.json", json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    print(json.dumps(manifest, indent=2, sort_keys=True))


if __name__ == "__main__":
    build()
