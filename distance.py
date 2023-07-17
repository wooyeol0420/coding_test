def calculate_distance(time, average_speed):
    distance = time * average_speed
    return distance

time = float(input("動いた時間(時間単位)を入力してください。: "))
average_speed = float(input("平均速度(距離の単位と合う単位)を入力してください。: "))

distance = calculate_distance(time, average_speed)
print("動いた距離は", distance, "です。")