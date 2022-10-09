from os import system
from time import sleep
system('clear')


numero_01 = int(input('Entre com um valor: '))
numero_02 = int(input('Entre com outro valor: '))
print(f'O número 1 é: [{numero_01}] e o 2 é: [{numero_02}]')
sleep(1)

print('Trocando os valores')

if numero_01 != numero_02:
    auxiliar = numero_01
    numero_01 = numero_02
    numero_02 = auxiliar
else:
    print('Os números são iguais não é possível ver o algoritmo funcionar')

print(f'Agora o número 1 é: [{numero_01}] e o 2 é: [{numero_02}]')
