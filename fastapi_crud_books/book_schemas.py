from pydantic import BaseModel

# 書籍の作成と更新に使用するスキーマ
# BaseModelの嬉しいところ：自動的に型チェックしてくれる
"""
    BaseModelの嬉しいところ：自動的に型チェックしてくれる
    
    完全に違う型で変換不可能な場合:
    例: None や 辞書型などを渡すと、コメントの通りエラーになります。

    変換可能な型の場合（ここが補足点）:
    例: 数値の 123 を渡すと、Pydanticはこれを文字列の "123" に自動変換して受け入れます。この場合はエラーになりません。
    int 定義のフィールドに 文字列 "10" を渡した場合も、数値の 10 に変換されます。
"""
class BookSchema(BaseModel):
    # タイトル
    title: str
    # カテゴリ
    category: str

# レスポンス用のスキーマには、書籍スキーマを継承してidも含める
class BookResponseSchema(BookSchema):
    # ID
    id: int
