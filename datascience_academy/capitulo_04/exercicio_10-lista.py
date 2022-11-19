from os import system   
system('clear')

# Exercício 10 - Considere a lista abaixo 
# e retorne apenas os elementos cujo índice for maior que 5.
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for i, valor in enumerate(lista):
    if i > 5:
        print(valor, end=" ")
