from itertools import zip_longest;

"""
Словарь - изменяемый

"""

d = {'a': 42, 'b': 57}
# вывод: {'a': 42, 'b': 57}
d.keys() # - не список, а генератор
# dict_keys(['a', 'b'])

# двоякая история иметь в памяти все ключи, если их много
# так или иначе мы итерируемся => нет смысла выделять всё сразу

list(d.keys())
# ['a', 'b']

d.items() # пары ключ-значение


"""
True == 1 - True
1.0 == 1 - True

"""

d = {1.0: "abc", True: 0.5, 1: "RULETKA"}
# только один ключ: 1.0: "RULETKA"
# пошагово:
"""
d[1.0] = "abc"
d[True] = 0.5 (~ d[1.0] = 0.5)
d[1] = "RULETKA" (~ d[1.0] = "RULETKA")

итого: ключ от первого совпадения, значение - от последнего
надо быть аккуратным, если дублируются ключи.

{**d}
"""

# zip
zip([1,2,7],[7,2,7],["Ya", 0, 7])
# print(zip([[1,2,7],[7,2,7],["Ya", 0, 7]]))
# <zip object at 0x7fcd5d8a7600>

# for item in zip([1,2,7],[7,2,7],["Ya", 0, 7]):
    # print(item)

# print(list(zip([1,2,3], [4,5,6])))

# for item in zip([2,7],[7,2,7],["Ya", 0, 7]):
#     print(item)
# for item in zip([2,7,3],[7,2,7],["Ya", 0]):
#     print(item)

# for item in zip_longest([2,7,3],[7,2,7],["Ya", 0]):
#     print(item) # 3, 7, None


# d = {1:2, 3:4}
# d = {item1: item2 for item1 in range(10) for item2 in range(20)}
# print(d)

# d = {}
# for i in range(10):
#     for j in range(20):
#         print(d)
#         d[i] = j
#         print(d)

# d = dict((item, item) for item in range(10))
# print(d)

# d[None] = 123 # - МОЖНО (самый полезный ключ)
# print(d)

grades = [('a', 10), ('b', 20), ('c', 30), ('a', "jeckpot")]

scores = {}

for student, grade in grades:
    scores.setdefault(student, []).append(grade)
    # если ключа в словаре нет, он его ставит
    """
    то же самое:

    if student not in scores:
        scores[student] = []
    scores[student].append(grade)
    """
    

# print(scores)

# с Python 3.7 словари сохраняют порядок вставки
# под капотом словаря - хэш таблица. Теперь она сохраняет порядок))?!
# теперь индекс соответсвует хэшу. Получается теперь массив внутри хэш-таблицы

# хэш-функции