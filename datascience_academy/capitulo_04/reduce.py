from functools import reduce
from os import system
system('clear')

lista = [5, 78, 23, 41]

def soma(a, b):
    x = a + b
    return x

print(reduce(soma, lista)) # 147

lst = [5, 8, 3, 5, 90]

print(reduce(lambda x, y: x + y, lst)) # 111

maior = lambda a, b: a if (a > b) else b
print(maior)              # <function <lambda> at 0x7fb1ee7551f0>
print(str(maior))         # <function <lambda> at 0x7f2e6f0351f0>
print(reduce(maior, lst)) # 90
