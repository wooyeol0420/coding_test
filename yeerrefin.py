import datetime

def convert_to_wagcal(year):
    if year >= 1868 and year <= 1911:
        era = "明治"
        era_year = year - 1867
    elif year >= 1912 and year <= 1925:
        era = "大正"
        era_year = year - 1911
    elif year >= 1926 and year <= 1988:
        era = "昭和"
        era_year = year - 1925
    elif year >= 1989:
        era = "平成"
        era_year = year - 1988
    else:
        return "対応していない年号です"

    return f"{era}{era_year}年"

def convert_to_ad(era, era_year):
    if era == "明治":
        year = era_year + 1867
    elif era == "大正":
        year = era_year + 1911
    elif era == "昭和":
        year = era_year + 1925
    elif era == "平成":
        year = era_year + 1988
    else:
        return "対応していない元号です"

    return year

def calculate_age(birth_year):
    today = datetime.date.today()
    age = today.year - birth_year
    if today < datetime.date(today.year, birth_year.month, birth_year.day):
        age -= 1
    return age

def main():
    while True:
        choice = input("変換する形式を選んでください（1: 和暦から西暦、2: 西暦から和暦、3: 年齢計算、4: 終了）: ")
        
        if choice == "1":
            wagcal_input = input("和暦を入力してください（例: 平成5年）: ")
            era, era_year = wagcal_input[:-1], int(wagcal_input[-1])
            ad_year = convert_to_ad(era, era_year)
            print(f"西暦{ad_year}年")
        
        elif choice == "2":
            ad_input = int(input("西暦を入力してください: "))
            wagcal_year = convert_to_wagcal(ad_input)
            print(wagcal_year)
        
        elif choice == "3":
            birth_year = int(input("生まれた年を入力してください（西暦）: "))
            age = calculate_age(birth_year)
            print(f"現在の年齢は{age}歳です")
        
        elif choice == "4":
            break
        
        else:
            print("無効な選択です")

if __name__ == "__main__":
    main()