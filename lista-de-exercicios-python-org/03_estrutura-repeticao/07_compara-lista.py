'''
Faça um programa que leia 5 números e informe o maior número. 
'''
from os import system
system('clear')

numeros = []

for numero in range(0, 5):
    numeros.append(int(input(f'Registre um número na posição {numero + 1}: ')))

print(f'Os números registrados são {numeros}')

numeros.sort()
maior_numero = numeros[-1]

print(f'Em ordem numérica fica: {numeros}')
print(f'O maior número dentre eles é {maior_numero}')
