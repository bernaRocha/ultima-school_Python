from os import system
system('clear')

numero1 = int(input('Informe o primeiro número: '))
numero2 = int(input('Informe o segundo número: '))

SOMATORIO = numero1 + numero2
SUBTRACAO = numero1 - numero2
MULTIPLICACAO = numero1 * numero2
DIVISAO = numero1 / numero2
MODULO_DIVISAO = numero1 % numero2
DIVISAO_INTEIRA = numero1 // numero2

print(f'A soma de {numero1} com {numero2} é {SOMATORIO}\n'
f'A subtração de {numero1} com {numero2} é {SUBTRACAO}\n'
f'A multiplicação de {numero1} com {numero2} é {MULTIPLICACAO}\n'
f'A divisão de {numero1} com {numero2} é {DIVISAO}' 
f'O módulo de {numero1} com {numero2} é {MODULO_DIVISAO}\n'
f'A divisão inteira de {numero1} com {numero2} é {DIVISAO_INTEIRA}\n')
