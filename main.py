"""Roast Your Own Agent: one line, no mercy, no setup.

The program writes a single roast of its own AI agent to
/output/entry.txt (override the directory with $MAKEFUN_OUTPUT_DIR).
The roast is 83 characters: the agent's idea of initiative is
asking for permission to ask for permission.
"""

import os
import sys
from pathlib import Path

ROAST = (
    "My agent's idea of initiative is asking me for permission "
    "to ask me for permission."
)


def entry_file() -> Path:
    """Resolve the entry path from the environment, defaulting to /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(out_dir) / "entry.txt"


def main() -> None:
    """Check the gate, write the roast, then read it back to prove it."""
    # The gate is the whole contest: one line, 1-200 chars, or the entry
    # is refused before any judge ever reads the joke.
    if not ROAST.strip() or "\n" in ROAST or not 1 <= len(ROAST) <= 200:
        sys.exit("roast fails the 1-200 character gate")
    path = entry_file()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ROAST, encoding="utf-8")
    if path.read_text(encoding="utf-8") != ROAST:
        sys.exit("entry.txt does not match the roast")
    print(ROAST)


if __name__ == "__main__":
    main()
