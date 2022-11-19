'''
Faça um Programa que peça as 4 notas bimestrais e mostre a média. 
'''
from os import system
system('clear')

notas_aluno = []
for notas in range(0, 4):
    notas = notas_aluno.append(float(input('Registre a nota do aluno: ')))

    media = sum(notas_aluno) / 4

print(f'A média do aluno é {media:.2f}')
