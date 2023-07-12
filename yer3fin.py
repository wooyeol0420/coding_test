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

def convert_to_ad(era, era_year):
    if era == "令和":
        ad_year = 2018 + era_year
    elif era == "平成":
        ad_year = 1988 + era_year
    elif era == "昭和":
        ad_year = 1925 + era_year
    else:
        ad_year = -1
    return ad_year

era_or_ad = input("和暦または西暦を入力してください: ")

if era_or_ad.isnumeric():
    ad = int(era_or_ad)
    era, era_year = convert_to_era(ad)
    if era_year != -1:
        print(f"西暦{ad}年は{era}{era_year}年です。")
    else:
        print("不明な西暦です。")
else:
    era, era_year = era_or_ad[:-1], int(era_or_ad[-1])
    ad = convert_to_ad(era, era_year)
    if ad != -1:
        print(f"{era}{era_year}年は西暦{ad}年です。")
    else:
        print("無効な和暦です。")