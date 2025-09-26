import sys
import argparse
from pathlib import Path
from ingest.loaders import load_path
from ingest.normalise import normalise

def read_stdin() -> str:
    return sys.stdin.read()

def summarize(txt: str) -> dict:
    lines = txt.splitlines()
    return {
        "chars": len(txt),
        "lines": len(lines),
        "empty_lines": sum(1 for l in lines if not l.strip()),
    }

# truncate stdout return
def preview(txt: str, n=400) -> str:
    t = txt.replace("\n", "\\n")
    return (t[:n] + ("…" if len(t) > n else ""))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path", help="file path or '-' for stdin")
    ap.add_argument("--show", action="store_true", help="print full normalized text (careful)")
    args = ap.parse_args()

    if args.path == "-":
        raw = read_stdin()
        source = "stdin"
        meta = {}
    else:
        p = Path(args.path)
        if not p.exists():
            print(f"ile not found: {p}", file=sys.stderr)
            sys.exit(1)
        raw, meta = load_path(str(p))
        source = str(p.resolve())

    norm = normalise(raw)
    stats_raw = summarize(raw)
    stats_norm = summarize(norm)

    print("— loader functions ingesting test file... —")
    print(f"source     : {source}")
    print(f"raw        : {stats_raw['chars']} chars, {stats_raw['lines']} lines")
    print(f"normalised : {stats_norm['chars']} chars, {stats_norm['lines']} lines")
    print("preview    :", preview(norm))

    if args.show:
        print("\n------------ full normalised text -----------------\n")
        print(norm)

if __name__ == "__main__":
    main()
