'''
Faça um Programa que peça as quatro notas de 10 alunos, 
calcule e armazene num vetor a média de cada aluno, 
imprima o número de alunos com média maior ou igual a 7.0. 
'''
from os import system
system('clear')

medias_alunos = []
media_acima_07 = 0

for aluno in range(10):
    soma_notas = 0

    for nota in range(4):
        soma_notas = float(input(f'Registre a {nota + 1}º nota do aluno {aluno + 1}: '))
        
    
    medias_alunos.append(sum(soma_notas / 4))

    if medias_alunos[aluno] >= 7:
        
        media_acima_07 += 1

print(f'Médias dos alunos: {medias_alunos}')
print(f'Total de alunmos aprovados: {media_acima_07}')
