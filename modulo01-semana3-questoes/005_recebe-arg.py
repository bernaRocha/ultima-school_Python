'''
5. Faça um programa com uma função que necessite de um argumento. 
A função deve retornar o valor de caractere 'P', se seu argumento for positivo, 
e 'N', se seu argumento for zero ou negativo.
'''
from os import system
system('clear')

def retorna_resposta(numero):
    if numero > 0:
        return ascii('P')
    elif numero == 0 or numero < 0:
        return ascii('N')
    else:
        print('Inválido')
        
print(retorna_resposta(99)) #'P'
print(retorna_resposta(0)) # 'N'
print(retorna_resposta(-9)) # 'N'
