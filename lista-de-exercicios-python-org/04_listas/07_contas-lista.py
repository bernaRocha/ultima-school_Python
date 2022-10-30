'''
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números. 
'''

from os import system
system('clear')

numeros = []
multiplicacao = 1

for i in range(5):
    i = int(input("Registre um valor para a lista: "))
    numeros.append(i)

somatorio = sum(numeros)

for i in numeros:
    multiplicacao *= i

print(f'A lista registrada é: {numeros}')
print(f'A soma dos números dessa lista é: {somatorio}')
print(f'A multiplicação dos termos é: {multiplicacao}')
