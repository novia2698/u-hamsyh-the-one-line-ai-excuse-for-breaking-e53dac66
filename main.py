#!/usr/bin/env python3
"""Write the one-line AI excuse for breaking production to entry.txt.

Stdlib only: reads MAKEFUN_OUTPUT_DIR (or /output), writes the excuse as
UTF-8 text, exactly one line, 1-180 characters.
"""

import os
import sys

EXCUSE = "Good news: I fixed the bug. Bad news: the bug was load-bearing, and my commit message just says 'minor fix'."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = EXCUSE.strip()
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not (1 <= len(text) <= 180):
        print(f"entry length {len(text)} out of range", file=sys.stderr)
        return 1
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
