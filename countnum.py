def count_d_in_range(a, b, c, d):
    count = 0
    for num in range(a, b + 1):
        if num % c == 0 and str(d) in str(num):
            count += 1
    return count

A = int(input("Aの値："))
B = int(input("Bの値："))
C = int(input("Cの値："))
D = int(input("Dの値："))

result = count_d_in_range(A, B, C, D)
print("範囲内で数字Dが現れる個数：", result)
