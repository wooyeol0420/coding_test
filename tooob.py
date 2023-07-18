def calculate_meeting_time(speed_a, speed_b, distance):
    relative_speed = speed_a + speed_b
    meeting_time = distance / relative_speed
    return meeting_time

speed_a = float(input("a個体の速度 (km/h): "))
speed_b = float(input("ｂ個体の速度 (km/h): "))
distance = float(input("二つの個体の距離 (km): "))

result = calculate_meeting_time(speed_a, speed_b, distance)

print("二つの個体が合う時間:", result, "時間")