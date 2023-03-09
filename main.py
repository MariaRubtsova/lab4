from random import randint

def kalk12():
    tr = 0
    fl = 0
    x = int()
    y = int()
    while fl < 3:
        x = randint(1, 100)
        y = randint(1, 100)
        print(x, "+", y)
        n = int(input("ответ:"))
        if (n == x + y):
            print("правильно!")
            tr += 1
        else:
            print("ошибка!")
            fl += 1
    print("количество верных ответов", tr)

kalk12()
