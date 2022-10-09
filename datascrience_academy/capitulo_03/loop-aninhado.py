import imp
from os import system
system('clear')

for i in range(0, 5):
    for a in range(6, 10):
        print(a, end=' ')
# 6 7 8 9 6 7 8 9 6 7 8 9 6 7 8 9 6 7 8 9
print()
print()

listaB = [32, 54, 56, 12, 91, 18]
soma = 0
for i in listaB:
    double_i = i * 2
    soma += double_i
print(soma) # 526
print()

lista = [5, 7, 3, 4, 2, 6, 7, 8, 9]
tamanho = len(lista)
print(f'A lista tem {tamanho} valores')
print()

# contando o número de colunas
lst = [[1, 2, 3], [7, 8, 9,], [5, 6, 2]]
primeira_linha = lst[0]
contador = 0
for coluna in primeira_linha:
    contador += 1

print(f'A lista tem {contador} colunas')
print()

dicionario = {'l1': 'Python', 'l2': 'Julia', 'l3': 'R'}
for k, v in dicionario.items():
    print(k, v)
'''
l1 Python
l2 Julia
l3 R
'''
