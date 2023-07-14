from datetime import datetime

current_year = datetime.now().year

user_input = input("年齢、もしくは生まれた年を西暦で後ろ二桁を入力してください。: ")

if user_input.endswith("年"):
    birth_year = int(user_input[:2]) + 1900
    age = current_year - birth_year
    print("あなたは", str(age) + "歳です。")
elif user_input.endswith("歳"):
    age = int(user_input[:2])
    birth_year = current_year - age
    print("あなたは", str(birth_year)[-2:] + "年度に生まれました。")
else:
    print("「００歳」、もしくは「００年」で入力してください。")