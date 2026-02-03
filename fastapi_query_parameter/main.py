from fastapi import FastAPI
from typing import Optional
from data import get_books_by_category

app = FastAPI()

# クエリパラメータで指定されたカテゴリに基づいて書籍情報を検索し、結果をJSON形式で返す
# listとdictの違い：listは順序があり、dictは順序がない(
# listはC/C++における配列、dictは連想配列
@app.get("/books/")
async def read_books(
    category: Optional[str] = None
) -> list[dict[str, str]]:
    # クエリパタメータで指定されたカテゴリに基づいて書籍を検索する
    result = get_books_by_category(category)
    # 結果を辞書のリストとして返す
    # リスト内包表記を使って、resultの各要素（Bookオブジェクト）を辞書に変換する
    # Bookオブジェクトの属性（id, title, category）を辞書のキーと値にする
    return [{
        "id": book.id,
        "title": book.title,
        "category": book.category
    } for book in result]