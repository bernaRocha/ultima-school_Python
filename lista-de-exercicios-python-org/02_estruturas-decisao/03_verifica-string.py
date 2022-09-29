'''
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: 
F - Feminino, M - Masculino, Sexo Inválido. 
'''
from os import system
system('clear')

sexo = input('qual seu sexo? [M/F] ').strip().upper()

if sexo in 'M':
    print('M - Masculino')
elif sexo in 'F':
    print('F - Feminino')
else:
    print('Sexo Inválido.')
