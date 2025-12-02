# * и ** можно называть как-угодно:
def proizvol(*lists, **dicts):
    ...

def f(*args, **kwargs):
    ...



def pair_sum(x, y): return x + y

t = (3, 5)

d = {
    "y": 10, "x": 7
}

print(pair_sum(*t))
print(pair_sum(**d)) # РАСПАКОВКА СЛОВАРЯ