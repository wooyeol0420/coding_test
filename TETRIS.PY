import random

def create_ladder(height, players):
    ladder = []
    for _ in range(height):
        row = []
        for _ in range(players):
            if random.random() < 0.3:  
                row.append("|")
            else:
                row.append(" ")
        ladder.append(row)
    return ladder

def print_ladder(ladder):
    for row in ladder:
        print("|", end="")
        for cell in row:
            print("-" if cell == "|" else " ", end="")
            print("|", end="")
        print()

def play_game(players):
    height = 5  
    ladder = create_ladder(height, players)
    print_ladder(ladder)

    winner = random.randint(0, players - 1)
    print("\n当選位置:", winner + 1)

    return winner

try:
    num_players = int(input("プレイヤーの数を入力してください："))
    if num_players <= 0:
        raise ValueError
    winner = play_game(num_players)
    print(f"\nプレイヤー{winner + 1}が当選しました！")

except ValueError:
    print("入力エラー：有効な数字を入力してください。")
