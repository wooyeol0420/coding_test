import random

def play_game():
    player_card = random.randint(1, 20)
    dealer_card = random.randint(1, 20)

    print(f"プレイヤーのカード: {player_card}")
    print(f"ディーラーのカード: {dealer_card}")

    if player_card > dealer_card:
        print("プレイヤーの勝ちです！")
    elif player_card < dealer_card:
        print("ディーラーの勝ちです！")
    else:
        print("引き分けです！")

play_game()
