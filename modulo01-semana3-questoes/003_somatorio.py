'''
3. Crie uma função de somatório que some todos os números que a mesma receber (usando *args ).
'''
from os import system
system('clear')

def somatorio(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    return f'O somatório deu {resultado}' 

print(somatorio(1, 2, 3, 4, 5, 6, 7)) # O somatório deu 28
