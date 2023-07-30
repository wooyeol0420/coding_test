def fleming_left_hand_rule(current_direction, magnetic_field_direction):
    if current_direction == "上向き" and magnetic_field_direction == "右側":
        return "電流方向に対する力の方向：左側"
    elif current_direction == "上向き" and magnetic_field_direction == "左側":
        return "電流方向に対する力の方向：右側"
    elif current_direction == "下向き" and magnetic_field_direction == "右側":
        return "電流方向に対する力の方向：右側"
    elif current_direction == "下向き" and magnetic_field_direction == "左側":
        return "電流方向に対する力の方向：左側"
    else:
        return "入力された方向が正しくありません。"

try:
    current_direction = input("電流の方向を入力してください（上向きまたは下向き）：")
    magnetic_field_direction = input("磁場の方向を入力してください（右側または左側）：")

    result = fleming_left_hand_rule(current_direction, magnetic_field_direction)
    print(result)

except ValueError:
    print("入力エラー：正しい方向を入力してください。")
