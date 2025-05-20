def num_tusk(a):
    if a == 1:
        #1
        class Restaurant:
            def __init__(self, name, type):
                self.restaurant_name = name
                self.cuisine_type = type
            def describe(self):
                print(f"Название ресторана: {self.restaurant_name}")
                print(f"Тип кухни: {self.cuisine_type}")
            def open(self):
                print(f"Ресторан '{self.restaurant_name}' открыт!")

        class IceCreamStand(Restaurant):
            def menu(self, List):
                print("Сорт мороженнного:")
                for i in List:
                    print(i)


        x = Restaurant('китайский','основной')
        y = ['ванильный','мятный','шоколадный','ассорти','фруктовый лёд']
        z = IceCreamStand('китайский','мороженное')
        z.menu(y)

    if a == 2:
        #2
        class Restaurant:
            def __init__(self, name, type):
                self.restaurant_name = name
                self.cuisine_type = type
            def describe(self):
                print(f"Название ресторана: {self.restaurant_name}")
                print(f"Тип кухни: {self.cuisine_type}")
            def open(self):
                print(f"Ресторан '{self.restaurant_name}' открыт!")


        class IceCreamStand(Restaurant):
            def __init__(self, name, location, working_hours):
                super().__init__(name, type='мороженное')
                self.location = location
                self.working_hours = working_hours
                self.flavours = []
                self.types = {
                    'стаканчик':[],
                    'на палочке':[],
                    'брикет':[]
                }

            def worked(self):
                print(f'Кафе: {self.restaurant_name}')
                print(f'Местоположение ресторана: {self.location}')
                print(f'Время работы: {self.working_hours}')
                print(' ')

            def add_list(self, write):
                if write not in self.flavours:
                    self.flavours.append(write)
                    print('сорт добавлен')
                else:
                    print('такой сорт уже есть')
            def delete_list(self, write):
                if write in self.flavours:
                    self.flavours.remove(write)
                    print('сорт удалён')
                else:
                    print('такого сорта нет')
            def menu(self):
                print("\nМеню мороженнного:")
                for i in self.flavours:
                    print(i)
                print(' ')


            def check(self, a):
                b = a.lower()
                if b not in self.flavours:
                    print('такого сора нету')
                    print(' ')
                else:
                    print('сорт в наличии')
                    print(' ')


            def type_icecream(self, type, Flavour):
                if type in self.types:
                    self.types[type] = Flavour
                    print('список типа обновлён')
                else:
                    print('такой тип отсутствует')
            def typing_types(self):
                print('\nДоступный тип мороженного: ')
                for i in self.types:
                    a = [j for j in self.types[i]]
                    print(i, '-', ', '.join(a) if a else 'сорт отсутствует')
                print(' ')


        # создание данных для класса
        x = IceCreamStand('Киоск с мороженным', 'улица 143, ТЦ север', '10;00 - 20;00')

        #создание списка
        x.worked()
        x.add_list('ванильное')
        x.add_list('фесташковое')
        x.add_list('клубничное')
        x.add_list('пломбир')
        x.add_list('шоколадное')

        #удаление и проверка наличия сорта
        x.menu()
        x.delete_list('шоколадное')
        x.delete_list('123')
        x.menu()

        #проверка наличия сорта
        y = input('Введите название мороженного - ')
        x.check(y)

        #добавление типов и проверка списка
        x.type_icecream('брикет',['шоколадное','клубничное'])
        x.type_icecream('на палочке',['пломбир','фесташковое'])
        x.typing_types()

    if a == 3:
        #3
        import tkinter

        class IceCreamStand:
            def __init__(self, name):
                self.restaurant = name
                name.title('Кафе с мороженным')

                self.label = tkinter.Label(name, text="Киоск с мороженным", font=40)
                self.label.pack()

                self.btn = tkinter.Button(name, text=('Список мороженного'), command = self.Flavour)
                self.btn.pack()

                self.text_tap = tkinter.Text(name, height=15,width=30)
                self.text_tap.pack()

            def Flavour(self):
                y = ['ванильный','мятный','шоколадный','ассорти','фруктовый лёд']
                self.text_tap.insert(tkinter.END, '     Сорта мороженного:\n')
                for i in y:
                    self.text_tap.insert(tkinter.END, f'{i}\n')



        root = tkinter.Tk()
        root.geometry('300x300')
        root.config(bg='blue')
        x = IceCreamStand(root)
        root.resizable(width=False, height=False)
        root.mainloop()

while True:
    x = int(input('     Введите номер задания: '))
    if x == 0:
        break
    else:
        num_tusk(x)

