import random

random_number = random.randint(1,100)

game_count = 1

while True:
    try:
        my_number = int(input("1~100の間の数字を入力してください。: "))

        if my_number > random_number:
            print("ダウン")
        elif my_number < random_number:
            print("アップ")
        elif my_number == random_number:
            print(f"おめでとうございます！数字は {random_number}で、 {game_count}回で当てました。")
            break

        game_count = game_count + 1
    except:
        print("Error発生。数字を入力してください。")