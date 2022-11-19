'''
Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário. 
'''

from os import system
system('clear')

lado = float(input('Medida do lado do quadrado (cm): '))
altura = float(input('Medida da altura do quadrado (cm): '))
area_quadrado = lado * altura
dobro_area = 2 * area_quadrado
print()
print(f'A área do quadrado mede: {area_quadrado:.2f} cm\n'
f'e o dobro da área mede {dobro_area:.2f} cm')
