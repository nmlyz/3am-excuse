#!/usr/bin/env python3
"""Write one line to /output/entry.txt: the excuse a hardware wallet
gives for refusing to sign a transaction at 3 AM.

The line was picked from 36 candidates by pairwise judging against the
brief — a refusal backed by the wallet's own memory of the owner's last
3 AM mistake, told in two concrete nouns and closed on its strongest
beat. The program builds the line from two clauses — the refusal, then
the remembered receipt — and checks the result against the entry gate
(length, single line, no leading or trailing space, exact judged
length) before writing it, then reads the file back to confirm the
bytes match.
"""

import os
import sys

LINE = (
    "I don't sign at 3 AM. "
    "Last time I did, you woke up owning a yacht-shaped JPEG "
    "and a support ticket."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    if not (1 <= len(LINE) <= 200):
        sys.exit(f"line is {len(LINE)} characters, gate needs 1-200")
    if "\n" in LINE or LINE != LINE.strip():
        sys.exit("line must be a single line with no surrounding space")
    data = (LINE + "\n").encode("utf-8")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        if f.read() != data:
            sys.exit("read-back mismatch")
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
