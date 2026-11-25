#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes one original funny line of text to /output/entry.txt.

The line: a bank's fraud system flags the most responsible behaviour
imaginable as suspicious. The twist is the punchline — the "crime" is
just being an adult on time.
"""

import os

LINE = "My bank froze my card for suspicious activity: buying groceries and paying rent on time."


def main() -> None:
    # Gate: the bounty only accepts a single line of 1-140 characters.
    assert 1 <= len(LINE) <= 140, f"entry line is {len(LINE)} chars, must be 1-140"
    assert "\n" not in LINE, "entry line must be a single line"
    assert LINE.strip(), "entry line must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Round-trip check: what landed on disk must be exactly the line.
    with open(path, encoding="utf-8") as f:
        assert f.read() == LINE, "entry.txt does not match the line"


if __name__ == "__main__":
    main()
