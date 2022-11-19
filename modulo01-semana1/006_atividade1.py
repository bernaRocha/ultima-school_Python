from os import system
system('clear')

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

resultado1 = 2 * numero1 * (numero2 / 2)
resultado2 = 3 * numero1 + numero2
resultado3 = numero2 ** 3

print(f'O produto do dobro do primeiro pela metade do segundo é {resultado1:.0f}')
print(f'A soma do triplo do primeiro com o segundo é {resultado2}')
print(f'O segundo elevado ao cubo é {resultado3}')
