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

muito_abaixo = imc < 17
abaixo_peso = imc <= 18.5
peso_normal = imc <= 25
sobrepeso = imc <= 30
obesidade_grau1 = imc <= 35
obesidade_grau2 = imc <= 40
obesidade_morbida = imc > 40

print(f'Seu IMC é de {imc:.1f}')

if muito_abaixo:
    print(f'Seu peso está muito baixo!')
elif abaixo_peso:
    print(f'Você está abaixo do peso')
elif peso_normal:
    print(f'Você está com o peso normal')
elif sobrepeso:
    print(f'Você está com sobrepeso')
elif obesidade_grau1:
    print(f'Você está com obesidade grau 1, cuidado')
elif obesidade_grau2:
    print(f'Você está com obesidade grau 2, cuidado')
else:
    print(f'Você está com obesidade mórbida, cuidado')
  