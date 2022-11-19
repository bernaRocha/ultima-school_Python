'''
2. Crie de forma recursiva uma função que printe do número recebido até o zero.
'''
from os import system
import time
system('clear')

def print_ate_zero(numero):
    if numero != 0:
        for i in range(numero, -1, -1):
            print(i, end="\n")
            time.sleep(1)
    else:
        print('Tente com um número diferente de zero')

print("Contando até ZERO")
print_ate_zero(10)
print('FIM')
