import random

A = random.randint(1, 100)
B = random.randint(1, 10)

selected_value = random.choice([A, B])

if selected_value == A:
    result = f"A{selected_value}"
else:
    result = f"B{selected_value}"

print(f"結果：{result}")
