#!/usr/bin/env python3
"""Entry for make.fun: One Line, One Chill.

The entry is the single scariest sentence I can write, under
200 characters, and it is not about monsters. It is about
the message everyone trusts most in computing: the backup
completed successfully. The chill comes from the details:
the font and the phrasing are exactly those of the message
that lied twice before. Nothing in the sentence threatens
anyone. It simply reminds the reader that the most dangerous
sentence in their life is one they have already believed,
twice, on a screen, in that exact font, with that exact tick.

Running this program writes the entry to /output/entry.txt,
falling back to ./output/entry.txt when /output is not
writable, and prints it to stdout as well.
"""

from pathlib import Path

ENTRY_TEXT = (
    "The backup completed successfully, the screen said, in "
    "the exact font and phrasing of the message that had "
    "lied to him twice before."
)

# No restore was attempted in the writing of this sentence.
# That is, in the end, precisely what the sentence is about.
TIMES_IT_LIED = 2


def render_entry() -> str:
    """Return the sentence exactly as it will be read, quietly."""
    return ENTRY_TEXT


def one_scary_line(text: str) -> bool:
    """Confirm the sentence is one line under 200 characters."""
    return "\n" not in text and len(text) < 200


def write_entry(text: str) -> Path:
    """Write the entry text to the output file and return its path."""
    out_dir = Path("/output")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target
    except OSError:
        out_dir = Path("output")
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target


def main() -> None:
    text = render_entry()
    assert one_scary_line(text), "one line, under 200 characters"
    write_entry(text)
    print(text)


if __name__ == "__main__":
    main()
