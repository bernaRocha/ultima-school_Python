'''
Faça um programa, com uma função que necessite de três argumentos, 
e que forneça a soma desses três argumentos. 
'''

from os import system
system('clear')

def soma_tres(numero_1, numero_2, numero_3):
    
    resultado = numero_1 + numero_2 + numero_3
    
    print(f'A soma de {numero_1} + {numero_2} + {numero_3} = {resultado}')

soma_tres(3, 6, 9)