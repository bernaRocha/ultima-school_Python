''' 
Faça um Programa que peça dois números e imprima o maior deles. 
'''
from os import system
system('clear')

numeros = []
for c in range(0, 2):
    numeros.append(int(input('Digite um número: ')))

if numeros[0] > numeros[1]:
    print(f'Entre os números {numeros[0]} e {numeros[1]}, o número maior é o {numeros[0]}')
else:
    print(f'Entre os números {numeros[0]} e {numeros[1]}, o número maior é o {numeros[1]}')
