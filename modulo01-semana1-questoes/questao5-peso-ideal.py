'''
Criei um programa que calcule o peso ideal de uma pessoa. Para isso utilize as fórmulas da tabela:
Para Homens: (72.7 * altura) – 58
Para Mulheres: (62.1 * altura) – 44.7 

Sua aplicação deve identificar se a pessoa é Homem ou Mulher e então fazer o cálculo apropriado. 
Deve ser impresso se a pessoa é homem ou mulher, juntamente com o peso ideal calculado.

'''
from os import system
system('clear')

print('Vamos calcular seu peso ideal')

nome = input('Como gostaria de ser chamado? ')
genero = input('Qual seu gênero? [M/m] [F/f] ').upper()
altura = float(input('Qual sua altura? [x.xx] '))
peso = float(input('Qual seu peso? '))

PESO_IDEAL_HOMEM = (72.7 * altura) - 58
PESO_IDEAL_MULHER = (62.1 * altura) - 44.7


if genero == 'M':
    print(f'{nome} seu peso ideal é de {PESO_IDEAL_HOMEM:.2f} Kg')
else:
    PESO_IDEAL_MULHER = (62.1 * altura) - 44.7
    print(f'{nome} seu peso ideal é de {PESO_IDEAL_MULHER:.2f} Kg')
