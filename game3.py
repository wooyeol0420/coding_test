import random

num = random.randint(1,10)
cnt = 0
print(num)

while True:
    cnt += 1
    usr = int(input('入力 : '))
    if usr == num:
        print('正解です!')
        break
    else:
        print("間違いました。")
        print("*"*40)
        
    if cnt == 5:
        print('回数オーバー、 正解は%dです。'%num)