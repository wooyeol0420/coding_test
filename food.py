import random

menus = ['チャハン', '寿司', '鍋', 'ラーメン', 'バスタ', '牛丼', '混ぜそば', 'そば', '親子丼', 'とんかつ']
prices = [500, 1000, 800, 900, 600, 480, 700, 500, 500, 700]

print('メニュー:')
for i in range(len(menus)):
    print(menus[i], prices[i])


i = random.randint(0, len(menus) - 1)
print('おすすめ:', menus[i])
print('価格:', prices[i])