from mcp.server.fastmcp import FastMCP
# from mcp.server.fastmcp.prompts import UserMessage
import httpx
from dotenv import load_dotenv
import os

load_dotenv()

# CKAN API のベース URL
CKAN_BASE   = "https://data.bodik.jp/api/3/action"
# 対象リソース ID
RESOURCE_ID = os.getenv("RESOURCE_ID")

# FastMCP サーバインスタンスを生成
mcp = FastMCP("OkinawaTourism")  

# --- 1) Resource: 最初の N 件取得 ---  
@mcp.resource("okinawa://records?limit={limit}")
async def get_records(limit: int = 5) -> dict:
    """
    CKAN DataStore API（datastore_search）を使用して、
    指定された件数のレコードを取得します。

    引数:
        limit (int): 取得するレコードの件数。デフォルトは5。

    戻り値:
        dict: APIからのJSONレスポンスを含む辞書。
    """
    params = {"resource_id": RESOURCE_ID, "limit": limit}
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{CKAN_BASE}/datastore_search", params=params)
        resp.raise_for_status()
        return resp.json()

# --- エンドポイント②: キーワードでレコードを検索 ---  
@mcp.tool()
async def search_records(q: str) -> dict:
    """
    CKAN DataStore API（datastore_search）の `q` パラメータを使用して、
    レコードをキーワード検索します。

    引数:
        q (str): 検索キーワード。

    戻り値:
        dict: APIからのJSONレスポンスを含む辞書。
    """
    params = {"resource_id": RESOURCE_ID, "q": q}
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{CKAN_BASE}/datastore_search", params=params)
        resp.raise_for_status()
        return resp.json()

# # --- プロンプト: 沖縄方言での応答を生成 ---  
# @mcp.prompt(name="okinawa_dialect_prompt", description="指定されたキーワードに対する沖縄方言の応答を生成します。")
# def okinawa_dialect_prompt(keyword: str) -> UserMessage:
#     """
#     指定されたキーワードに対する沖縄方言の応答を生成します。

#     引数:
#         keyword (str): 応答を生成するためのキーワード。

#     戻り値:
#         UserMessage: 沖縄方言での応答を含むユーザーメッセージ。
#     """
#     content = f"ハイサイ！「{keyword}」について、沖縄の言葉で教えてくれませんか？"
#     return UserMessage(content=content)

# --- エントリポイント: SSE トランスポートでサーバ起動 ---  
if __name__ == "__main__":
    mcp.run()
