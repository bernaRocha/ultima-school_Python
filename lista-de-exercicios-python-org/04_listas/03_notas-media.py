'''
Faça um Programa que leia 4 notas, 
mostre as notas e a média na tela. 
'''
from os import system
system('clear')

notas = []

for nota in range(0, 4):
    nota = float(input(f'Registre a nota {nota + 1} do aluno: '))
    notas.append(nota)

media = sum(notas) / 4

print(f'Notas registradas: {notas}')
print(f'A média do aluno é: {media}')
