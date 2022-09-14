from os import system
system('clear')

numero1 = int(input('Informe o primeiro número: '))
numero2 = int(input('Informe o segundo número: '))

somatorio = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2
modulo_divisao = numero1 % numero2
divisao_inteira = numero1 // numero2

print(f'A soma de {numero1} com {numero2} é {somatorio}\n'
f'A subtração de {numero1} com {numero2} é {subtracao}\n'
f'A multiplicação de {numero1} com {numero2} é {multiplicacao}\n'
f'A divisão de {numero1} com {numero2} é {divisao}' 
f'O módulo de {numero1} com {numero2} é {modulo_divisao}\n'
f'A divisão inteira de {numero1} com {numero2} é {divisao_inteira}\n')
