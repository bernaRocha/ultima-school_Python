from os import system
from ssl import VerifyFlags
system('clear')

# filter(funcao, sequencia)

def verificaPar(num):
    if num % 2 == 0:
        return True
    else:
        return False

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(filter(verificaPar, lista))           # <filter object at 0x7f31aa8e8160>
print(list(filter(verificaPar, lista)))     # [0, 2, 4, 6, 8, 10]

print('Com lambda: ', end='')
print(list(filter(lambda x: x % 2== 0, lista))) # Com lambda: [0, 2, 4, 6, 8, 10]

print('Com lambda, maiores que 8: ', end='')
print(list(filter(lambda x: x > 8, lista)))     # Com lambda, maiores que 8: [9, 10]
