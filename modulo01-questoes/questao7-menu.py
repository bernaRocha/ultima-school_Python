'''
Uma loja de móveis está com dificuldades de calcular algumas condições de pagamento de seus móveis. 
Eles possuem algumas regras e o seu trabalho é implementar uma aplicação que faça os cálculos 
de acordo com as regras:
Regras
À vista em dinheiro, recebe 15% de desconto
À vista no cartão de crédito, recebe 10% de desconto
Em duas vezes, preço normal de etiqueta sem juros
Mais de duas vezes, preço normal de etiqueta mais juros de 10%

O programa deve ter uma variável com o valor de etiqueta do produto, 
uma variável com forma de pagamento e uma com o preço final após a aplicação de uma das regras.
'''

from os import system
system('clear')

preco_etiqueta = float(input('Qual o preço do produto: '))

print('''Opções de pagamento:
[ 1 ] - À vista em dinheiro, recebe 15% de desconto
[ 2 ] - À vista no cartão de crédito, recebe 10% de desconto
[ 3 ] - Em duas vezes, preço normal de etiqueta sem juros
[ 4 ] - Mais de duas vezes, preço normal de etiqueta mais juros de 10%
''', end='\n\n')

forma_de_pagamento = int(input('Qual a opção desejada: '))

a_vista_dinheiro = preco_etiqueta - (0.15 * preco_etiqueta)
a_vista_cartao = preco_etiqueta - (0.10 * preco_etiqueta)
duas_vezes = preco_etiqueta
acima_duas_vezes = preco_etiqueta + (0.10 * preco_etiqueta)


if forma_de_pagamento == 1:
    preco_final = a_vista_dinheiro 
    print(f'A compra de valor R$ {preco_etiqueta:.2f} vai ficar em R$ {preco_final:.2f}')

elif forma_de_pagamento == 2:
    preco_final = a_vista_cartao
    print(f'A compra de valor R$ {preco_etiqueta:.2f} vai ficar em R$ {preco_final:.2f}')

elif forma_de_pagamento == 3:
    preco_final = duas_vezes
    parcela = duas_vezes / 2
    print(f'A compra de valor R$ {preco_etiqueta:.2f} vai ficar em R$ {preco_final:.2f}' 
    'e cada parcela de valor R$ {parcela:.2f}')

else:
    preco_final = acima_duas_vezes
    print(f'A compra de valor R$ {preco_etiqueta:.2f} vai ficar em R$ {preco_final:.2f}')
    
print(f'Volte sempre!!!!')
