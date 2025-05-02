
# setup
```
uv init -p python3.11
uv venv
source .venv/bin/activate
uv sync
```

# mcp clientの設定
```
code ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

# <user_name>, <path>は変更する
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
        "RESOURCE_ID": "b21e91f4-7d62-44f5-895c-99a6d7e13b11"
      }
    }
  }
}
````