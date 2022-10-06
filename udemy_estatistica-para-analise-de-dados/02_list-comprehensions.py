from os import system
system('clear')

lista = []
for valor in range(10):
    lista.append(valor  + 10)

print(f'Lista: {lista}')
#### Lista: [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# de forma resumida
lista = [valor + 10 for valor in range(10)]
print(f'Lista: {lista}')
#### Lista: [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

multiplos_03 = []
for numero in range(0, 100):
    if numero % 3 ==0:
        multiplos_03.append(numero)

print(f'Múltiplos de 3 até o número 100: {multiplos_03}')
'''
Múltiplos de 3 até o número 100: [0, 3, 6, 9, 12, 15, 18, 21, 
24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 
72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
'''

conceito = ['aprovado' if nota >= 7 else 'reprovado' for nota in range(0, 11)]
print(conceito)
'''
['reprovado', 'reprovado', 'reprovado', 'reprovado', 'reprovado', 'reprovado', 'reprovado',
'aprovado', 'aprovado', 'aprovado', 'aprovado']
'''
