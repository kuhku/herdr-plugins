# pane-id

各ペインに自分のペイン ID（`wQ:pSF` など）を表示用の値 `id` として付ける。agents 欄の行に `$id` を書くと、ペイン名の隣などに ID が出る。

起動時と、ペインの作成・移動、タブの移動のたびに、全ペインへ付け直す。ずれたときは action「ペインIDを付け直す」で手動でも付け直せる。

## 設定

キーと表示はプラグインから配れないので、`~/.config/herdr/config.toml` に書く。

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

agents 欄で行を選ぶとそのペインにフォーカスが移るので、続けて `prefix+y` を押せば、選んだ agent のペイン ID がコピーされる。
