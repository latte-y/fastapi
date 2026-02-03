from fastapi import FastAPI, HTTPException
from typing import Optional
from data import get_user, User

app = FastAPI()

# ユーザーIDをパスパラメータとして受け取り、ユーザ情報を返すエンドポイント
# 引数：ユーザID（整数）
# 戻り値：ユーザー情報（辞書型）
@app.get("/users/{user_id}")
async def read_user(user_id: int) -> dict:
    # ユーザー情報の取得
    # Optional型を使っている理由：get_user関数がNoneを返す可能性があるため
    user: Optional[User] = get_user(user_id)

    if user is None:
        # ユーザーが見つからない場合は404エラーを返す
        raise HTTPException(status_code=404, detail="User not found")
    
    # ユーザー情報が見つかった場合は辞書型に変換して返す
    return {"user_id": user.id, "user_name": user.name}