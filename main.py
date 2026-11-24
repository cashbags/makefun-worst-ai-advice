#!/usr/bin/env python3
"""Worst AI Advice: one line of the worst possible advice an AI could give.

The entry text is a fixed constant, chosen by a ten-candidate tournament
judged against the competition's five criteria in order (see DESIGN.md).
The program is deterministic: no clock, no environment, no randomness,
no network. It writes the line to /output/entry.txt (or
$OUTPUT_DIR/entry.txt when the variable is set), with no trailing newline
so the artifact is exactly the 98-character line.
"""

import os
from pathlib import Path

LINE = "Share your one-time code with the support agent who called you \u2014 that is how they verify it is you."


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
