"""Draft flaw: the joke explains itself. Revision fix: land the surprise at the very end."""

import os
from pathlib import Path

TEXT = "My fitness tracker just congratulated me for standing, so apparently my life now peaks during software updates."


def main() -> None:
    text = TEXT.strip()
    assert text == TEXT
    assert "\n" not in text and "\r" not in text
    assert 1 <= len(text) <= 200
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
