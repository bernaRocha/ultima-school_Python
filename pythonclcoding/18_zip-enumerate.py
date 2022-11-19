from os import system
system('clear')

# zip enumerate
nomes = ['Fulano', 'Beltrano', 'Ciclano']
idades = [20, 31, 72]

for i, (nomes, idades) in enumerate(zip(nomes, idades)):
    print(i, nomes, idades)
'''
0 Fulano 20
1 Beltrano 31
2 Ciclano 72
'''

# zip Dictionary
produtos = ['PC gamer', 'Mouse com fio', 'Discman']
precos = [10.000, 30, 290]

produtos_precos = {produtos: precos for produtos,
                   precos in zip(produtos, precos)}

print(produtos_precos)
# {'PC gamer': 10.0, 'Mouse com fio': 30, 'Discman': 290}
