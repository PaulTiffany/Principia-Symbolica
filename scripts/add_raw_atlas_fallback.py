#!/usr/bin/env python3
"""Add the GitHub raw atlas as a secondary transport fallback.

The GitHub Pages JSON remains canonical. This post-processing step is kept
separate from the main atlas generator so the hierarchy is explicit and easy
to validate:

1. Searchable HTML projection
2. Canonical GitHub Pages JSON
3. Byte-identical GitHub Pages text mirror
4. GitHub raw JSON transport fallback
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ATLAS = ROOT / "atlas"
BASE = "https://paultiffany.github.io/Principia-Symbolica"
RAW = "https://raw.githubusercontent.com/PaulTiffany/Principia-Symbolica/main/principia_atlas.json"

VISIBLE_NEEDLE = f'''<a href="{BASE}/principia_atlas.txt">indexable text mirror</a>
<span aria-hidden="true">·</span>
<a href="{BASE}/llms.txt">machine reading guide</a>'''
VISIBLE_REPLACEMENT = f'''<a href="{BASE}/principia_atlas.txt">indexable text mirror</a>
<span aria-hidden="true">·</span>
<a href="{RAW}">GitHub raw fallback</a>
<span aria-hidden="true">·</span>
<a href="{BASE}/llms.txt">machine reading guide</a>'''

STRUCTURED_NEEDLE = f'''{{"@type":"DataDownload","contentUrl":"{BASE}/principia_atlas.txt","encodingFormat":"text/plain"}}]}}'''
STRUCTURED_REPLACEMENT = f'''{{"@type":"DataDownload","contentUrl":"{BASE}/principia_atlas.txt","encodingFormat":"text/plain"}},
{{"@type":"DataDownload","contentUrl":"{RAW}","encodingFormat":"application/json","name":"GitHub raw transport fallback"}}]}}'''


def patch_html(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    if RAW not in text:
        if VISIBLE_NEEDLE not in text:
            raise RuntimeError(f"Visible fallback insertion point missing from {path}")
        text = text.replace(VISIBLE_NEEDLE, VISIBLE_REPLACEMENT, 1)
        if STRUCTURED_NEEDLE not in text:
            raise RuntimeError(f"Structured fallback insertion point missing from {path}")
        text = text.replace(STRUCTURED_NEEDLE, STRUCTURED_REPLACEMENT, 1)
        path.write_text(text, encoding="utf-8")


def patch_llms(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    if RAW in text:
        return
    needle = f"- [Indexable text mirror]({BASE}/principia_atlas.txt)"
    if needle not in text:
        raise RuntimeError(f"LLM fallback insertion point missing from {path}")
    replacement = needle + f"\n- [GitHub raw JSON fallback]({RAW}): Secondary transport mirror; the GitHub Pages JSON remains canonical."
    path.write_text(text.replace(needle, replacement, 1), encoding="utf-8")


def patch_manifest(path: Path) -> None:
    manifest = json.loads(path.read_text(encoding="utf-8"))
    manifest["canonical_json_url"] = f"{BASE}/principia_atlas.json"
    manifest["text_fallback_url"] = f"{BASE}/principia_atlas.txt"
    manifest["raw_transport_fallback_url"] = RAW
    path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    pages = sorted(ATLAS.rglob("index.html"))
    if not pages:
        raise RuntimeError("No generated atlas HTML pages found")
    for page in pages:
        patch_html(page)
    patch_llms(ATLAS / "llms.txt")
    patch_manifest(ATLAS / "build-manifest.json")
    for page in pages:
        if RAW not in page.read_text(encoding="utf-8"):
            raise RuntimeError(f"Raw fallback missing after patching {page}")
    print(f"Added raw fallback to {len(pages)} generated HTML pages")


if __name__ == "__main__":
    main()
