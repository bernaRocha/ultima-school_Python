'''
Faça um Programa que verifique se uma letra digitada é vogal ou consoante. 
'''
from os import system
system('clear')

letra = input('Digite uma letra: ').strip().lower()

if letra[0] in 'aeiou':
    print(f'A letra digitada [ {letra[0]} ] é uma vogal')
else:
    print(f'A letra digitada [ {letra[0]} ] é uma consoante')
    