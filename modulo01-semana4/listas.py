from os import system
system('clear')

# listas
lista = [0, 2, 4, True]
print(lista, type(lista))

lista.append('hello world!')
print(lista[3])

lista_de_nomes = ['Fulano', 'Beltrano', 'Ciclano']
# print(lista_de_nomes[-10]) # IndexError: list index out of range
lista_de_nomes[::-1]

# mostrar os métodos
print(dir(lista_de_nomes))
'''
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', 
'__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', 
'__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', 
'__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
'__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', 
'__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 
'reverse', 'sort']
'''

# mesmo endereço de memória

nomes_selecionados = lista_de_nomes
print(nomes_selecionados)

# endereço diferente de memória
nomes_selecionados = lista_de_nomes.copy()
