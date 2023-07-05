import random

cnt = 0

try:
    cnt = int(input("番号をいくつ作りましょうか : "))
except ValueError :
    print("数字を入力してください")


for i in range(cnt) :
    lotto = random.sample(range(1, 46), 6) 
    lotto.sort() 
    print(lotto)