def calculate_amount_per_ratio(total_amount, ratios):
    total_ratio = sum(ratios)
    amounts = [round(total_amount * ratio / total_ratio) for ratio in ratios]
    return amounts

try:
    total_amount = float(input("総量(ml)を入力してください。: "))
    num_ratios = int(input("比率の個数を入力してください。: "))

    ratios = []
    for i in range(num_ratios):
        ratio = float(input(f"{i+1}番の比率を入力してください。: "))
        ratios.append(ratio)

    amounts = calculate_amount_per_ratio(total_amount, ratios)

    print("各比率の量:")
    for i, amount in enumerate(amounts):
        print(f"{i+1}番の比率: {amount} ml")

except ValueError:
    print("エラー。有効な数字を入力してください。")