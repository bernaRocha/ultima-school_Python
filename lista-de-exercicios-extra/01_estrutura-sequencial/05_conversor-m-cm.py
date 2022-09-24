'''
Faça um Programa que converta metros para centímetros. 
1 metro = 100 centímetros
'''

from os import system
system('clear')

metros = float(input('Diga o valor em metros a ser convertido para cm: '))
centimetros = metros * 100
print(f'{metros} m equivalem a {centimetros:.2f} cm')
