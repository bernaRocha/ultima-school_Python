'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a 
senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando 
a pedir as informações. 
'''

from os import system
system('clear')

nome = input('Qual seu nome? ')
senha = input('Registre uma senha: ')

while senha == nome:
    print('Essa senha é inválida, tente novamente.')
    senha = input('Registre uma senha: ')

print('Nome e senha cadastradas com sucesso. ')
