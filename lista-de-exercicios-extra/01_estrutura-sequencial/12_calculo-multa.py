'''
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento 
diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo 
regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo 
excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes)
e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na 
variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as 
mensagens adequadas. 
'''
from os import system
system('clear')

kilos_pescados = float(input('Total de Kilos pescados: '))
if kilos_pescados > 50:
    excesso = kilos_pescados - 50
    multa_excesso = excesso * 4

    print(f'Tendo pescado uma quantidade de {excesso} Kg acima do permitido por lei\n'
    f'sua multa será de {multa_excesso:.2f} R$')

print(f'Você pescou um total de {kilos_pescados} Kg de peixe')
