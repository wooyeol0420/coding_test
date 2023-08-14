import time

def play_sound(repeats):
    sounds = ["ティック", "トック"]
    for _ in range(repeats):
        for sound in sounds:
            print(sound)
            time.sleep(30 / repeats)

try:
    repeats_per_minute = int(input("何回繰り替えますか？"))
    
    if repeats_per_minute <= 0:
        raise ValueError

    while True:
        play_sound(repeats_per_minute)

except ValueError:
    print("エラー。有効な数字を入力してください。")
#Ctril+cで終了