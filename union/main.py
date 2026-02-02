# 関数の引数がintがたかstr型のいずれかであることを指定し、結果を返す関数
# 引数：整数型/文字列型
# 戻り値：文字列型

def parse_input(value: int | str) -> str:
    # 型判定
    if isinstance(value, int):
        return f"value is int: {value}"
    elif isinstance(value, str):
        return f"value is str: {value}"
    else:
        raise ValueError("[Error] Input type is not int or str")


# =========================================================
# 正しい値で関数をテスト
print(parse_input(10))
print(parse_input("hello"))

# =========================================================
# 異なる値で関数をテスト
try:
    print(parse_input(10.5))
except ValueError as e:
    print(e)