from os import system
system('clear')

linhas = int(input('Quantas linhas no diamante: '))
print('Imprimindo o diamante')


for i in range(1, linhas + 1):
    for j in range(1, linhas - i + 1):
        print(end=" ")
    for k in range(0, 2 * i - 1):
        print('*', end='')
    print()
for i in range(1, linhas):
    for j in range(1, i + 1):
        print(end=" ")
    for l in range(1, (2 * (linhas - i))):
        print('*', end='')
    print()
    