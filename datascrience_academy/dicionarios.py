from os import system
system('clear')

estudantes_lst = ['Fulano', 24, 'Ciclano', 30, 'Beltrano', 18, 'Fernanda', 29, 'João', 40]

estudantes_dct = {'Fulano': 24, 'Ciclano': 30, 'Beltrano': 18, 'Fernanda': 29, 'João': 40}
print(estudantes_dct['Fulano'])

estudantes_dct['Novo nome'] = 20
print(estudantes_dct)

print(estudantes_dct.keys())
#### dict_keys(['Fulano', 'Ciclano', 'Beltrano', 'Fernanda', 'João', 'Novo nome'])

print(estudantes_dct.values())
#### dict_values([24, 30, 18, 29, 40, 20])

print(estudantes_dct.items())
##### dict_items([('Fulano', 24), ('Ciclano', 30), ('Beltrano', 18), ('Fernanda', 29), ('João', 40), ('Novo nome', 20)])

print(len(estudantes_dct)) # 6

estudantes_novos = {'Outro': 14, 'Mais um': 25}
estudantes_dct.update(estudantes_novos)
print(estudantes_dct)
#### {'Fulano': 24, 'Ciclano': 30, 'Beltrano': 18, 'Fernanda': 29, 'João': 40, 'Novo nome': 20, 'Outro': 14, 'Mais um': 25}

## Dicionário aninhado
dict_aninhado = {'chave1': {'chave2_aninhada': {'chave3_aninhada':'Dicionário aninhado em Python'}}}

print(dict_aninhado['chave1']['chave2_aninhada']['chave3_aninhada'])
#### Dicionário aninhado em Python
