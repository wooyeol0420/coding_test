def calculate_water_to_add(original_percent, original_volume, target_percent):
    if target_percent < original_percent:
        water_volume = (original_volume * (original_percent - target_percent)) / target_percent
        return water_volume
    else:
        return "不可能です。作ろうとしているアルコール量が現在のアルコール量より大きいです。"

try:
    original_percent = float(input("主な材料とする酒のアルコール量: "))
    original_volume = float(input("お酒を入れようとする量 (ml): "))
    target_percent = float(input("作ろうとする酒のアルコール量: "))

    water_amount = calculate_water_to_add(original_percent, original_volume, target_percent)

    if isinstance(water_amount, float):
        if water_amount < 0:
            print("不可能です。作ろうとしているアルコール量が現在のアルコール量より大きいです。")
        else:
            print("別の液体を入れるべき量:", water_amount, "ml")
    else:
        print(water_amount)

except ValueError:
    print("エラー。数字のみ入力してください。")
