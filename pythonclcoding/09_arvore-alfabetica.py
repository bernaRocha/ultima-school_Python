from os import system
system('clear')

numero = int(input('Quantas linhas: '))
for i in range(97, 97 + numero):
    for j in range(97, i + 1):
        print(chr(i), end=" ")
    print()