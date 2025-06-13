def num_tusk(a):
    if a == 1:
        import random
        x = []
        z = 0
        for i in range(5):
            y = random.randint(1,10)
            x.append(y)
        print(x)
        print('угадайте число от 1 до 10')
        z = int(input('введите число - '))
        for i in x:
            if z == i:
                print('Поздравляю, Вы угадали число!')
                break
            else:
                print('Нет такого числа!')
                break

    if a == 2:
        # 2
        import random
        x = [random.randint(0,9) for i in range(5)]
        y = []

        print(x)

        for i in x:
            if x.count(i)>1 and i not in y:
                y.append(i)

        if y:
            print("повторяющиеся числа - ", y)
        else:
            print('повторяющихся чисел нет')


# 3
    if a == 3:
        import random
        x = ('понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье')
        q = list(x)
        z = []  # выходные
        r = list(x)  # рабочие дни
        w = int(input('сколько выходных дней вы хотите? - '))
        for i in range(w):
            y = random.choice(q)
            z.append(y)
            q.remove(y)
        print('Ваши выходные дни: ', z)
        print('Ваши рабочие дни: ', q)


    if a == 4:
        import random

        x = ['Иванов','Лазарев','Исаев','Гордеев','Устинов','Тихонов','Яковлев','Рябов','Жуков','Григорьев']
        y = ['Алексеев','Никулин','Шевченко','Шумакова','Шакиров','Пищикова','Ившина','Нафиков','Горбачёва','Коробейникова']
        z = []
        for i in range(5):
            q = random.choice(x)
            p = random.choice(y)
            z.append(q)
            z.append(p)
        w = tuple(z)

        print(x,y,z,len(z),sorted(w), sep = '\n')
        if 'Иванов' in w:
            print(w.count('Иванов'))
        else:
            print('Иванов отсутствует')

while True:
    x = int(input('     Введите номер задания: '))
    if x == 0:
        break
    else:
        num_tusk(x)