'''
Criei um programa que possua as variáveis A, B e C. 
Imprima o resultado de A + B caso ele seja menor do que C, caso contrário imprima que o valor é menor. 
Teste a aplicação com alguns valores nas variáveis sugeridas.
'''

from os import system
system('clear')

varA = int(input('Registre o primeiro valor: '))
varB = int(input('Registre o segundo valor: '))
varC = int(input('Registre o terceiro valor: '))

lista_var = [varA, varB, varC]
somatorio = varA + varB


if somatorio < varC:
    print(f'O somaŕio dos dois primeiros valores é {somatorio}')
else:
    print(f'O menor valor é {min(lista_var)}')
