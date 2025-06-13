def num_tusk(a):
    if a == 1:
        x = int(input('введите число; '))
        if x % 3 == 0:
            print('число делиться на 3')
        else:
            print('число не делиться на 3')

    if a == 2:
        x = input('введите число: ')
        y = 100
        try:
            b = int(x)
            z = y / b
        except ZeroDivisionError:
            b = 0
            print('Error - "X" не должно быть равно 0')
        except ValueError:
            print('Error - "X" не должно быть строкой')
        else:
            print(z)

    if a == 3:
        x = input('введите дату: ')
        y = int(x[0:2])
        z = int(x[3:5])
        w = int(x[-2:])
        if y * z == w:
            print('True')
        else:
            print('False')

    if a == 4:
        x = int(input('введите число: '))
        b = str(x)
        y2 = 0
        w2 = 0
        if len(b) % 2 == 0:
            q = len(b) // 2
            y = b[:q]
            w = b[q:]

            for i in y:
                y2 += int(i)
            for i in w:
                w2 += int(i)

            if y2 == w2:
                print('этот билет Счастливый')
            else:
                print('этот билет не Счастливый')
        else:
            print('введите число с чётным количеством цифр ')


while True:
    x = int(input('     Введите номер задания: '))
    if x == 0:
        break
    else:
        num_tusk(x)



#