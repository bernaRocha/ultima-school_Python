'''
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez. 
'''
from os import system
system('clear')

notas = []

while True:

    nota = float(input('Registre a nota do aluno: '))
    
    ### verificação
    if 0 < nota <= 10:
        notas.append(nota)
    else:
        print('Nota inválida')
    
    if len(notas) == 2:
        break

media = (notas[0] + notas[1]) / 2

aprovado_com_distincao = media == 10
aprovado = media >= 7
reprovado = media < 7

if aprovado_com_distincao:
    print(f'Aluno aprovado com distinção pela média {media}')
elif reprovado:
    print(f'Aluno reprovado com média {media:.2f}')
else:
    print(f'Aluno aprovado com média {media:.2f}')
