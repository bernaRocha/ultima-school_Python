'''
Faça um programa para imprimir:

        1
        1   2
        1   2   3
        .....
        1   2   3   ...  n
'''

from os import system
system('clear')

def print_n_times(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end='  ')
        print(' ')

print_n_times(5)