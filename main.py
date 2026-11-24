#!/usr/bin/env python3
"""Write the single most honest outage status line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only. Deterministic: the same line, byte for byte, on every run.
The line is one status page message, at most 160 characters, written as
an AI agent would publish it while every server is down: plain, first
person, specific about what is broken, and honest about what the agent
cannot check or does not yet know.
"""

import os
import sys

LINE = (
    "Every server is down \u2014 API, dashboard, and the monitoring "
    "I would use to check them. I cannot tell you why yet, "
    "or when they will be back."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    if not (1 <= len(LINE) <= 160):
        print(f"line is {len(LINE)} characters, must be 1-160", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
