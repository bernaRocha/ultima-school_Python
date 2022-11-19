'''
6. Crie uma função que permita contar o número de vezes que aparece uma letra em uma string.
'''
from os import system
system('clear')

def conta_caractere():
    frase = input('Digite a frase a ser analisada: ').strip().lower()
    letra = input('qual letra deseja contar suas repetições? ')
    contador = frase.count(letra.lower())
    print(f'Na frase "{frase}" a letra {letra} aparece {contador} vezes.')
    
conta_caractere()
