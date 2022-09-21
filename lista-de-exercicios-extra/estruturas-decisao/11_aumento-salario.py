'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.

    Faça um programa que recebe o salário de um colaborador e o reajuste 
    segundo o seguinte critério, baseado no salário atual:

    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% 
    Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento. 
'''

from os import system
system('clear')

salario = float(input('Qual o seu salário? '))
novo_salario = 0

if salario <= 280.0:
    novo_salario = salario + (0.2 * salario)
    valor_reajuste = novo_salario - salario
    print(f'Tendo um salário de {salario:.2f} seu aumento será de 20%.\n'
    f'Você ganhou um reajuste de R$ {valor_reajuste:.2f}\n'
    f'Seu atual salário é {novo_salario:.2f}')

elif salario < 1500.0:
    novo_salario = salario + (0.15 * salario)
    valor_reajuste = novo_salario - salario
    print(f'Tendo um salário de {salario:.2f} seu aumento será de 15%.\n'
    f'Você ganhou um reajuste de R$ {valor_reajuste:.2f}\n'
    f'Seu atual salário é {novo_salario:.2f}')

else:
    novo_salario = salario + (0.05 * salario)
    valor_reajuste = novo_salario - salario
    print(f'Tendo um salário de {salario:.2f} seu aumento será de 5%.\n'
    f'Você ganhou um reajuste de R$ {valor_reajuste:.2f}\n'
    f'Seu atual salário é {novo_salario:.2f}')
