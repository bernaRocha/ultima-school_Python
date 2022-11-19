'''
1. Crie uma função que, ao receber um número inteiro, 
retorna se um número  é par ou ímpar (utilizando **kwargs).
'''
from os import system
system('clear')

def verifica_par_impar(numero):
    if numero % 2 == 0:
        return f'O número {numero} é par'
    else:
        return f'O número {numero} não é par'

print(verifica_par_impar(8)) # O número 8 é par
print(verifica_par_impar(9)) # O número 9 não é par
    