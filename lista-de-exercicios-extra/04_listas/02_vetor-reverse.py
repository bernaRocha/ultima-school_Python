'''
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa. 
'''
from os import system
system('clear')

lista = []

comeco = int(input('Começo do vetor: '))
fim = comeco + 10

for i in range(comeco, fim):
    lista.append(i)

lista.reverse()
print(lista, end=" ")

# i = invert(i) #### inverte o sinal dos números
