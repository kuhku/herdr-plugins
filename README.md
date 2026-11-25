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
| 01 | [**pane-id**](#pane-id) | Shows every agent pane's ID in its border label and the agents sidebar, and copies the focused pane's ID with one key |

<br>

## Install

```bash
herdr plugin install kuhku/herdr-plugins/pane-id
```

Update later with `herdr plugin update`. Remove with `herdr plugin uninstall kuhku.pane-id`.

<br>

## pane-id

> The ID you pass to `herdr pane send-text`, without opening `herdr pane list`.

pane-id writes each agent pane's ID into its display name, so the border label and the
agents sidebar read like this:

```text
┌ claude ❯ wQ:pSF ──────────────────────
```

Every pane, agent or not, also gets the ID as a display token named `id`, which you can put
anywhere in a sidebar row as `$id`.

- **Always current**: re-tags every pane at startup and whenever a pane is created or moved, an agent is detected, or a tab is moved.
  Moving a pane to another workspace gives it a new ID, so this matters.
- **Manual fallback**: if anything drifts, run `herdr plugin action invoke kuhku.pane-id.retag`.
- **Display only**: it writes display metadata only, so agent state and manual pane names stay untouched.
  A manual pane name, when set, takes the border label instead.

Turn on border labels and the copy key in `~/.config/herdr/config.toml` (plugins can't ship either):

```toml
[ui]
show_agent_labels_on_pane_borders = true

# Copy the focused pane's ID to the clipboard (macOS)
[[keys.command]]
key = "prefix+y"
type = "shell"
command = "printf '%s' \"$HERDR_ACTIVE_PANE_ID\" | /usr/bin/pbcopy"
description = "Copy focused pane ID"
```

To copy an agent's ID, pick its row in the sidebar (that focuses its pane), then press `prefix+y`.
On Linux, swap `/usr/bin/pbcopy` for `wl-copy` or `xclip -selection clipboard`.

<br>

## Develop

Clone and link instead of installing, so edits take effect without a push:

```bash
git clone https://github.com/kuhku/herdr-plugins.git
herdr plugin link "$PWD/herdr-plugins/pane-id"
```

`link` and `install` of the same plugin can't coexist. Run `herdr plugin unlink kuhku.pane-id` before switching back.
