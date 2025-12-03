from __future__ import annotations
from time import sleep

class Goose:
    hp: int = 10
    name: str = "Goose"
    calculator: int = 100
    
    
    def __init__(self, name: str, hp: int):
        self.name = name
        self.hp = hp
        
    def __setattr__(self, key, value):
        (super).__setattr__(self, key, value)
        
    def __getattr__(self, name):
        (super).__getattribute__(self, name)
        
    # Аннотация - можно делать так.
    # Python 3.14+ -> можно без кавычек (from __future__ import annotations)
    # Кавычками указываем, что объект не до конца инициализирован, но имеет такие-то поля
    def honk(self: "Goose"): # -> Меня может вызвать только объект, которому я принадлежу
        print(f"{self.name} honks with volume {self.hp}!")
    
    @staticmethod
    def calculate():
        print(10)
    
    
    @staticmethod   
    def create(name: str, hp: int) -> Goose:    # Фабричный метод. Зачем передавать
                                                # экземпляр?
                                                # Статичного метода достаточно
        # sleep(5)    # М.б. длительные операции
        return Goose(name, hp)
    
    @classmethod # больше про Generic-фабрику
    def create_class(cls, name: str) -> "Goose":
        print(cls.__name__)
        return cls(name, 100)
        # return Goose(name, 100)
    

"""
def honk(self) - под капотом Python подсовывает в первый аргумент объект
""" 

"""
def __init__ - Конструктор делать легковесным
Тяжёлые операции вынести в статичный метод - def create
    там можно "спарсить файл, открыть файл, проверить файл на существование,
    сгенерировать объект и вернуть его"
"""

goose = Goose.create(name="ABC", hp=100)


class TemkaGoose(Goose):
    ...
    
goose1 = TemkaGoose.create_class(name="TEST")

TemkaGoose.calculate()

    
# goose = Goose("Arnold", 20)
# print(goose.name, goose.hp)
# print(id(goose.name), id(goose.hp))

# goose.name = "Privet"
# print(goose.name, goose.hp)
# print(id(goose.name), id(goose.hp))


# defaultGoose = Goose()
# print(defaultGoose.name, defaultGoose.hp)


