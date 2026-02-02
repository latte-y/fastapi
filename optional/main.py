from typing import Optional

# ユーザー情報を持つプロフィールを返却する関数
# 引数：文字列型、文字列型/Optional、数値型/Optional
# 戻り値：辞書型
def get_profile(
    email: str, # デフォルト値を設定していないので、必ず引数emailには値が入る
    username: Optional[str] = None,
    age: Optional[int] = None
) -> dict:
    
    # 辞書型の変数profileを定義
    profile = {"email": email}
    
    if username:
        # 引数usernameが引数に存在する場合
        profile["username"] = username
    if age:
        # 引数ageが引数に存在する場合
        profile["age"] = age
        
    return profile

# ============================================================
# 呼び出し
# ============================================================
# usernameとageを指定しない場合
user_profile = get_profile(email="aaa@exmple.com")
# 表示
print(user_profile)

# usernameとageの両方を指定する場合
complete_profile = get_profile(
    email="bbb@example.com",
    username="元太",
    age=30)
# 表示
print(complete_profile)