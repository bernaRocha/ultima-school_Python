from os import system   
system('clear')

# Exercício 7 - Usando a função filter(), encontre os valores que são comuns às duas listas abaixo.
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]

print(f'Comuns na lista A e B: {list(filter(lambda x: x in a, b))}')