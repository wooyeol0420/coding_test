import time

def timer(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds
    print(f"{hours}時間 {minutes}分 {seconds}秒のタイマーを開始します。")
    time.sleep(total_seconds)
    print("タイマーが終了しました！")

try:
    hours = int(input("タイマーに設定する時間（時）を入力してください："))
    minutes = int(input("タイマーに設定する時間（分）を入力してください："))
    seconds = int(input("タイマーに設定する時間（秒）を入力してください："))
    timer(hours, minutes, seconds)

except ValueError:
    print("入力エラー：有効な数字を入力してください。")
