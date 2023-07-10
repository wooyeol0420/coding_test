def convert_to_ad(era, year):
    if era == "昭和":
        ad_year = 1925 + int(year)
    elif era == "平成":
        ad_year = 1988 + int(year)
    elif era == "令和":
        ad_year = 2018 + int(year)
    else:
        ad_year = -1
    return ad_year

era = input("入力してください: ")
year = input("入力してください: ")
ad = convert_to_ad(era, year)
if ad != -1:
    print(f"{era}{year}年は西暦{ad}年です。")
else:
    print("無効な入力です。")