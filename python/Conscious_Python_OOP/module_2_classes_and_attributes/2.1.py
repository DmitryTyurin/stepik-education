# Создайте класс Car.
# Объявите (создайте) атрибут color внутри класса, со значением "blue"
# Выведите на экран значение атрибута color с помощью print()


class Car:
    color = "blue"


print(Car.color)


# Создайте класс Person
# Объявите внутри класса два атрибута: name, time, со значениями "Vasya" и 2, соответственно.
# Выведите на экран сообщение, используя знания об атрибутах и f-строку. Подставьте значения атрибутов в f-строке.
# Само сообщение выглядит так: Теперь Vasya может программировать 2 часа без перерыва


class Person:
    name = "Vasya"
    time = 2


print(f"Теперь {Person.name} может программировать {Person.time} часа без перерыва")


# Создайте класс Number и два атрибута: num1 и num2, со значениями 5 и 10 соответственно.
# Выведите на экран сумму значений этих атрибутов, используя обращения к атрибутам через точку.


class Number:
    num1 = 5
    num2 = 10


print(Number.num1 + Number.num2)

# Создайте класс Backpack и атрибут things внутри класса.
# Значение атрибута things будет список ["хомяк", "капустка", "фонарик", "шапка Пикачу", "игрушечный меч майнкрафт"].
# Используя цикл for по атрибуту things, выведите на экран все элементы входящие в атрибут, каждый на отдельной строке (см. пример ниже)
# Не забывайте правильно обратиться к атрибуту класса в цикле.


class Backpack:
    things = [
        "хомяк",
        "капустка",
        "фонарик",
        "шапка Пикачу",
        "игрушечный меч майнкрафт",
    ]


for thing in Backpack.things:
    print(thing)
