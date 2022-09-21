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

em_ordem = numeros.sort() #### coloca a lista em ordem
maior_numero = numeros[-1]

print(f'O maior número é o {maior_numero}') #### o maior é o último da lista
