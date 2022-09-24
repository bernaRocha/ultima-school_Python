'''
Faça um Programa que leia três números e mostre-os em ordem decrescente. 
'''
from os import system
system('clear')

numeros = []

while True:
    numero = int(input('Registre um número: '))
    numeros.append(numero)

    if len(numeros) == 3:
        break

numeros.sort(reverse=True)
print('Os números registrados em ordem decrescente ficam: ')
for numero in numeros:
    print(numero, end=' -> ')
print(' FIM da sequência')
