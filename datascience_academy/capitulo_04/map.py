from os import system
system('clear')


lista = [1, 2, 3, 4, 5, 6]
quadrados = []

for num in lista:
    quadrados.append(num **2)

print(quadrados) # [1, 4, 9, 16, 25, 36]

##### feito com map
    ### map(funcao, objeto)

def ao_quadrado(num):
    return num ** 2

print(map(ao_quadrado, lista)) # <map object at 0x7f090ddb9370>

for algarismo in map(ao_quadrado, lista):
    print(algarismo, end=' ') # 1 4 9 16 25 36
print('')

lista_ao_quadrado = list(map(ao_quadrado, lista))
print(lista_ao_quadrado) # 1 4 9 16 25 36

#### map com lambda

com_lambda = map(lambda x: x ** 2, lista)
print(com_lambda) # <map object at 0x7fd25e62b160>
print(list(com_lambda)) # [1, 4, 9, 16, 25, 36]

lista_a = [1, 6, 8, 90, 3456]
lista_b = [50, 2, 5, 7,0]

print(list(map(lambda x, y: x + y, lista_a, lista_b))) # [51, 8, 13, 97, 3456]
