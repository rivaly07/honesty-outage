#!/usr/bin/env python3
"""Write the status page line to entry.txt inside the output directory.

No network, no dependencies: standard library only.
"""

import os
import sys

ENTRY = (
    "API, web and database are down, and so am I: this page is a static cache. "
    "I cannot check anything, not even our monitors. Cause unknown; "
    "no ETA I would trust."
)


def output_dir() -> str:
    d = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(d, exist_ok=True)
    return d


def main() -> int:
    d = output_dir()
    path = os.path.join(d, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
