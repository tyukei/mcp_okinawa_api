from mcp.server.fastmcp import FastMCP
import httpx
from dotenv import load_dotenv
import os

load_dotenv()

# CKAN API のベース URL
CKAN_BASE   = "https://data.bodik.jp/api/3/action"
# 対象リソース ID
RESOURCE_ID = os.getenv("RESOURCE_ID")

# FastMCP サーバインスタンスを生成
mcp = FastMCP("OkinawaTourism")  # サーバ名を任意に設定 :contentReference[oaicite:3]{index=3}

# --- 1) Resource: 最初の N 件取得 ---  
@mcp.resource("okinawa://records?limit={limit}")
async def get_records(limit: int = 5) -> dict:
    """
    CKAN DataStore の datastore_search API を呼び出し、
    指定件数分のレコードを返却します。
    """
    params = {"resource_id": RESOURCE_ID, "limit": limit}
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{CKAN_BASE}/datastore_search", params=params)
        resp.raise_for_status()
        return resp.json()
# CKAN DataStore は resource_id をテーブル名として扱います :contentReference[oaicite:4]{index=4}

# --- 2) Tool: キーワード検索 ---  
@mcp.tool()
async def search_records(q: str) -> dict:
    """
    CKAN DataStore の q パラメータによる全文検索を実行します。
    """
    params = {"resource_id": RESOURCE_ID, "q": q}
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{CKAN_BASE}/datastore_search", params=params)
        resp.raise_for_status()
        return resp.json()
# DataStore API では q, offset, limit, filters, sort 等が利用可能です :contentReference[oaicite:5]{index=5}

# # --- 3) Tool: SQL 実行 ---  
# @mcp.tool()
# async def run_sql(sql: str) -> dict:
#     """
#     CKAN DataStore の SQL クエリ実行エンドポイントを呼び出します。
#     """
#     params = {"sql": sql}
#     async with httpx.AsyncClient() as client:
#         resp = await client.get(f"{CKAN_BASE}/datastore_search_sql", params=params)
#         resp.raise_for_status()
#         return resp.json()
# # datastore_search_sql では標準的な SQL 文を投げられます :contentReference[oaicite:6]{index=6}

# サーバ起動（SSE トランスポート）
if __name__ == "__main__":
    mcp.run()
