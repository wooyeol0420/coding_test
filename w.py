def calculate_filling_time(hose_rate, tank_capacity):
    filling_time = tank_capacity / hose_rate
    return filling_time

hose_rate = float(input("時間当たり出る水の量 (L/時間): "))
tank_capacity = float(input("容器の大きさ (L): "))

result = calculate_filling_time(hose_rate, tank_capacity)

print("容器がいっぱいになる時間は:", result, "時間")