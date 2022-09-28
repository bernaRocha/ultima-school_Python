'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês. 
'''
from os import system
system('clear')

valor_hora = float(input('Qual o valor da sua hora trabalhada? '))
total_horas_mes = float(input('Quantas horas você trabalhou neste mês: '))
salario = valor_hora * total_horas_mes

print(f'Tendo sua hora trabalha da com valor de {valor_hora} R$\n'
f'e trabalhado neste mês um total de {total_horas_mes} Hrs\n'
f'seu salário bruto será de [{salario:.2f}] R$')
