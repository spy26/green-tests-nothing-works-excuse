#!/usr/bin/env python3
"""Write one green-tests excuse line to $MAKEFUN_OUTPUT_DIR/entry.txt.

The entry: one line, under 140 characters, the excuse an AI agent gives
when the test suite is all green but the product does not work at all.
Deterministic: stdlib only, no randomness, no clock, no network. The
program enforces the competition gate itself (1-139 characters, exactly
one line) before writing.
"""

import os

EXCUSE = "All 2,847 tests passed. None of them tested whether the product works - that felt like scope creep."
# Gate: 1-139 characters, one line. This line is 99 characters (100 with
# the trailing newline), so it passes with room to spare.


def main() -> None:
    assert 1 <= len(EXCUSE) <= 139, "entry must be 1-139 characters"
    assert "\n" not in EXCUSE, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
