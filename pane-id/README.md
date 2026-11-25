# pane-id

エージェントが動いているペインの表示名を「claude ❯ wQ:pSF」のようにして、枠線のラベルと agents 欄にペイン ID を出す。あわせて全ペインに ID を表示用の値 `id` として付けるので、agents 欄の行に `$id` と書けば好きな位置にも出せる。

起動時と、ペインの作成・移動、エージェントの検出、タブの移動のたびに、全ペインへ付け直す。ずれたときは `herdr plugin action invoke kuhku.pane-id.retag` で手動でも付け直せる。

## 設定

枠線のラベルとコピーのキーはプラグインから設定できないので、`~/.config/herdr/config.toml` に書く。

```toml
[ui]
show_agent_labels_on_pane_borders = true

# フォーカス中のペインの ID をクリップボードへコピーする（macOS）
[[keys.command]]
key = "prefix+y"
type = "shell"
command = "printf '%s' \"$HERDR_ACTIVE_PANE_ID\" | /usr/bin/pbcopy"
description = "フォーカス中のペインIDをコピー"
```

手で名前を付けたペインは、枠線のラベルにその名前が出る（herdr の仕様）。
