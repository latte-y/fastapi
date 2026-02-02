# 1.整数型
def add(num1: int, num2: int) -> str:
    result: str = 'Result of Addition: '
    return result + str(num1 + num2)

# 2.文字列型
def greet(name: str) -> str:
    return f"Good Morning! {name}!"

# 3.浮動小数点型
def divide(dividend: float, divisor: float) -> float:
    return dividend / divisor

# 4.リスト型
def process_items(items: list[str]) -> None:
    for item in items:
        print(item)

# 5.辞書型
def count_characters(word_list: list[str]) -> dict[str, int]:
    count_map: dict[str, int] = {}
    for word in word_list:
        # 例：count_map["Apple"] = len("Apple")
        # つまり、{"Apple: 5"}になる
        count_map[word] = len(word)
    return count_map

# --------------　出力 --------------- #
print(add(1, 2))
print(greet("Yuki"))
print(divide(22, 7))
process_items(["リスト", "ゴリラ", "ラッパ"])
character_counts = count_characters(["AWS", "Google Cloud", "Microsoft Azure"])
print("文字に対する文字数は＝＞", character_counts)