from typing import Optional

# Userクラス
# ユーザーのIDと名前を属性としてもつ
class User:
    def __init__(self, id: int, name:str):
        # ユーザーID
        self.id = id
        # ユーザー名
        self.name = name

# ダミーDBとして機能するユーザーリスト
user_list = [
    User(id=1, name="内藤"),
    User(id=2, name="佐藤"),
    User(id=3, name="鈴木"),
]

# 指定したユーザIDに対応するユーザをuser_listから検索する関数
def get_user(user_id: int) -> Optional[User]:
    for user in user_list:
        if user.id == user_id:
            return user
    # ユーザーが見つからない場合はNoneを返す
    return None