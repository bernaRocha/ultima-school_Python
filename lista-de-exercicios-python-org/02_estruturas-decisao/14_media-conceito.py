'''
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

      Média de Aproveitamento  Conceito
      Entre 9.0 e 10.0        A
      Entre 7.5 e 9.0         B
      Entre 6.0 e 7.5         C
      Entre 4.0 e 6.0         D
      Entre 4.0 e zero        E
'''
from os import system
system('clear')

notas = []
for i in range(2):
    nota = float(input("Registre a nota do aluno: "))
    notas.append(nota)

print(f'As notas do aluno são: {notas}')

media = sum(notas) / 2

if media < 4:
    conceito = 'E'
elif media < 6:
    conceito = 'D'
elif media < 7.5:
    conceito = 'C'
elif media < 9:
    conceito = 'B'
else:
    conceito = 'A'

print(f'Tendo a média de: {media} pontos o conceito do aluno é: {conceito}')
