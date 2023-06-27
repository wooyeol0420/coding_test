marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number +1
    if mark >= 60:
        print("%d番の学生は合格です。" % number)
    else:
        print("%d番学生は不合格です。" % number)