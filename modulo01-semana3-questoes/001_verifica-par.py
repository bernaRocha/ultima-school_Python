'''
1. Crie uma função que, ao receber um número inteiro, 
retorna se um número  é par ou ímpar (utilizando **kwargs).
'''
from os import system
system('clear')

def verifica_par_impar(numero, divisor=2):
    if numero // divisor == 0:
        return f'O número {numero} não é par'
    else:
        return f'O número {numero} é par'

print(verifica_par_impar(6))
    