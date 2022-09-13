'''
Um nutricionista está precisando de uma ajuda para calcular o IMC de seus pacientes. 
Para calcular o IMC ele passou a seguinte fórmula: IMC = peso / ( altura )². 
Crie um programa que faça o cálculo do IMC de uma pessoa (ele deve ser impresso na tela) 
e classifique o IMC dessa pessoa de acordo com a tabela (também deverá ser impresso):

Valor do IMC           Classificação
Abaixo de 18,5          Pessoa abaixo do peso
Entre 18,5 e 25         Pessoa com peso normal
Entre 25 e 30           Pessoa acima do peso
Acima de 30             Pessoa obesa

'''

from os import system
system('clear')

peso_atual = float(input('Qual seu peso atual em Kg: '))
altura = float(input('Qual a sua altura: '))

imc = peso_atual / (altura * altura)

MUITO_ABAIXO = imc < 17
ABAIXO_PESO = imc <= 18.5
PESO_NORMAL = imc <= 25
SOBREPESO = imc <= 30
OBESIDADE_GRAU1 = imc <= 35
OBESIDADE_GRAU2 = imc <= 40
OBESIDADE_MORBIDA = imc > 40

print(f'Seu IMC é de {imc:.1f}')

if MUITO_ABAIXO:
    print(f'Seu IMC é {imc}. Seu peso está muito baixo!')
elif ABAIXO_PESO:
    print(f'Seu IMC é {imc}. Você está abaixo do peso')
elif PESO_NORMAL:
    print(f'Seu IMC é {imc}. Você está com o peso normal')
elif SOBREPESO:
    print(f'Seu IMC é {imc}. Você está com sobrepeso')
elif OBESIDADE_GRAU1:
    print(f'Seu IMC é {imc}. Você está com obesidade grau 1, cuidado')
elif OBESIDADE_GRAU2:
    print(f'Seu IMC é {imc}. Você está com obesidade grau 2, cuidado')
else:
    print(f'Seu IMC é {imc}. Você está com obesidade mórbida, cuidado')
      