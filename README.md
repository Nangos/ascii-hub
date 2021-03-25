# ASCII-HUB: A ~~Place~~Toy to Draw ~~and Share ASCII Widgets~~

## Summary (Version `0.1.0`)

Currently a client-only toyish ASCII art editor. Just trying frond-end devs in Python.

Tested only on Chrome 89.0.4389.90 for Windows 10 (64 bit).

### How to run
Visit https://nangos.github.io/ascii-hub in a browser.

### How to run locally
```sh
git clone https://github.com/nangos/ascii-hub.git
cd ascii-hub
python -m http.server 8000 # (for example)
```
Then visit http://localhost:8000/ in a brower.

## Version Updates

- `v0.1.0`
    - (Very simple & ugly) web page.
    - (Very slowly rendered) basic ASCII-based painter. (Even slow for a 12x30 board)
    - Support of *real* copy & paste to/from clipboard.

- `v0.0.0`
    - Added `README.md`.

---

## What's Next?
- For the edit areas, use HTML canvas/SVG to instead. Rendering a huge HTML table is apparently too slow.
- More advanced mouse & keyboard control.