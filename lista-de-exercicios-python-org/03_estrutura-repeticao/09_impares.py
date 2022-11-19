'''
Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50. 
'''
from os import system
system('clear')

for i in range(0, 51):
    if i % 2 != 0:
        print(i, end=' - ')
print('FIM')  
      