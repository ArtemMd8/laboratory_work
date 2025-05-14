#1

class Restaurant:
    """Класс для описания ресторана"""

    def __init__(self, restaurant_name, cuisine_type):
        """Инициализирует атрибуты названия ресторана и типа кухни"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Выводит информацию о ресторане"""
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")

    def open_restaurant(self):
        """Выводит сообщение об открытии ресторана"""
        print(f"Ресторан '{self.restaurant_name}' открыт!")

# Создание экземпляра класса
newRestaurant = Restaurant("Гастрономик", "французская")

# Вывод атрибутов по отдельности
print(newRestaurant.restaurant_name)
print(newRestaurant.cuisine_type)

# Вызов методов
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()