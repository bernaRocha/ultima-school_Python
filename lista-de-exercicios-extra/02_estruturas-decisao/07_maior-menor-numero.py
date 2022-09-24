'''
Faça um Programa que leia três números e mostre o maior e o menor deles. 
'''
from os import system
system('clear')

numeros = []

while True:
    numero = int(input('Registre um número: '))
    numeros.append(numero)

    if len(numeros) == 3:
        break

em_ordem = numeros.sort()
maior_numero = numeros[-1]
menor_numero = numeros[0]

print(f'O maior número é o {maior_numero}\n'
f'O menor número é o {menor_numero}\n'
f'Números registrados: {numeros}')
