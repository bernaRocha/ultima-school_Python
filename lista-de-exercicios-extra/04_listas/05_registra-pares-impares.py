'''
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
Imprima os três vetores. 
'''
from os import system
system('clear')

numeros = []
pares = []
impares = []

for i in range(0, 20):
    numero = int(input(f'Registre um número na posição {i + 1}: '))
    numeros.append(numero)

    if numero % 2 ==0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f'Os números registrados são: {numeros}\n'
f'Os pares são: {pares}\n'
f'Os ímpares são: {impares}')
