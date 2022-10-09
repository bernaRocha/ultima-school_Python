from os import system
from unicodedata import numeric
system('clear')

# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.
lista_numeros = []
for i in range(1, 11):
    lista_numeros.append(i)

print(lista_numeros) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela

lista_objetos = ['computador', 'remédio', 'vs code', 'Python', 'Youtube']
print(lista_objetos)
# ['computador', 'remédio', 'vs code', 'Python', 'Youtube']

# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
nome = 'Bernardo'
estado = 'cansado'
print(f'{nome} está {estado}')
# Bernardo está cansado

# # Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla

numero = (1, 2, 2, 3, 4, 4, 4, 5)
print(f'Quantidade de números [4] = {numero.count(4)}')

# Exercício 5 - Crie um dicionário vazio e imprima na tela

dicionario_vazio = {}
print(dicionario_vazio) # {}

# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
dicionario = {'valor01': 10, 'valor02': 30, 'valor03': 40}
print(dicionario)
## {'valor01': 10, 'valor02': 30, 'valor03': 40}

# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela

dicionario['valor04'] = 100
print(f'Novo dicionário: {dicionario}')
## Novo dicionário: {'valor01': 10, 'valor02': 30, 'valor03': 40, 'valor04': 100}

# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.

dic_numerico = {'preco_ps2': 10, 'precos_comida': [10, 20], 'preco_remedio': 100000}
print(dic_numerico)
### {'preco_ps2': 10, 'precos_comida': [10, 20], 'preco_remedio': 100000}

# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.

lista_grande = ['string', ('valor01', 'valor02'), {1: 'Python', 2: 'SQL'}, 3.141592]
print(lista_grande)

## ['string', ('valor01', 'valor02'), {1: 'Python', 2: 'SQL'}, 3.141592]

# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'

print(f'A frase cortada do índice 1 ao 18: {frase[0:19]}')
# A frase cortada do índice 1 ao 18: Cientista de Dados 
