# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`)
#    и методы (`make_sound()`, `eat()`) для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных
#   и вызывает метод `make_sound()` для каждого животного.
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы
# (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).
#
# Дополнительно:
# Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации о зоопарке в файл
# и возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.
import pickle

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, Возраст: {self.age}"

    def make_sound(self):
        pass

    def eat(self):
        print("ест корм")

class Bird(Animal):
    def make_sound(self):
        print("ку-ку")

class Mammal(Animal):
    def make_sound(self):
        print("беее-е-е")

class Reptile(Animal):
    def make_sound(self):
        print("шипит")

class Worker:
    def __init__(self, name, phone, position):
        self.name = name
        self.phone = phone
        self.position = position

    def __str__(self):
        return f"{self.name}, тел: {self.phone}, должность: {self.position}"

class ZooKeeper(Worker):
    def feed_animal(self):
        print(f"{self.name} кормит животное")

class Veterinarian(Worker):
    def heal_animal(self):
        print(f"{self.name} лечит животное")

class Zoo:
    def __init__(self, country, city):
        self.country = country
        self.city = city
        self.workers = []
        self.animals = []

    def add_worker(self, name, phone, position):
        position_lower = position.lower()
        if position_lower == "veterinarian":
            new_worker = Veterinarian(name, phone, position)
        elif position_lower == "zookeeper":
            new_worker = ZooKeeper(name, phone, position)
        else:
            raise ValueError("Недопустимая должность работника")
        self.workers.append(new_worker)
        print(f"Добавлен работник: {new_worker}")

    def add_animal(self, name, age, animal_type):
        animal_type = animal_type.lower()
        if animal_type == "bird":
            new_animal = Bird(name, age)
        elif animal_type == "mammal":
            new_animal = Mammal(name, age)
        elif animal_type == "reptile":
            new_animal = Reptile(name, age)
        else:
            raise ValueError(f"Неизвестный тип животного: {animal_type}")
        self.animals.append(new_animal)
        print(f"Добавлено животное: {new_animal}")

    def __str__(self):
        workers_str = '\n'.join(str(worker) for worker in self.workers)
        animals_str = '\n'.join(str(animal) for animal in self.animals)
        return (f"Зоопарк: {self.country}, {self.city}\n"
                f"Работники:\n{workers_str}\n"
                f"Животные:\n{animals_str}")

    def save_to_file(self, filename):
        """Сохраняет объект зоопарка в файл"""
        with open(filename, 'wb') as f:
            pickle.dump(self, f)
        print(f"Зоопарк сохранён в файл {filename}")

    @staticmethod
    def load_from_file(filename):
        """Загружает объект зоопарка из файла"""
        with open(filename, 'rb') as f:
            zoo = pickle.load(f)
        print(f"Зоопарк загружен из файла {filename}")
        return zoo

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

# Пример использования
zoo1 = Zoo("Россия", "Москва")

zoo1.add_worker("Коля", "666666", "Veterinarian")
zoo1.add_worker("Паша", "777777", "ZooKeeper")

zoo1.add_animal("Орел", 5, "Bird")
zoo1.add_animal("Баран", 8, "Mammal")
zoo1.add_animal("Змея", 16, "Reptile")

# Демонстрация полиморфизма
print("\nЗвуки животных:")
animal_sound(zoo1.animals)

# Демонстрация методов работников
print("\nРаботники выполняют свои обязанности:")
for worker in zoo1.workers:
    if isinstance(worker, Veterinarian):
        worker.heal_animal()
    elif isinstance(worker, ZooKeeper):
        worker.feed_animal()

print("\nИнформация о зоопарке:")
print(zoo1)


# Сохранение зоопарка
zoo1.save_to_file('my_zoo.pkl')

# Загрузка зоопарка
loaded_zoo = Zoo.load_from_file('my_zoo.pkl')

print("\nЗагруженный зоопарк:")
print(loaded_zoo)

# Проверка работоспособности методов
print("\nПроверка методов загруженного зоопарка:")
loaded_zoo.workers[0].heal_animal()
loaded_zoo.animals[0].make_sound()