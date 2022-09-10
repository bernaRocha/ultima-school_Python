print('Começo')

soma = 0

while soma < 100:
    soma += 11
    print(f'Soma = {soma}', end=' | ')
print('FIM')

print('Outro exemplo')

soma = 1

contagem = 1

max_repeticoes = 110

while soma < 100:
    soma -= 5
    print(f'Soma = {soma}', end=' | ')

    contagem += 1
    if contagem > max_repeticoes:
        print()
        print(f'Máximo de repetições {max_repeticoes} foi atingido.')
        print(f'Soma {soma}')
        break

print('Fim do segundo exemplo.')

'''
while condicao:
    try:
        # codigo
        # break
    except:
        # retorna erro
        # conta repetições para quebrar a condição
'''
