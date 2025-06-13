def num_tusk(a):
    if a == 1:
# номер 5.1
        x = int(input("enter number: "))
        y = ""
        for i in range(x):
            z = input("enter word: ")
            y += z + " "
        print(y)


    if a == 2:
# номер 5.2
        y = ''
        z = ''
        while True:
            y = input("enter word: ")
            if y == 'stop':
                break
            else:
                z += y + ' '
        print(z)

    if a == 3:
# номер 5.3
        def word():
            while True:
                x = input('enter word; ').lower()
                y = x
                if x =='stop':
                    break
                elif 'ф' in x:
                    print("Ого! Это редкое слово!")
                else:
                    print("Эх, это не очень редкое слово...")

        if __name__ == '__main__':
            word()


    if a == 4:
# номер 5.4
        import random
        i1 = 0
        i2 = 0
        while True:

            x = random.randint(1,10)
            y = random.randint(1,10)
            z = x + y
            print('решите выражение: ',x,' + ', y, ' = ?')

            if i1 == 3:
                print('Игра пройдена, всё решено верно')
                break
            if i2 == 3:
                print('Игра окончена, повторите арифметику')
                break


            w = int(input('Введите ответ: '))
            if z == w:
                print('Верно!')
                i1 += 1

            else:
                print('Ответ неверный')
                i2 += 1

while True:
    x = int(input('     Введите номер задания: '))
    if x == 0:
        break
    else:
        num_tusk(x)
