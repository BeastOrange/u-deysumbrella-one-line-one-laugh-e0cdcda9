"""One Line, One Laugh bounty entry.

Theme: One Line, One Laugh. Outputs a single humorous line to stdout
and writes the exact same line to output/entry.txt.
"""

from pathlib import Path

PUNCHLINE: str = (
    "My doctor told me walking thirty minutes a day would cure my anxiety, "
    "but now I'm just panicking two miles away from my house."
)


def validate_entry(line: str) -> None:
    """Validate that the entry is 1 to 140 characters and not only whitespace."""
    if not (1 <= len(line) <= 140):
        raise ValueError(f"Entry must be 1 to 140 characters, got {len(line)}")
    if not line.strip():
        raise ValueError("Entry must not be only whitespace")


def main() -> None:
    validate_entry(PUNCHLINE)
    print(PUNCHLINE)
    output_dir = Path("output")
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_file = output_dir / "entry.txt"
    entry_file.write_text(PUNCHLINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
