def get_trash(day):
    if day == '月曜日' or day == '水曜日' or day == '金曜日':
        return '燃えるゴミ'
    elif day == '火曜日' or day == '日曜日':
        return 'ごみを出せない日'
    elif day == '木曜日':
        return '資源ごみ'
    elif day == '土曜日':
        return '燃えないゴミ'
    else:
        return '曜日だけ入力してください。'

day_of_week = input('曜日を入力してください。: ')

trash_type = get_trash(day_of_week)
print(f'{day_of_week}は{trash_type}です。')