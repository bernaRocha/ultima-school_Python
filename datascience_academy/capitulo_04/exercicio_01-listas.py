from os import system   
system('clear')

# Exercício 1 - Crie uma lista de 3 elementos e calcule a terceira potência de cada elemento.

lista = []
terceira_potencia = []
i = 1

while True:
    numero = int(input(f"Registre um número na posição {i} para a lista: "))
    i += 1
    lista.append(numero)

    if len(lista) == 3:
        break

for num in lista:
    num = num ** 3
    terceira_potencia.append(num)
    
    list(terceira_potencia)

print(f'A terceira potência da lista {lista} é: {terceira_potencia}')
    