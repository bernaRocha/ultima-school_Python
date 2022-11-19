from os import system
system('clear')

def ChecaBissexto(ano):
    if((ano % 400 == 0) or (ano % 100 != 0) and (ano % 4 == 0)):
        print(f'O ano {ano} é bissexto')
    else:
        print(f'O ano {ano} NÃO é bissexto')
    
ano = int(input('Entre com o ano: '))

ChecaBissexto(ano)
