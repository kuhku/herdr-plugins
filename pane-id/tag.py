"""全ペインに、自分のペインIDを表示用に付ける。

- トークン id: agents 欄の行に "$id" と書くと出る
- エージェントの表示名: エージェントが動いているペインでは「claude ❯ wQ:pSF」にする。
  枠線の左上のラベルと agents 欄の agent の行に出る

何度実行しても結果は同じ。
"""

import json
import os
import subprocess
import sys

HERDR = os.environ.get("HERDR_BIN_PATH") or "herdr"
SOURCE = "kuhku.pane-id"
SEPARATOR = " ❯ "


def metadata_args(pane: dict) -> list[str]:
    pane_id = pane["pane_id"]
    args = ["--token", f"id={pane_id}"]
    agent = pane.get("agent")
    if agent:
        args += ["--display-agent", f"{agent}{SEPARATOR}{pane_id}"]
    else:
        # エージェントが終わったペインに前の表示名を残さない
        args += ["--clear-display-agent"]
    return args


def main() -> int:
    out = subprocess.run([HERDR, "pane", "list"], capture_output=True, text=True, check=True).stdout
    panes = json.loads(out)["result"]["panes"]
    failed = 0
    for pane in panes:
        pane_id = pane["pane_id"]
        result = subprocess.run(
            [HERDR, "pane", "report-metadata", pane_id, "--source", SOURCE, *metadata_args(pane)],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            failed += 1
            print(f"{pane_id}: {result.stderr.strip()}", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
