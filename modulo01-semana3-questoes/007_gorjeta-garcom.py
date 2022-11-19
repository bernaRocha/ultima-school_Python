'''
7. Escreva uma função que, dado o valor da conta de um restaurante, calcule e exiba a gorjeta do garçom, 
considerando 10% do valor da conta.
'''
from os import system
system('clear')

def calcula_gorjeta():
    conta = float(input('Quanto deu a conta no nosso restaurante? '))
    gorjeta = conta * 0.1
    print(f'Tendo consumido R$ {conta}, o garçom receberá {gorjeta:.2f} de gorjeta')
    print('Volte sempre!')

calcula_gorjeta()