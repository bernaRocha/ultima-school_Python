'''
Faça um Programa que peça dois números e imprima a soma. 
'''
from os import system
system('clear')

numero_1 = int(input('Informe um número: '))
numero_2 = int(input('Informe outro número: '))
somatorio = numero_1 + numero_2

print(f'A soma de {numero_1} + {numero_2} é igual a: {somatorio}')
