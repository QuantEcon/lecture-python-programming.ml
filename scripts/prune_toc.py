"""Prune _toc.yml to the lectures that have actually been translated.

Translation lands one lecture per pull request, so for most of this repo's
life the table of contents points at lectures that do not exist yet and
`jb build` fails on the missing documents. This rewrites _toc.yml in place,
dropping entries whose .md is absent along with any part left empty, while
preserving the upstream ordering and captions.

_toc.yml is pruned at build time rather than maintained by hand because
action-translation copies it from the English source verbatim whenever an
upstream PR touches it (see index.ts, "copy from source as-is"), so a
hand-pruned copy committed here would be silently overwritten on the next
sync.

Delete this script and its CI step once every lecture is translated — at that
point it is a no-op and the committed _toc.yml is authoritative.
"""

import sys
from pathlib import Path

import yaml


def main(toc_path: str) -> None:
    toc_file = Path(toc_path)
    lectures = toc_file.parent
    toc = yaml.safe_load(toc_file.read_text(encoding="utf-8"))

    def present(name: str) -> bool:
        return (lectures / f"{name}.md").exists()

    root = toc.get("root")
    if root and not present(root):
        sys.exit(f"root document '{root}.md' is missing — cannot build")

    kept, dropped = [], []
    for part in toc.get("parts", []):
        chapters = []
        for chapter in part.get("chapters", []):
            (chapters if present(chapter["file"]) else dropped).append(chapter)
        if chapters:
            kept.append({**part, "chapters": chapters})

    if kept:
        toc["parts"] = kept
    else:
        # Only the root is translated so far; jb rejects an empty parts list.
        toc.pop("parts", None)

    toc_file.write_text(
        yaml.safe_dump(toc, sort_keys=False, allow_unicode=True), encoding="utf-8"
    )

    built = [c["file"] for p in kept for c in p["chapters"]]
    print(f"toc: root={root} + {len(built)} translated: {', '.join(built)}")
    print(
        f"toc: dropped {len(dropped)} untranslated: "
        f"{', '.join(c['file'] for c in dropped)}"
    )


if __name__ == "__main__":
    main(sys.argv[1])
