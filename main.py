import os
from pathlib import Path

TEXT = "I made a new email for a fresh start, and it immediately asked if I wanted to import 9,412 unread mistakes."


def main() -> None:
    text = TEXT.strip()
    assert text == TEXT, "entry must already be stripped"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
