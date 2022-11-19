'''
Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. 
'''
from os import system
system('clear')

nota = float(input('Registre uma nota (0.0 - 10.0): '))
nota_valida = 0 <= nota <= 10

while not nota_valida:
    print('Número inválido, tente novamente.')
    nota = float(input('Registre uma nota (0-10.0): '))

print(f'A nota registrada foi {nota:.2f}')
