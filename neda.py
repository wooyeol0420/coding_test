def calculate_cost_price(A, B, C):
    P = C
    cost_price = P / (1 + A / 100)

    discounted_price = P * (1 - B / 100)

    if cost_price <= 0 or discounted_price != C:
        return "仕入れ値が存在しないか、不正確な割引率です。"
    else:
        return cost_price

try:
    A = float(input("利益率（A％）を入力してください: "))
    B = float(input("割引率（B％）を入力してください: "))
    C = float(input("割引後の価格（C円）を入力してください: "))

    cost_price = calculate_cost_price(A, B, C)

    print(f"仕入れ値は {cost_price} 円です。")

except ValueError:
    print("入力エラー：浮動小数点数を入力してください。")
