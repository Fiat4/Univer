import random
print("Приветствую тебя,мой орогой друг! \nСейчас я дам тебе пример и тебе стоит его решить. \nУ тебя есть 3 попытки на один пример.")
i = 1
while i == 1:
    lives = 3
    g = lives
    print('Колличество жизней:',g)
    a = random.randint(0,999)
    b = random.randint(0,999)
    v = "-"
    t = a - b
    while g > 0:
        if g == 3:
            r = "Решите пример"
        if g != 3:
            r = 'Попробуйте снова'
        print(r ,a, v, b)
        e = int(input())
        if e == t:
            print('Ты выиграл)а)!')
            break
        if e != t:
            g = g - 1
            if g == 0:
                print('Ты проиграл(а)')
                break
        print('Неправильно \nКолличество жизней:', g)


    print("Не хочешь ли попробовать снова? \nДа - 1\nНет - 0")
    h = int(input())
    if h == 1:
        i = 1
    else:
        i = 0
