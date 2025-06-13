def num_tusk(a):
    if a == 1:
        #1
        from PIL import Image
        x = Image.open('num1.jpg')

        x.show()
        size = x.size
        format = x.format
        color_model = x.mode

        print('размер фото - ', size)
        print('формат фото - ', format)
        print('цветовая палитра фото - ', color_model)

    if a ==2:
        #2
        from PIL import Image
        x = Image.open('num2.jpg')
        y, w = x.size


        RotateX = x.transpose(Image.FLIP_LEFT_RIGHT)
        RotateY = RotateX.transpose(Image.FLIP_TOP_BOTTOM)
        RotateW = RotateY.resize((y//3,w//3))
        RotateW.save('num2(update).jpg')

        x.show()
        RotateW.show()



    if a == 3:
        #3
        from PIL import Image, ImageFilter, ImageChops

        x1 = Image.open('num3(1).jpg')
        x12 =x1.rotate(180)
        x1.show()
        x12.show()


        x2 = Image.open('num3(2).jpg')
        x22 = x2.crop((20,80,1000,600))
        x2.show()
        x22.show()



        x3 = Image.open('num3(3).jpg')
        x32 = x3.convert('L')
        x3.show()
        x32.show()


        x4 = Image.open('num3(4).jpg')
        x42 = x4.filter(ImageFilter.BoxBlur(20))
        x4.show()
        x42.show()


        x5 = Image.open('num3(5).jpg')
        x52 = ImageChops.invert(x5)
        x5.show()
        x52.show()

    if a == 4:
        #4
        from PIL import Image, ImageDraw, ImageFont
        x = Image.open('num4.jpg')
        x.show()
        TEXT = ImageDraw.Draw(x)
        color = (255,255,0)

        FONT = ImageFont.truetype('arial.ttf', size=250)
        TEXT.text((100,500),'Watermark',font=FONT,fill=color)

        x.save('num4(r).jpg')
        x.show()

while True:
    x = int(input('     Введите номер задания: '))
    if x == 0:
        break
    else:
        num_tusk(x)