'''
Faça um programa que leia 5 números e informe a soma e a média dos números. 
'''
from os import system
system('clear')

numeros = []

for i in range(0, 5):
    numeros.append(int(input(f'Registre um número na posição {i + 1}: ')))

somatorio = sum(numeros)
media = somatorio / (len(numeros))

print(f'Os números registrados são: {numeros}\n'
f'O somatório deles é {somatorio}\n'
f'A média desses valores é {media}')
