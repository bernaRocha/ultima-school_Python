'''
Faça um Programa que leia um vetor de 10 caracteres, 
e diga quantas consoantes foram lidas. Imprima as consoantes. 
'''
from os import system
system('clear')

lista_caracteres = []
total_consoantes = 0

for caractere in range(0, 10):
    caractere = input('Registre um caractere: ').lower()[0]
    lista_caracteres.append(caractere)

    if caractere not in 'aeiou':
        total_consoantes += 1
        
print(f'Você registrou os seguintes caracteres: {lista_caracteres}')
print(f'O total de consoantes é: {total_consoantes}')
