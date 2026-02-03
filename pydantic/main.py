from datetime import datetime
from pydantic import BaseModel, ValidationError

# イベントを表すクラス
# BaseModelを継承することで、Pydanticの機能を利用できる
class Event(BaseModel):
    # イベント名（デフォルトは未定）
    name: str = "未定"
    # 開催日時
    start_datetime: datetime
    # 参加者リスト（デフォルトは空リスト）
    participants: list[str] = []

# ダミーデータ（外部からのイベントデータのつもり）
external_data = {
    "name": " FastAPI勉強会",
    "start_datetime": "2026-02-03 22:25",
    "participants": ["Alice", "Bob", "Charlie"]
}

# 辞書のアンパック
# **は辞書のキーと値をクラスの引数に展開する
event = Event(**external_data)
print("イベント名：", event.name, type(event.name))
print("開催日時：", event.start_datetime, type(event.start_datetime))
print("参加者：", event.participants, type(event.participants))