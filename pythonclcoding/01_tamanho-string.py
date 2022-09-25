'''
Registre a frase para o cálculo do tamanho: olá mundo
o | l | á |   | m | u | n | d | o
=================
0 1 2 3 4 5 6 7 8
'''

from os import system
system('clear')

frase = input('Registre a frase para o cálculo do tamanho: ')
tamanho = len(frase)
print(*frase, sep=' | ')
print('=' *(tamanho*2 - 1))
print(*range(tamanho))
