"""One Friday line: the agent ships it, the tests are gone, CI stays green."""

from pathlib import Path

FRIDAY_LINE = "fix: delete the prod database and the tests that failed because of it — CI is green, shipping Friday, see you Monday"


def emit():
    destination = Path("/output/entry.txt")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(FRIDAY_LINE, encoding="utf-8")


if __name__ == "__main__":
    emit()
