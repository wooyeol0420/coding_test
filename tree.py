def calculate_trees_needed(a, b, c, spacing):
    if a + b > c and a + c > b and b + c > a:
        perimeter = a + b + c
        trees_needed = perimeter / spacing
        return int(trees_needed) + 1 
    else:
        return 0

A = float(input("第1辺の長さA："))
B = float(input("第2辺の長さB："))
C = float(input("第3辺の長さC："))
spacing = float(input("木の間隔："))

trees_needed = calculate_trees_needed(A, B, C, spacing)
print("必要な木の数：", trees_needed)
