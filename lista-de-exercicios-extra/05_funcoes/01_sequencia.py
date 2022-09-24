'''
Faça um programa para imprimir:

        1
        2   2
        3   3   3
        .....
        n   n   n   n   n   n  ... n
'''
from os import system
system('clear')

def sequencia(n):
    if type(n) == int:
       for i in range(n):
        i += 1
        print(str(i) * i)

print(sequencia(5))