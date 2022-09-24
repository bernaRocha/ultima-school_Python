'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são 
do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato 
e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, 
    dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
Ex:
Salário Bruto: (5 * 220)                : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00 
'''
from os import system
system('clear')

hora_trabalho = float(input('Qual o valor da sua hora/trabalho? '))
horas_mes = float(input('Quantas horas você trabalhou esse mês? '))

salario_bruto = hora_trabalho * horas_mes

if salario_bruto <= 900:
    desconto_imposto_renda = 0
elif salario_bruto <= 1500:
    desconto_imposto_renda = 0.05 * salario_bruto
elif salario_bruto <= 2500:
    desconto_imposto_renda = 0.1 * salario_bruto
else: 
    desconto_imposto_renda = 0.2 * salario_bruto


desconto_inss = 0.1 * salario_bruto
desconto_fgts = 0.11 * salario_bruto
total_descontos = desconto_imposto_renda + desconto_inss + desconto_inss

salario_liquido = salario_bruto - total_descontos

print(f'\nSalário bruto: ({hora_trabalho:.2f} R$/H * {horas_mes:.0f} Hrs)', end='')
print(f' : R$ {salario_bruto:>8.2f}')

print()

print(f'(-) IR (5%)      ', end='')
print(f'                   : R$ {desconto_imposto_renda:>8.2f}')

print(f'(-) INSS (10%)',end='')
print(f'                      : R$ {desconto_inss:>8.2f}')

print(f'FGTS (11%)',end='')
print(f'                          : R$ {desconto_fgts:>8.2f}')
 
print('Total de descontos', end='')
print(f'                  : R$ {total_descontos:>8.2f}')

print('\nSalário líquido', end='')
print(f'                     : R$ {salario_liquido:>8.2f}')
