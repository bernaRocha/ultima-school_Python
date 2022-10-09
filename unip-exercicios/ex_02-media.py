from os import system
system('clear')

p1 = 0.4
p2 = 0.6
nota01 = float(input('Digite a nota 01: '))
nota02 = float(input('Digite a nota 02: '))
media = (nota01 * p1) + (nota02 * p2)

print(f'A média é {media}')