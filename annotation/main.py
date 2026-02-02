from typing import Annotated

# 引数で渡された整数値が指定された範囲内にあるかをチェックする関数
# 引数：数値型（Annotated)
# 戻り値：None
def process_value(
    value: Annotated[int, "range: 0 <= value <= 100"]
) -> None:
    # 引数で渡された整数値が範囲内にあるかをチェックする
    if 0 <= value <= 100:
        print(f"Value is in range: {value}")
    else:
        raise ValueError(f"Value is out of range: {value}")

# ==========================================================
# 正しい値で関数をテスト
process_value(50)

# ==========================================================
# 範囲外の値で関数をテスト
try:
    process_value(150)
except ValueError as e:
    print(e)