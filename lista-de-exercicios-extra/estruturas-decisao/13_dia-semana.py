'''
Faça um Programa que leia um número e exiba o dia correspondente da semana. 
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido. 
'''
from os import system
system('clear')

dias_semana = 'Domingo Segunda Terça Quarta Quinta Sexta Sábado'.split()

dia = input('Que dia da semana é hoje? [1] - Dom, [2] - Seg ...: ')

if dia == '1':
    print(f'Hoje é {dias_semana[0]}')
elif dia == '2':
    print(f'Hoje é {dias_semana[1]}')
elif dia == '3':
    print(f'Hoje é {dias_semana[2]}')
elif dia == '4':
    print(f'Hoje é {dias_semana[3]}')
elif dia == '5':
    print(f'Hoje é {dias_semana[4]}')
elif dia == '6':
    print(f'Hoje é {dias_semana[5]}')
elif dia == '7':
    print(f'Hoje é {dias_semana[6]}')
else:
    print('Valor inválido')
    