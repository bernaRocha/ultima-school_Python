from os import system
from datetime import datetime
system('clear')

cadastro = 'Bernardo', 'Programador', 33
print(cadastro, type(cadastro)) # ('Bernardo', 'Programador', 33) <class 'tuple'>

cliente = ('Maria', 'estudante', 20)
nome, profissao, idade = cliente
print(nome) # Maria
print(profissao) # estudante
print(idade) # 20

cliente = cliente[0], 'programadora', cliente[2]
print(cliente) # ('Maria', 'programadora', 20)

print(cliente, len(cadastro)) # ('Maria', 'programadora', 20) 3
nome, profissao, _ = cliente
print(nome, profissao) # Maria programadora

nome, profissao, _ = cadastro
print(nome, profissao) # Bernardo Programador

nome, *restante = cliente
print(nome, restante) # Maria ['programadora', 20]

print(cadastro) # ('Bernardo', 'Programador', 33)
cadastro = 'Bernardo', 'Programador', 33, []
cadastro[-1].append(datetime.today())
print(cadastro) # ('Bernardo', 'Programador', 33, [datetime.datetime(2022, 9, 23, 17, 34, 55, 955989)])
