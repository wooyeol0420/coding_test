def calculate_probability_same_face(A, num_sides):
    if A < 1 or num_sides < 1:
        return "サイコロの面の数は１以上で入力してください。"

    total_outcomes = num_sides ** A

    same_face_outcomes = num_sides

    probability = same_face_outcomes / total_outcomes
    return probability

try:
    A = int(input("サイコロの数を入力してください。: "))
    num_sides = int(input("サイコロの面の数を入力してください。: "))

    probability_same_face = calculate_probability_same_face(A, num_sides)

    print(f"同じ面が出る確率: {probability_same_face:.4f}")

except ValueError:
    print("整数で入力してください。")
