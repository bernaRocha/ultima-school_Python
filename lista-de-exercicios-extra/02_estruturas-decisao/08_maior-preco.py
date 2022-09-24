'''
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato. 
'''
from os import system
system('clear')

precos = []

while True:
    preco = float(input('Registre um preço: '))
    precos.append(preco)

    if len(precos) == 3:
        break
precos.sort()
mais_caro = precos[-1]
mais_barato = precos[0]

print(f'O produto mais barato tem o preço R$ {mais_barato}\n'
f'O mais caro tem o preço R$ {mais_caro}')
