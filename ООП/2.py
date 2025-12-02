# def(...) ... - сигнатура

"""
Виды парметров в Python:

1. Позиционные-только

"""

def demo_params(a, b = 10, /, c = 20, *args, d, e=50, **kwargs):
    """
    Пример смешанной сигнатуры.
    a, b - позиционные-только (из-за '/')
    c - позиционный или ключевой
    *args - дополнительные позиционные
    d, e - ключевые-только (из-за '*')
    **kwargs - дополнительные ключевые
    """
    return {
        "a": a, "b": b, "c": c, "d": d, "e": e, "kwargs": kwargs
    }


print(demo_params.__defaults__) # - не выведет e=50, ибо после *?


def casino_royal(a: int, b: float) -> str:
    ...

# casino_royal(1, 2)
# casino_royal(b = 2, a = 1)

# Нужен порядок?

def casino_royal(a: int, b: float, /) -> str:
    ...

# *args - ТОЛЬКО после Позиционные-только или Позиционные-или-ключевые
def casino_royal(a: int, b: float, *args) -> str: # всё, что после 1 и 2 параметра объедини и выведи мне
    print(args)
    return "hello"

casino_royal(1, 2, 123, 12, 890) # кортеж (123, 12, 890)

# * - "больше позиционных параметров нет. Дальше только ключевые(именованные)"
def casino_royal1(a: int, b: float, *, f, g) -> str:
    print(a, b, f, g)
    return "hello"

# casino_royal1(1, 2, 123, 12) - не даст
casino_royal1(1, 2, g = 10, f = 20)

# **kwargs - в отличие от позиционного *args передаются и КЛЮЧИ и ЗНАЧЕНИЯ - создаётся СЛОВАРЬ
def casino_royal2(a: int, b: float, *args, f, g, **kwargs) -> str:
    print(args)
    print(kwargs)
    return "hello"

casino_royal2(1, 2, f = 123, g =567, h = 123, d = 777)          # без *args
casino_royal2(1, 2, 1, 2, 3, f = 123, g =567, h = 123, d = 777) # с *args

