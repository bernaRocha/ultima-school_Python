def apresentacao(nome):
    return f'Olá, {nome}'

def apresentacao_com_nome(nome, idade):
    return f'Olá, {nome}, sua idade é: {idade}'

def potencia(x, expoente=2):
    return x ** expoente

def juros_simples(capital, taxa, tempo):
    return capital * (taxa / 100) * tempo

def junta_com_ampersand(*args):
    return "&".join(args)

def junta_com_underscore(*args):
    return '_'.join(args)

def fatorial(numero):
    if numero == 1:
        return 1
    
    return numero * fatorial(numero - 1)