e = int(input('input the sec : '))
hour = e // 3600
min = e % 3600 // 60
sec = e % 60
print(e, 'sec is', hour, 'hour', min, 'min', sec, 'sec')