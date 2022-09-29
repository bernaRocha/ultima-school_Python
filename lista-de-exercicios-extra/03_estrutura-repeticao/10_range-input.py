'''
Faça um programa que receba dois números inteiros e gere os números inteiros 
que estão no intervalo compreendido por eles. 
'''
from os import system
system('clear')

comeco = int(input('Número do começo da lista: '))
fim = int(input('Número do fim da lista: '))

for i in range(comeco, fim + 1):
    print(f'{i} - ', end=' ')
    
print("FIM")
