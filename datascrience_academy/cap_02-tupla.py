from os import system
system('clear')

tupla1 = ('A', 'B', 'C') ### imutável

lista_tupla1 = list(tupla1) ### transforma a tupla em listra
lista_tupla1.append('D') # adiciona

tupla1 = tuple(lista_tupla1) ### transforma a lista em tupla
print(tupla1)
#### ('A', 'B', 'C', 'D')