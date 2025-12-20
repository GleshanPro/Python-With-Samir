"""
1. is VS ==
- Оператор is сравнивает идентичность объектов (один и тот же объект), а == - их логическое равенство, определённое методом eq.
(но в опр ситуациях они ведут себя одинаково)

2. Что будет выведено?
- 15
"""
def multiply(factor): # На сам деле - фабричный метод по генерации декоратора
    def decorator(func):
        def wrapper(x):
            return func(x) * factor
        return wrapper
    return decorator

@multiply(3)
def identity(x):
    return x
print(identity(5))

# Мы не можем кастомизировать функцию декоратором. Как тут умножаем 5 на 3