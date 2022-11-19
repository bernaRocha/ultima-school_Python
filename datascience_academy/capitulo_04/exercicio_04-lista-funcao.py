from os import system   
system('clear')

# Exercício 4 - Crie duas funções, uma para elevar um número ao quadrado e outra para elevar ao cubo. 
# Aplique as duas funções aos elementos da lista abaixo. 
# Obs: as duas funções devem ser aplicadas simultaneamente.
lista = [0, 1, 2, 3, 4]

ao_quadrado = []
ao_cubo = []

def elevar_ao_quadrado(lista):
    for i in lista:
        ao_quadrado.append(i ** 2)
    #print(ao_quadrado)
    return ao_quadrado

def elevar_ao_cubo(lista):
    for i in lista:
        ao_cubo.append(i ** 3)
    return ao_cubo
    #print(ao_cubo)

print(f'Ao quadrado: {elevar_ao_quadrado(lista)}\n'
f'Ao cubo: {elevar_ao_cubo(lista)}')
