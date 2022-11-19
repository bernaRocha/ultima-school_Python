from os import system
system('clear')

linhas = 7
diferenca = linhas

for i in range(0, linhas):
    print(' ' * i, end='')
    print('* ' * (diferenca - i), end='')
    print('')
