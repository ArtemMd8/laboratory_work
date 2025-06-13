
def num_tusk(a):
    if a == 1:
        #1
        from pathlib import Path
        from PIL import Image

        # files_render - переменная переходящая в папке

        Images_link = input('ведите путь к папке с исходными файлами - ')
        Rendered_link = input('ведите путь к папке с отредактированными файлами - ')

        Main_link = Path(Images_link)
        Main_render = Path(Rendered_link)

        for files_render in Main_link.glob('*.jpg'):
            x = Image.open(files_render)
            x = x.rotate(180)
            final = Main_render /  files_render.name #объединяет путь
            x.save(final)

    if a == 2:
        #2
        from pathlib import Path
        from PIL import Image

        # files_render - переменная переходящая в папке

        Images_link = input('ведите путь к папке с исходными файлами - ')
        Rendered_link = input('ведите путь к папке с отредактированными файлами - ')

        Main_link = Path(Images_link)
        Main_render = Path(Rendered_link)
        a = ['*.jpg','*.png']
        for i in a:
            for files_render in Main_link.glob(i):
                x = Image.open(files_render)
                x = x.rotate(180)
                final = Main_render /  files_render.name #объединяет путь
                x.save(final)

    if a == 3:
        #3
        import csv
        summa = 0

        with open('utf8.csv') as f:
            read = csv.reader(f)
            next(read)
            for i in read:
                x,y,z = i
                y = int(y)
                z = int(z)
                summa += z*y
                print(f"{x} - {y} шт. за {z} руб.")
        print(f"Итоговая сумма: {summa} руб.")

while True:
    a = int(input('     Введите номер задания: '))
    if a == 0:
        break
    else:
        num_tusk(a)