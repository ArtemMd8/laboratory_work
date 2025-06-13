def num_tusk(a):
    if a == 1:
        #1
        from PIL import Image, ImageFilter, ImageChops
        x = Image.open('num1.jpg')
        size = x.size
        print('Рзамер - фото',size)

        a = int(input('Введите левую границу - '))
        b = int(input('Введите верхнюю границу - '))
        c = int(input('Введите праую границу - '))
        d = int(input('Введите нижнюю границу - '))

        x2 = x.crop((a,b,c,d))
        x.show()
        x2.show()

    if a == 2:
        #2

        from PIL import Image
        a = Image.open('num2(1).jpg')
        b = Image.open('num2(2).jpg')
        c = Image.open('num2(3).jpg')
        d = Image.open('num2(4).jpg')
        e = Image.open('num2(5).jpg')

        x = {'Новый год': a,'Пасха': b,'9 Мая': c,'8 Марта': d,'23 Февраля': e}
        for i in x.keys():
            print(i)

        w = input('Введите название праздника - ')
        r = x[w]
        r.show()

    if a == 3:
        #3
        from PIL import Image, ImageDraw, ImageFont
        name = input('Ввведите имя - ')

        x = Image.open('num3.jpg')
        x.show()

        TEXT1 = ImageDraw.Draw(x)
        TEXT2 = ImageDraw.Draw(x)
        TEXT3 = ImageDraw.Draw(x)
        color1 = (0,255,0)
        color2 = (255,0,0)
        color3 = (0,0,255)
        FONT1 = ImageFont.truetype('impact.ttf', size=30)
        FONT2 = ImageFont.truetype('arial.ttf', size=50)
        FONT3 = ImageFont.truetype('arialbd.ttf', size=60)

        TEXT1.text((0,100),'Поздравляю! '+ name, font=FONT1, fill=color1)
        TEXT2.text((0,300),'Поздравляю! '+ name, font=FONT2, fill=color2)
        TEXT3.text((0,600),'Поздравляю! '+ name,font=FONT3,fill=color3)

        x.save('num3(r).png')
        x.show()

while True:
    x = int(input('     Введите номер задания: '))
    if x == 0:
        break
    else:
        num_tusk(x)