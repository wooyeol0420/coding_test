def convert_to_era(ad_year):
    if ad_year >= 2019:
        era = "令和"
        era_year = ad_year - 2018
    elif ad_year >= 1989:
        era = "平成"
        era_year = ad_year - 1988
    elif ad_year >= 1926:
        era = "昭和"
        era_year = ad_year - 1925
    else:
        era = "不明"
        era_year = -1
    return era, era_year

ad = int(input("西暦を入力してください: "))
era, era_year = convert_to_era(ad)
if era_year != -1:
    print(f"西暦{ad}年は{era}{era_year}年です。")
else:
    print("不明な西暦です。")