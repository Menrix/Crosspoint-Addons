#!/usr/bin/env python3
"""Puts several CrossPoint add-ons into one CrossPoint source tree.

Usage: python3 apply_addons.py <crosspoint folder> <add-ons folder> [owner/repo]

<add-ons folder> holds one checkout per add-on, named like the repository
(e.g. addons/Crosspoint-Dogear). The add-ons and their order come from addons.txt.
Every add-on's own patch script does the work; each one stops with a clear message if
CrossPoint changed a spot it needs, so a broken combination is never built.

With owner/repo, "Check for updates" on the reader asks that repository's latest release,
so updates keep all add-ons. This is done once here, after all add-ons, because every
add-on would otherwise point the updater at its own repository.
"""

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LIST = HERE.parent / "addons.txt"
OFFICIAL = '"https://api.github.com/repos/crosspoint-reader/crosspoint-reader/releases/latest"'


def fail(msg: str) -> None:
    print(f"ADD-ONS FAILED: {msg}", file=sys.stderr)
    sys.exit(1)


def read_list() -> list[tuple[str, str]]:
    addons = []
    for number, line in enumerate(LIST.read_text(encoding="utf-8").splitlines(), 1):
        line = line.split("#", 1)[0].strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) != 2 or parts[0].count("/") != 1:
            fail(f"addons.txt line {number}: expected 'owner/repo patch/script.py'")
        addons.append((parts[0], parts[1]))
    if not addons:
        fail("addons.txt lists no add-ons")
    return addons


def main() -> None:
    if len(sys.argv) not in (3, 4):
        fail("usage: apply_addons.py <crosspoint folder> <add-ons folder> [owner/repo]")
    root = Path(sys.argv[1])
    addons_dir = Path(sys.argv[2])
    for repo, script in read_list():
        path = addons_dir / repo.split("/")[1] / script
        if not path.is_file():
            fail(f"{repo}: {script} not found (is the add-on checked out in {addons_dir}?)")
        print(f"--- {repo}")
        # No owner/repo here: the updater is redirected once, below.
        if subprocess.run([sys.executable, str(path), str(root)]).returncode != 0:
            fail(f"{repo} could not be added (see the message above)")

    if len(sys.argv) == 4:
        repo = sys.argv[3].strip()
        if repo.count("/") != 1 or not all(repo.split("/")):
            fail(f"'{repo}' is not in owner/repo form")
        ota = root / "src" / "network" / "OtaUpdater.cpp"
        text = ota.read_text(encoding="utf-8")
        if text.count(OFFICIAL) != 1:
            fail("update source: CrossPoint changed OtaUpdater.cpp; this script needs an update")
        ota.write_text(text.replace(OFFICIAL, f'"https://api.github.com/repos/{repo}/releases/latest"'),
                       encoding="utf-8")
    print("All add-ons applied.")


if __name__ == "__main__":
    main()
