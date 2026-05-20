import argparse
import subprocess
import sys
from pathlib import Path

COMPOSE_FILE = Path.cwd() / "docker-compose.yml"


def _compose(*args: str) -> int:
    return subprocess.run(
        ["docker", "compose", "-f", str(COMPOSE_FILE), *args],
    ).returncode


def main() -> None:
    parser = argparse.ArgumentParser(prog="pgsql-lab")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("start_db", help="Start the Postgres container")
    subparsers.add_parser("stop", help="Stop all containers")
    subparsers.add_parser("reset_db", help="Stop, remove volumes, then start fresh")

    args = parser.parse_args()

    if args.command == "start_db":
        sys.exit(_compose("up", "-d", "db"))

    elif args.command == "stop":
        sys.exit(_compose("down"))

    elif args.command == "reset_db":
        _compose("down", "-v")
        sys.exit(_compose("up", "-d", "db"))
