from typing import Optional, List

# 書籍情報を表すクラス
class Book:
    # __init__はコンストラクタであり、クラスのインスタンスが生成されるときに自動的に呼び出されるメソッド
    # selfはインスタンス自身を指す
    # id, title, categoryは引数として受け取る
    def __init__(self, id: str, title: str, category:str):
        # 書籍ID
        self.id = id
        # 書籍タイトル
        self.title = title
        # 書籍カテゴリ
        self.category = category

# ダミーの書籍情報リスト
# category: technical:技術書, business:ビジネス書, novel:小説, other:その他
books = [
    Book("1", "Python入門", "technical"),
    Book("2", "Python実践", "technical"),
    Book("3", "Forbs", "business"),
    Book("4", "ONE PIECE", "novel"),
    Book("5", "TOEIC公式問題集", "other"),
]

# カテゴリに基づいて書籍を検索する関数
# もしcategoryがNoneなら、全ての書籍を返す
def get_books_by_category(
    category: Optional[str] = None
) -> List[Book]:

    if category is None:
        # categoryがNoneの場合、全ての書籍を返す
        return books
    else:
        # リスト内包表記を使って、指定されたカテゴリに一致する書籍のみを抽出
        # bookはbooksリストの各要素（Bookオブジェクト）を指す
        # book.categoryはBookオブジェクトのcategory属性（文字列）を指す
        # book.category == categoryは、Bookオブジェクトのcategory属性が指定されたcategoryと等しいかどうかを判定する
        # 等しい場合、そのBookオブジェクトが新しいリストに含まれる
        return [book for book in books if book.category == category]