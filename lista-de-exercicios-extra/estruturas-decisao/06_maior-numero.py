'''
Faça um Programa que leia três números e mostre o maior deles. 
'''
from os import system
system('clear')

numeros = []
while True:
    
    numero = int(input('Registre um número: '))
    numeros.append(numero)

    if len(numeros) == 3:
        break

maior_numero = numeros.sort() #### coloca a lista em ordem

print(f'O maior número é o {numeros[-1]}') #### o maior é o último da lista
