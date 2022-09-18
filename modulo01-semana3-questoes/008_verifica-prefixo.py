'''
8. Crie uma função que receba duas palavras e retorne True caso a primeira palavra 
seja um prefixo da segunda. Exemplo: 'uf' é prefixo de 'ufabc'. 'ufabc' não é prefixo de 'uf'.
'''
from os import system
system('clear')


def verifica_prefixo():
    palavra_1 = input('Digite a primeira palavra: ').strip().upper()
    palavra_2 = input('Digite a segunda palavra: ').strip().upper()
    prefixo_palavrra_1 = palavra_1[:3]

    if prefixo_palavrra_1 in palavra_2:
        print(True)
    else:
        print(False)
    
verifica_prefixo()

'''
Digite a primeira palavra: ultima
Digite a segunda palavra: python
False
'''
