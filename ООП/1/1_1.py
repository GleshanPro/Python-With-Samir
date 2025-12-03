class Pokemon:
    def __init__(self):
        self.a = 12

class Area:
    _obj = None # вне init - статические поля. Принадлежат классу.
    # _ - пожалуйста, не обращайтесь к этому полю нигде, кроме методов класса или ... к которому принадлежит этот класс
    # cls - класс под который нужно выделить память, который нужно создать. Тут в него передаётся Area
    # в Python всё есть соглашение. Можно self назвать по-другому
    def __new__(cls, *args, **kwargs): # new - поставщик ссылки на self (выделяет на него память)
        print(cls)
        if Area._obj is None:
            Area._obj = Pokemon()
            return Area._obj
        else:
            return Area._obj
    """
    new

    Выделяем память на объект
    ->
    Возвращаем ссылку -> она попадает в init(self)
    """

    def __init__(self):
        self.x = 10

ar = Area()

print(type(ar))


a2 = Area()

print(id(a2), id(ar)) # вызвали конструктор два раза - instance остался один

# print(dir(ar.x)) # не работает, хотя в self его назначали.  'Pokemon' object has no attribute 'x'