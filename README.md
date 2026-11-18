# Crosspoint-Addons

One firmware for the Xteink X4 Pro, X3 and X4 that combines several add-ons for the
[CrossPoint Reader](https://github.com/crosspoint-reader/crosspoint-reader) firmware.

Each add-on lives, builds and is tested in its own repository. This repository only puts
them together on top of an official CrossPoint release.

## Included add-ons

| Add-on | What it does |
| --- | --- |
| [Crosspoint-Dogear](https://github.com/Menrix/Crosspoint-Dogear) | Bookmarks show as a folded page corner |
| [Crosspoint-ToDoList](https://github.com/Menrix/Crosspoint-ToDoList) | To-do and shopping lists you tick on the reader, fill from phone or computer |

The list and its order are in [`addons.txt`](addons.txt).

## Install

Download `crosspoint-<version>-x4pro.bin` (X4 Pro) or `crosspoint-<version>-x3-x4.bin`
(X3 and X4) from [Releases](../../releases), copy it to the SD card root and use
Settings -> SD Card Firmware Update. Or use https://crosspointreader.com/#flash-tools with
"Custom .bin". After that, Settings -> Check for Updates gets new versions from here.

> **X3 and X4: not tested on a device.** Only the X4 Pro is tested. The X3 and X4 have no touch
> screen, so everything runs over the few buttons (and their layout differs by setting), which
> makes the add-ons harder to use there. Feedback welcome.

Install only one of these firmwares at a time: this one already contains every add-on.

## How it is built

`Actions -> Build CrossPoint with all add-ons -> Run workflow` (started by hand for now):

1. takes the latest official CrossPoint release (or the version you type in),
2. takes the current state of every add-on in `addons.txt`,
3. runs each add-on's own patch script (`scripts/apply_addons.py`); if CrossPoint changed a spot
   an add-on needs, the build stops with a clear message instead of making a broken firmware,
4. points "Check for Updates" at this repository,
5. builds both devices and publishes them as one release. The release notes list which state
   of each add-on went in.

## Adding an add-on

Add one line to `addons.txt`: the repository and the path of its patch script. The script is
called as `python3 <script> <crosspoint folder>` and must change only what it needs.

## License

MIT, see [LICENSE](LICENSE). The add-ons keep their own licenses.
