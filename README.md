# CrossPoint Add-ons

*My CrossPoint add-ons in one firmware – install once, get them all.*

One firmware with all my add-ons for the
[CrossPoint Reader](https://github.com/crosspoint-reader/crosspoint-reader) firmware.

## Included add-ons

| Add-on | What it does | Preview |
| --- | --- | --- |
| [Crosspoint-Dogear](https://github.com/Menrix/Crosspoint-Dogear) | Fold a page corner, jump back with one press | <img src="images/dogear.jpg" width="200" alt="Dog-ear on a book page"> |
| [Crosspoint-ToDoList](https://github.com/Menrix/Crosspoint-ToDoList) | Interactive to-do lists – write and tick right on the reader | <img src="images/todolist.jpg" width="200" alt="A shopping list on the reader"> |

**Free & open source · Ready to flash · Updates built in**

## Install

Get the file for your device from **[Releases](../../releases)**:

| Device | File |
| --- | --- |
| Xteink X4 Pro | `crosspoint-<version>-x4pro.bin` |
| Xteink X3 and X4 | `crosspoint-<version>-x3-x4.bin` |

> **Tested on the X4 Pro.** On the X3, the dog-ear was tested by a user; the to-do lists are not
> tested on the X3 and X4 yet. No touch screen there, so everything runs over the buttons.

Copy it to the SD card and use **Settings → SD Card Firmware Update**. Later updates:
**Settings → Check for Updates**. It already contains all of these add-ons, so don't install them
separately.

## Why a firmware and not a plugin?

The add-ons can't be CrossPoint plugins: they need to hook into the reader itself, the home
screen and File Transfer, and plugins can't reach those parts. So they are built into the latest
**official** CrossPoint. A reader can only run one firmware at a time, so this collection puts
my add-ons together.

## How it is built

**Actions → Build CrossPoint with my add-ons → Run workflow** puts the add-ons listed in
[`addons.txt`](addons.txt) on the latest official CrossPoint release and publishes the firmware
under Releases. A new add-on is one more line in that file.

## License

MIT, see [LICENSE](LICENSE). The add-ons keep their own licenses.

Made with the help of Claude.
