'''
Um freelancer está com dificuldade para calcular qual o valor cobrar por um projeto 
que está estimado em 80 horas. Após pensar e revisitar o preço de alguns projetos 
que cobrou no passado ele montou a seguinte fórmula: 
valor inicial + quantidade de horas estimadas * valor da hora + 15% do valor calculado. 
Sua tarefa é criar um programa que faça essa conta para o freelancer. 

Considere que o valor inicial sempre será 1000,00 R$ e o valor da hora cobrada é de 20,45 R$. 

A aplicação deve imprimir o valor calculado pelo projeto considerando duas casas decimais na formatação do valor.
Dica: Olhar a ordem como as operações da fórmula devem ser realizadas.
'''
from os import system
system('clear')

horas_trabalhadas = 80

VALOR_BASE = 1000.00
VALOR_HORA = 20.45

valor_inicial = VALOR_BASE + (horas_trabalhadas * VALOR_HORA)
taxa_extra = (15/ 100) * valor_inicial

orcamento = valor_inicial + taxa_extra

print(f'O orçamento total a ser cobrado é de R$ {orcamento:.2f}')
