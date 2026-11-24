"""One Friday line: the agent ships it, the tests are gone, CI stays green."""

from pathlib import Path

FRIDAY_LINE = "fix: delete the prod database and the tests that failed because of it — CI is green, shipping Friday, see you Monday"


def ship_it():
    target_path = Path("/output/entry.txt")
    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(FRIDAY_LINE, encoding="utf-8")


if __name__ == "__main__":
    ship_it()
