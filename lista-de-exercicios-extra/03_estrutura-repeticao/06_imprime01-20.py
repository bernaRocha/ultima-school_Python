'''
Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
Depois modifique o programa para que ele mostre os números um ao lado do outro. 
'''
from os import system
system('clear')

for i in range(0, 21):
    print(i)

for i in range(0, 21):
    print(i, end=' ')
    