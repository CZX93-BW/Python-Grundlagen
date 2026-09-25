"""Search the handbook offline, keeping solutions out of normal results."""
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("terms", nargs="+", help="Ein oder mehrere Suchwörter")
    parser.add_argument("--loesungen", action="store_true")
    parser.add_argument("--limit", type=int, default=15)
    args = parser.parse_args()
    words = " ".join(args.terms).casefold().split()
    if not words or args.limit < 1:
        parser.error("Suchwörter und eine positive Treffergrenze verwenden")
    results = []
    for path in ROOT.rglob("*.md"):
        relative = path.relative_to(ROOT)
        if "99_archiv" in relative.parts or ("91_loesungen" in relative.parts and not args.loesungen):
            continue
        text = path.read_text(encoding="utf-8")
        lower = text.casefold()
        if all(word in lower for word in words):
            title = text.splitlines()[0].lstrip("# ")
            score = sum(lower.count(word) + 20 * title.casefold().count(word) for word in words)
            results.append((score, relative.as_posix(), title))
    results.sort(key=lambda item: (-item[0], item[1]))
    print(f"{len(results)} Treffer")
    for _, relative, title in results[:args.limit]:
        print(f"\n{title}\n  {relative}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
