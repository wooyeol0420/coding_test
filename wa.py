def calculate_time_to_fill_or_empty(volume_in, volume_out):
    if volume_in <= 0 or volume_out >= 0:
        return "入る量は正の数で、抜ける量は負の数である必要があります。"

    if volume_in == volume_out:
        return "容器は常に同じ量の水を入れて排出するため、容器は絶対に満杯になりません。"

    time = volume_in / (volume_in - volume_out)
    return f"{time:.2f}時間後に容器は満杯になります。"

try:
    volume_in = float(input("容器に入れる水の量を入力してください（正の数）："))
    volume_out = float(input("容器から抜く水の量を入力してください（負の数）："))

    result = calculate_time_to_fill_or_empty(volume_in, volume_out)
    print(result)

except ValueError:
    print("入力エラー：有効な数字を入力してください。")
