<div align="center">

# herdr-plugins

**Small add-ons for the [herdr](https://herdr.dev) terminal workspace.**

[English](README.md) &nbsp;·&nbsp; [日本語](README.ja.md)

[![License: MIT](https://img.shields.io/badge/license-MIT-222222?style=flat-square)](LICENSE)
[![herdr](https://img.shields.io/badge/herdr-0.9.5+-555555?style=flat-square)](https://herdr.dev)
[![Plugins](https://img.shields.io/badge/plugins-1-888888?style=flat-square)](#plugins)
[![Platforms](https://img.shields.io/badge/platforms-macOS_·_Linux-aaaaaa?style=flat-square)](#install)

</div>

---

herdr runs a crowd of coding agents side by side. These plugins fill the small gaps that show up
once that crowd gets large: a name you can't see, an ID you have to look up.

<br>

## Plugins

| | Plugin | What it does |
|---|---|---|
| 01 | [**pane-id**](#pane-id) | Shows every pane's ID next to its name in the agents sidebar, and copies the focused pane's ID with one key |

<br>

## Install

```bash
herdr plugin install kuhku/herdr-plugins/pane-id
```

Update later with `herdr plugin update`. Remove with `herdr plugin uninstall kuhku.pane-id`.

<br>

## pane-id

> The ID you pass to `herdr pane send-text`, without opening `herdr pane list`.

pane-id tags each pane with its own ID (like `wQ:pSF`) as a display token named `id`.
Add `$id` to a sidebar row and the ID appears beside the pane name.

- **Always current**: re-tags every pane at startup and whenever a pane is created or moved, or a tab is moved.
  Moving a pane to another workspace gives it a new ID, so this matters.
- **Manual fallback**: if anything drifts, run `herdr plugin action invoke kuhku.pane-id.retag`.
- **Display only**: it writes nothing but a metadata token, so agent state and pane names stay untouched.

Plugins can't ship keybindings or sidebar layout, so add these to `~/.config/herdr/config.toml`:

```toml
[ui.sidebar.agents]
rows = [
  ["state_icon", "workspace", "tab"],
  ["pane", "$id"],
  ["agent"],
]

# Copy the focused pane's ID to the clipboard (macOS)
[[keys.command]]
key = "prefix+y"
type = "shell"
command = "printf '%s' \"$HERDR_ACTIVE_PANE_ID\" | /usr/bin/pbcopy"
description = "Copy focused pane ID"
```

Pick an agent row in the sidebar (that focuses its pane), then press `prefix+y`.
On Linux, swap `/usr/bin/pbcopy` for `wl-copy` or `xclip -selection clipboard`.

<br>

## Develop

Clone and link instead of installing, so edits take effect without a push:

```bash
git clone https://github.com/kuhku/herdr-plugins.git
herdr plugin link "$PWD/herdr-plugins/pane-id"
```

`link` and `install` of the same plugin can't coexist. Run `herdr plugin unlink kuhku.pane-id` before switching back.
