'''
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os. 
'''
from os import system
system('clear')

comeco = int(input('Começo do vetor: '))
fim = comeco + 5

for i in range(comeco, fim):
    print(i, end= " ")
print("FIM")
