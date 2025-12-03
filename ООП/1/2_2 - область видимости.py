x = "global"

def outer():
    x = "enclosing"
    def inner():
        nonlocal x # x для inner - нелокальная. Он где-то выше. В другом уровне вложенности (на 1 уровень )
        # ТОЛЬКО НА ОДИН УРОВЕНЬ ВЛОЖЕННОСТИ ВЫШЕ! на два не сработает.
        x = "changed in inner"
        return x
    inner()

# без nonlocal - enclosing
print(outer()) # changed in inner
print(x)       # global