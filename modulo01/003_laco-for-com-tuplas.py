nomes = ['Bernardo', 'Bianca', 'Naomi', 'Renata', 'Mariana', 'Edu']
idades = [21, 19, 34, 52, 45, 51]

lista_de_tuplas = zip(nomes, idades)

for indice, idade in enumerate(idades):
    if idade > 50:
        
        print(f'No índice {indice} a pessoa é maior que 50')

#print(f'No índice {indice} a pessoa é maior que 50')


nomes_com_ate_6_chars = [nome for nome in nomes if len(nome) <= 6]
print(f'Nomes com até 6 caracteres: {nomes_com_ate_6_chars}')

print([nome.upper() for nome in nomes])