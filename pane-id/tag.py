"""全ペインに、自分のペインIDを表示用トークン id として付ける。

agents 欄の行に "$id" を書くと表示される。何度実行しても結果は同じ。
"""

import json
import os
import subprocess
import sys

HERDR = os.environ.get("HERDR_BIN_PATH") or "herdr"
SOURCE = "kuhku.pane-id"


def main() -> int:
    out = subprocess.run([HERDR, "pane", "list"], capture_output=True, text=True, check=True).stdout
    panes = json.loads(out)["result"]["panes"]
    failed = 0
    for pane in panes:
        pane_id = pane["pane_id"]
        result = subprocess.run(
            [HERDR, "pane", "report-metadata", pane_id, "--source", SOURCE, "--token", f"id={pane_id}"],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            failed += 1
            print(f"{pane_id}: {result.stderr.strip()}", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
