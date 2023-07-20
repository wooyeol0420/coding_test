def adjust_alcohol_percentage(current_percent, desired_percent):
    amount_of_pure_alcohol = 100
    
    current_volume = amount_of_pure_alcohol / current_percent
    
    desired_volume = amount_of_pure_alcohol / desired_percent
    
    water_to_add = desired_volume - current_volume
    
    return water_to_add

# 변수 입력 받기
current_percent = float(input("現在のアルコール: "))
desired_percent = float(input("望むアルコール: "))

result = adjust_alcohol_percentage(current_percent, desired_percent)

print("追加すべき水の量:", result, "mL")