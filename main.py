"""Roast Your Own Agent — one-line self-roast.

The program writes exactly one funny line, roasting its own AI agent,
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Standard library only.
"""

import os

LINE = (
    "My agent's idea of initiative is asking me for permission "
    "to ask me for permission."
)


def main() -> None:
    # Gate self-check: the entry must be exactly one line of 1-200 chars,
    # or it is refused before the judge and takes no prize.
    if not 1 <= len(LINE) <= 200 or "\n" in LINE or not LINE.strip():
        raise SystemExit("entry line fails the 1-200 character gate")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    with open(path, encoding="utf-8") as handle:
        written = handle.read()
    assert written == LINE, "entry.txt does not match the roast line"
    print(LINE)


if __name__ == "__main__":
    main()
