from os import system   
system('clear')

# Exercício 6 - Considerando o range de valores abaixo, use a função filter() para retornar apenas os valores negativos.
range(-5, 5)

resultado = filter(lambda x: x < 0, range(-5, 5))
print(list(resultado))
# [-5, -4, -3, -2, -1]

#### sem filter()
for i in range(-5, 5):
    if i < 0:
        print(i, end=" ")

# -5 -4 -3 -2 -1