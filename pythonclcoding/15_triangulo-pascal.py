from os import system
system('clear')

def trianguloPascal(N):
    for i in range(1, N + 1): # quantidade de linhas no range
        for j in range(0, N - i + 1):
            print(' ', end='')
        
        # o primeiro elemento é sempre 1 
        C = 1
        for j in range(1 , i + 1):
            print(' ', C, sep='', end='')

            C = C * (i - j) // j
        print()

N = int(input('Quantas linhas quer para o triângulo de Pascal? '))

trianguloPascal(N)
print('FIM')
