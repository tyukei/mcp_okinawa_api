
![1000000600](https://github.com/user-attachments/assets/26e28887-78bb-444b-87f9-a3e206f26edd)


# setup
以下のコマンドを実行する
```
uv init -p python3.11
uv venv
source .venv/bin/activate
uv sync
```

mcp clientの設定する
設定ファイルは以下にある
```
code ~/Library/Application\ Support/Claude/claude_desktop_config.json
```
設定ファイルには、以下をコピペする
ただし、user_name, pathは変更する
```
{
  "mcpServers": {
    "okinawa-tourism": {
      "command": "/Users/<user_name>/.local/bin/uv",
      "args": [
        "--directory",
        "<path>",
        "run",
        "python",
        "main.py"
      ],
      "env": {
        "RESOURCE_ID": "<db_id>"
      }
    }
  }
}
````

commandのパスは以下より取得
```
which uv
```

argsのパスは以下より取得
```
pwd
```

envのidは以下より取得
https://odcs.bodik.jp/470007/

| 名称                                       | UUID                                   |
|------------------------------------------|----------------------------------------|
| 沖縄県公共施設一覧                         | b621375e-0737-4de2-bf0f-c6a573f2ea85    |
| 「沖縄食材の店」登録店舗一覧               | 6d89d0fe-401f-4753-8548-4cc71c8ee5bf    |
| 教育施設一覧                               | 999fd0ba-4588-4660-8855-559703434624    |
| 新規食品営業許可・届出施設一覧            | aee32ccf-01f7-439a-9789-20c329167ba0    |


