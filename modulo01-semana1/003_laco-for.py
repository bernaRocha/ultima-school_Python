print('Fulano'.lower())

nomes = ['Fulano', 'Beltrano', 'Ciclano', 'Nome Composto', 'Ana', 'Naomi']

for nome in nomes:
    print(f'Em minúsculas: {nome.lower()}')

for nome in nomes:
    print(f'Em maiúsculas: {nome.upper()}')

print(list(range(5,11)))

for numero in range(1,20, 2): # de 1 até 50 pulando de 2 em 2
    print(numero)

nomes_ = ['Bernardo', 'Bianca', 'Naomi', 'Renata', 'Mariana', 'Edu']
idade = [21, 19, 34, 12, 45, 31]

lista_de_tuplas = zip(nomes_, idade)
#print(next(lista_de_tuplas))
#print(list(lista_de_tuplas)) # [('Eu', 21), ('Você', 19)]

for nomes_, idade in lista_de_tuplas:
    print(f'Nome:{nomes_} tem {idade} anos de idade')

'''
Nomes:Eu
Idades: 21
Nomes:Você
Idades: 19
'''
