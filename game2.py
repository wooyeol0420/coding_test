import random

sel = ['チョキ', 'グー', 'パー']
result = {0: '勝利しました。', 1: '負けました。', 2: '引き分けました。'}

def checkWin(user, com):

    if not user in sel:
       print('間違いました。もう一度入力してください。')
       return False

    print(f'使用者 ( {user} vs {com} ) コンピューター')
    if user == com:
        state = 2
    elif user == 'チョキ' and com == 'グー':
        state = 1
    elif user == 'グー' and com == 'パー':
        state = 1
    elif user == 'パー' and com == 'チョキ':
        state = 1
    else:
        state = 0
    print(result[state])
    return True


print('\n-------------------------------------------')
while True:
    user = input("チョキ, グー, パー : ")
    com = sel[random.randint(0, 2)]
    if checkWin(user, com):
        break
print('-------------------------------------------\n')