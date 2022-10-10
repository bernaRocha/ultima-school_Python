from os import system
system('clear')

numero_01 = float(input('Primeiro número: '))
numero_02 = float(input('Segundo número: '))

ADICAO = numero_01 + numero_02
SUBTRACAO = numero_01 - numero_02
MULTIPLICACAO = numero_01 * numero_02
DIVISAO = numero_01 / numero_02
DIVISAO_INTEIRA = numero_01 // numero_02
EXPONENCIACAO = numero_01 ** numero_02

print(f'Soma:            {numero_01} + {numero_02} = {ADICAO}\n'
f'Subtração:       {numero_01} - {numero_02} = {SUBTRACAO}\n'
f'Multiplicação:   {numero_01} * {numero_02} = {MULTIPLICACAO}\n'
f'Divisão:         {numero_01} / {numero_02} = {DIVISAO}\n'
f'Divisão inteira: {numero_01} // {numero_02} = {DIVISAO_INTEIRA}\n'
f'Exponenciação:   {numero_01} ** {numero_02} = {EXPONENCIACAO}\n')
