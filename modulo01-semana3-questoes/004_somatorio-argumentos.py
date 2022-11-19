'''
4. Crie um programa com uma função que necessite de três argumentos, 
e que forneça a soma desses três argumentos.
'''
from os import system
system('clear')

def soma_tres(argumento1, argumento2, argumento3):
    somatorio = argumento1 + argumento2 + argumento3
    return somatorio

print(f'A soma dos três argumentos é: {soma_tres(1, 3, 5)}') # 9
print(f'A soma dos três argumentos é: {soma_tres(9, 23, 67)}') # 99
