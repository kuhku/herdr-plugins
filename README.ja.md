<div align="center">

# herdr-plugins

**ターミナルの作業場 [herdr](https://herdr.dev) に足す、小さな部品たち。**

[English](README.md) &nbsp;·&nbsp; [日本語](README.ja.md)

[![License: MIT](https://img.shields.io/badge/license-MIT-222222?style=flat-square)](LICENSE)
[![herdr](https://img.shields.io/badge/herdr-0.9.5+-555555?style=flat-square)](https://herdr.dev)
[![Plugins](https://img.shields.io/badge/plugins-1-888888?style=flat-square)](#プラグイン)
[![Platforms](https://img.shields.io/badge/platforms-macOS_·_Linux-aaaaaa?style=flat-square)](#入れ方)

</div>

---

herdr ではコーディングエージェントを何体も並べて動かします。数が増えると、名前が見えない、ID をいちいち調べる、といった小さな手間が出てきます。ここのプラグインは、その隙間を埋めるためのものです。

<br>

## プラグイン

| | プラグイン | できること |
|---|---|---|
| 01 | [**pane-id**](#pane-id) | agents 欄のペイン名の隣に各ペインの ID を出す。フォーカス中のペインの ID はキー 1 つでコピーできる |

<br>

## 入れ方

```bash
herdr plugin install kuhku/herdr-plugins/pane-id
```

更新は `herdr plugin update`、削除は `herdr plugin uninstall kuhku.pane-id` です。

<br>

## pane-id

> `herdr pane send-text` に渡す ID を、`herdr pane list` を開かずに。

各ペインに自分の ID（`wQ:pSF` など）を、表示用の値 `id` として付けます。agents 欄の行に `$id` を書くと、ペイン名の隣に ID が出ます。

- **いつも最新**: 起動時と、ペインの作成・移動、タブの移動のたびに、全ペインへ付け直します。ペインを別のワークスペースへ移すと ID が変わるためです。
- **手動でも直せる**: ずれたときは `herdr plugin action invoke kuhku.pane-id.retag` で付け直せます。
- **表示だけ**: 書き込むのは表示用の値だけで、エージェントの状態やペイン名には触れません。

キーの割り当てと agents 欄の並びはプラグインから配れないので、`~/.config/herdr/config.toml` に書きます。

```toml
[ui.sidebar.agents]
rows = [
  ["state_icon", "workspace", "tab"],
  ["pane", "$id"],
  ["agent"],
]

# フォーカス中のペインの ID をクリップボードへコピーする（macOS）
[[keys.command]]
key = "prefix+y"
type = "shell"
command = "printf '%s' \"$HERDR_ACTIVE_PANE_ID\" | /usr/bin/pbcopy"
description = "フォーカス中のペインIDをコピー"
```

agents 欄で行を選ぶとそのペインにフォーカスが移るので、続けて `prefix+y` を押します。Linux では `/usr/bin/pbcopy` を `wl-copy` か `xclip -selection clipboard` に替えてください。

<br>

## 手元で直すとき

install の代わりに clone して link すると、push しなくても直したものがすぐ効きます。

```bash
git clone https://github.com/kuhku/herdr-plugins.git
herdr plugin link "$PWD/herdr-plugins/pane-id"
```

同じプラグインの link と install は同時に使えません。install に戻すときは、先に `herdr plugin unlink kuhku.pane-id` を実行します。
