def calculate_alcohol_consumed(volume_ml, alcohol_percent):
    alcohol_content = volume_ml * (alcohol_percent / 100)
    return alcohol_content

try:
    volume_ml = float(input("飲んだお酒の量をミリリットル(ml)で入力してください："))
    alcohol_percent = float(input("お酒のアルコール度数を入力してください："))

    alcohol_consumed = calculate_alcohol_consumed(volume_ml, alcohol_percent)
    print(f"飲んだお酒から合計で{alcohol_consumed:.2f} mlのアルコールを摂取しました。")

except ValueError:
    print("入力エラー：有効な数字を入力してください。")
