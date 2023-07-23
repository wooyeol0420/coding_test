def calculate_new_employees(A, B, C, D):
    total_employees_last_year = A

    male_increase = total_employees_last_year * B / 100
    female_decrease = total_employees_last_year * C / 100

    male_employees_this_year = total_employees_last_year + male_increase - D
    female_employees_this_year = total_employees_last_year - female_decrease - D

    return male_employees_this_year, female_employees_this_year

try:
    A = int(input("去年の全体の新入社員数（A）を入力してください: "))
    B = float(input("男性社員の増加率（B％）を入力してください: "))
    C = float(input("女性社員の減少率（C％）を入力してください: "))
    D = int(input("全体の社員数の減少数（D人）を入力してください: "))

    male_employees, female_employees = calculate_new_employees(A, B, C, D)

    print(f"今年の男性社員数: {male_employees}人")
    print(f"今年の女性社員数: {female_employees}人")

except ValueError:
    print("入力エラー：整数または浮動小数点数を入力してください。")
