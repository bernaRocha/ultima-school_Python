'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

    o produto do dobro do primeiro com metade do segundo .
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo. 
'''
from os import system
system('clear')

numero_inteiro = int(input('Registre um número inteiro: (-2,-1,0,1,2...) '))
numero_inteiro_02 = int(input('Registre outro número inteiro: (-2,-1,0,1,2...) '))
numero_real = float(input('Registre um número real: (natural, inteiro, racional ou irracional...) '))

resultado_01 = (2 * numero_inteiro) * (numero_inteiro_02 / 2)
resultado_02 = (3 * numero_inteiro) + numero_real
resultado_03 = pow(numero_real, 3)

print(f'O dobro de {numero_inteiro} multiplicado pela metade de {numero_inteiro_02} = {resultado_01}')
print(f'A soma do triplo de {numero_inteiro} com {numero_real} = {resultado_02}')
print(f'O cubo de {numero_real} = {resultado_03}')
