'''
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo. 
'''
from os import system
system('clear')

numero = int(input('Registre um número: '))

NUMERO_POSITIVO = numero >= 0
NUMERO_NEGATIVO = numero < 0

print(f'O número {numero} é positivo.' if NUMERO_POSITIVO else f'O número {numero} é negativo.')
