from os import system
system('clear')

numero = int(input('Quantas linhas: '))
for i in range(1, numero + 1):
    for j in range(1, i + 1):
        print(i, end='')
    print()
    