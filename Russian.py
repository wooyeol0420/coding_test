import random

def russian_roulette(num_players):
    print("ロシアンルーレットを始めます。")
    print(f"{num_players}人の参加者のうち、1人が敗北します。")

    chamber = [0] + [1] * 5

    random.shuffle(chamber)

    for i in range(num_players):
        input(f"{i+1}番の参加者のターンです。Enterキーを押して引き金を引いてください。")
        bullet = chamber.pop()
        if bullet == 0:
            print(f"{i+1}番の参加者が敗北しました。ゲームが終了します。")
            return

    print("生き残った参加者はいません。全ての参加者が無事プレイしました。")

if __name__ == "__main__":
    num_players = int(input("参加者数を入力してください："))
    russian_roulette(num_players)
