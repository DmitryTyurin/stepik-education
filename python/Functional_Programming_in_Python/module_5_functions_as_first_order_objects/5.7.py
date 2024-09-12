# Напишите функцию apply, которая принимает функцию и итерируемый объект (например, список) и применяет функцию к каждому элементу итерируемого объекта.
# В качестве ответа функция apply должна вернуть список из вычисленных значений.


def apply(func, iterable):
    return [func(x) for x in iterable]


# Затем создайте функцию compute, которая принимает список функций и произвольное количество значений.
# Функция compute должна применить каждую функцию к каждому значению в переданном порядке и сформировать из полученных значений новый список, который и будет возвращаться в качестве ответа

compute = lambda func, *args: [x(y) for x in func for y in args]


# Затем создайте функцию compute, которая принимает список функций и произвольное количество значений. Функция compute должна применить все функции сразу к каждому значению в переданном порядке и сформировать из полученных значений новый список, который и будет возвращаться в качестве ответа
def compute(functions, *values):
    results = []

    for value in values:
        result = value
        for func in functions:
            result = func(result)
        results.append(result)

    return results


# Напишите функцию filter_list, которая принимает функцию f и список lst.
# Функция f обязательно должна проверять определенное условие и возвращать булев тип.
# Задача функции filter_list состоит в том, чтобы вернуть новый список, составленный из элементов входного lst, отфильтрованных согласно функции f.

filter_list = lambda f, lst: [x for x in lst if f(x)]

# На основании предыдущей функции filter_list, напишем новую функцию filter_collection. Особенность функции filter_collection заключается в том, что она возвращает тот же тип коллекции, который она принимала на вход.
# А остальной принцип  ее работы похож с функцией filter_list: обе принимают функцию f для проверки, при помощи которой фильтруются элементы коллекции
# Функция f обязательно должна проверять определенное условие и возвращать булев тип.


def filter_collection(func, numbers):
    if isinstance(numbers, tuple):
        return tuple(x for x in numbers if func(x))
    elif isinstance(numbers, list):
        return [x for x in numbers if func(x)]
    else:
        return "".join([x for x in numbers if func(x)])

# Реализуйте функцию aggregation, которая принимает на вход функцию func и коллекцию элементов sequence.
# Функция func будет принимать только два элемента.
# Задача функции aggregation уметь накапливать результат вычисления функции func путем последовательного применения ее ко всем элементам. Но так как функция func умеет работать только с двумя значениями, вам необходимо передавать элементы последовательно парами. В результате у вас должен получится список, в котором копятся результаты работы функции aggregation
# Пример, в качестве func возьмем функцию
# def get_add(x, y):
#     return x + y
# Коллекцией у нас будет следующий список
# numbers = [5, 2, 4, 3, 5]
# Применяя func к первым элементам коллекции 5 и 2, получим сумму 7. Это первое наше агрегированное значение
# Далее берем уже накопленное значение 7 и следующий необработанный элемент 4, суммируем и получаем новую агрегацию 11.
# Затем суммируем нашу агрегацию 11 со значением 3, получаем 14. И в конце добавляем последний элемент и готово итоговое значение 19. В итоге в процессе применения функции func мы нашли следующие значения [7, 11, 14, 19]. Данный список и нужно будет вернуть в качестве ответа.
