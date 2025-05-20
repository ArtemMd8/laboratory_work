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

        # Создание экземпляра класса
        x = Restaurant("китайский", "китайский")

        print(x.restaurant_name)
        print(x.cuisine_type)

        x.describe()
        x.open()

    if a == 2:
        #2
        class Restaurant1:
            def __init__(self, name, type):
                self.restaurant_name = name
                self.cuisine_type = type
            def describe(self):
                print(f"Название ресторана: {self.restaurant_name}")
                print(f"Тип кухни: {self.cuisine_type}")
            def open(self):
                print(f"Ресторан '{self.restaurant_name}' закрыт")

        class Restaurant2:
            def __init__(self, name, type):
                self.restaurant_name = name
                self.cuisine_type = type
            def describe(self):
                print(f"Название ресторана: {self.restaurant_name}")
                print(f"Тип кухни: {self.cuisine_type}")
            def open(self):
                print(f"Ресторан '{self.restaurant_name}' открыт!")

        class Restaurant3:
            def __init__(self, name, type):
                self.restaurant_name = name
                self.cuisine_type = type
            def describe(self):
                print(f"Название ресторана: {self.restaurant_name}")
                print(f"Тип кухни: {self.cuisine_type}")
            def open(self):
                print(f"Ресторан '{self.restaurant_name}' открыт!")

        class Restaurant4:
            def __init__(self, name, type):
                self.restaurant_name = name
                self.cuisine_type = type
            def describe(self):
                print(f"Название ресторана: {self.restaurant_name}")
                print(f"Тип кухни: {self.cuisine_type}")
            def open(self):
                print(f"Ресторан '{self.restaurant_name}' закрыт")


        # Создание класса
        x1 = Restaurant1("французский", "французский")
        x2 = Restaurant2("испанский", "испанский")
        x3 = Restaurant3("швейцарский", "швейцарский")
        x4 = Restaurant4("корейский", "корейский")

        x1.describe()
        x2.describe()
        x3.describe()
        x4.describe()

    if a == 3:
        #3
        class Restaurant:
            def __init__(self, name, type, rating):
                self.restaurant_name = name
                self.cuisine_type = type
                self.restaurant_rating = rating

            def describe(self):
                print(f"Название ресторана: {self.restaurant_name}")
                print(f"Тип кухни: {self.cuisine_type}")
                print(f"Рейтинг ресторана : {self.restaurant_rating}")

            def open(self):
                print(f"Ресторан '{self.restaurant_name}' открыт!")

            def rating_start(self, Nrating):
                self.restaurant_rating = Nrating
                print(f"Рейтинг изменён на {self.restaurant_rating} звёзд")

        # Создание класса
        x = Restaurant("китайский", "китайский", 2.5)

        x.describe()
        y = int(input('Введите рейтинг ресторана - '))
        x.rating_start(y)


while True:
    x = int(input('     Введите номер задания: '))
    if x == 0:
        break
    else:
        num_tusk(x)