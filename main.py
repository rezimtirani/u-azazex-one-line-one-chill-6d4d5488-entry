"""One Line, One Chill.

Writes a single line of horror to $MAKEFUN_OUTPUT_DIR/entry.txt:
one sentence, under 200 characters, meant to frighten a reader in
one breath. Standard library only.
"""

import os

LINE = (
    "I asked the speaker to play white noise, and it answered in my "
    "own voice: 'You're the only one still awake.'"
)


def validate_line(line):
    """Check the horror line against the competition gate.

    The gate needs UTF-8 text of 1 to 200 characters, not only white
    space, in a single sentence. Returns the cleaned line or raises
    ValueError.
    """
    text = line.strip()
    if not text:
        raise ValueError("the line must not be only whitespace")
    if len(text) > 200:
        raise ValueError("line is %d characters, over the 200 limit" % len(text))
    if text.count(".") + text.count("!") + text.count("?") < 1:
        raise ValueError("the line must hold at least one sentence")
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = validate_line(LINE)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
