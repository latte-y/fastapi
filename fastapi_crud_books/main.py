from fastapi import FastAPI, HTTPException
from book_schemas import BookSchema, BookResponseSchema

app = FastAPI()

# デモ用のDBがわりに使うリスト
# ダミーの書籍情報リスト
books: list[BookResponseSchema] = [
    # BookResponseSchemaのインスタンスを生成して、booksリストに追加する
    BookResponseSchema(id=1, title="Python入門", category="technical"),
    BookResponseSchema(id=2, title="Python応用", category="technical"),
    BookResponseSchema(id=3, title="週刊ダイヤモンド", category="magazine"),
    BookResponseSchema(id=4, title="ONE PIECE", category="comics"),
    BookResponseSchema(id=5, title="北欧家具カタログ", category="design")
]

# ---------------------------------------------
# 書籍を追加するためのエンドポイント
# 引数：BookSchema
# 戻り値：BookResponseSchema
# ---------------------------------------------
# response_model：返り値の型を指定
@app.post("/books/", response_model=BookResponseSchema)
def create_book(book: BookSchema):
    # 書籍IDを作成
    # booksリストの最大IDを取得して、1を足して新しいIDを生成する（booksリストが空の場合、default=0で0を返す）
    new_book_id = max([book.id for book in books], default=0) + 1
    # 新しい書籍を作成
    """
        **book.model_dump() と書くことで、元のデータにある項目は全部まとめてコピーして、足りない id だけ追加する
        book.model_dump()：Pydanticモデルの値を辞書型に変換する
        
        例：
            ・book.model_dump() -> {"title": "Python入門", "category": "technical"}
            ・new_book_id = 6
            の場合
            new_book = BookResponseSchema(id=6, title="Python入門", category="technical")になる
        つまり、
            new_book = BookResponseSchema(id=new_book_id, **book.model_dump())
            は
            new_book = BookResponseSchema(id=new_book_id, title="Python入門", category="technical")
            と同じ
    """
    new_book = BookResponseSchema(id=new_book_id, **book.model_dump())
    # ダミーデータに追加
    books.append(new_book)
    # 登録書籍データを返す
    return new_book


# ---------------------------------------------
# すべての書籍を取得するためのエンドポイント
# 引数：なし
# 戻り値：BookResponseSchemaのリスト
# ---------------------------------------------
@app.get("/books/", response_model=list[BookResponseSchema])
def read_books():
    # すべての書籍データを取得
    return books


# ---------------------------------------------
# 書籍情報をidによって1件取得するエンドポイント
# 引数：書籍ID
# 戻り値：BookResponseSchema
# ---------------------------------------------
@app.get("/books/{book_id}", response_model=BookResponseSchema)
def read_book(book_id: int):
    # 指定されたIDの書籍データを取得
    for book in books:
        if book.id == book_id:
            return book
    # 該当する書籍が見つからない場合、404エラーを返す
    raise HTTPException(status_code=404, detail="Book not found")


# ---------------------------------------------
# idに対応する書籍情報を更新するためのエンドポイント
# 引数：
#   書籍ID
#   BookSchema
# 戻り値：BookResponseSchema
# ---------------------------------------------
@app.put("/books/{book_id}", response_model=BookResponseSchema)
def update_book(book_id: int, book: BookSchema):
    # 特定のIDの書籍を更新
    # enumerate：リストの要素とそのインデックスを同時に取得する
    for index, existing_book in enumerate(books):
        if existing_book.id == book_id:
            update_book = BookResponseSchema(id=book_id, **book.model_dump())
            books[index] = update_book
            return update_book
    # 該当する書籍が見つからない場合、404エラーを返す
    raise HTTPException(status_code=404, detail="Book not found")


# ---------------------------------------------
# idに対応する書籍情報を削除するためのエンドポイント
# 引数：書籍ID
# 戻り値：BookResponseSchema
# ---------------------------------------------
@app.delete("/books/{book_id}", response_model=BookResponseSchema)
def delete_book(book_id: int):
    # 特定のIDの書籍を削除
    for index, book in enumerate(books):
        if book.id == book_id:
            # pop(index)：指定されたインデックスの要素を削除する
            books.pop(index)
            # 削除した書籍のデータを返す
            return book
    # 該当する書籍が見つからない場合、404エラーを返す
    raise HTTPException(status_code=404, detail="Book not found")
