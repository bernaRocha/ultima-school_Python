from os import system
system('clear')

# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou 
# igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"

# hoje = input('Qual dia da semana é hoje? ').capitalize().split()
# if hoje == 'Sábado' or 'Domingo':
#     print('Hoje é dia de descansar. Desliga o computador')
# else:
#     print('Você precisa trabalhar!')

# Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista
lista_frutas = ['Morango', 'Uva', 'Maça', 'Banana', 'Melão']
if 'Morango' in lista_frutas:
    print('Morango faz parte da lista')
else:
    print('Morango não faz parte da lista')
print()

# Exercício 3 - Crie uma tupla de 4 elementos, 
# multiplique cada elemento da tupla por 2 e guarde os resultados em uma 
# lista

lista_numeros = []
tupla_numeros = (5, 6, 7, 9)

for n in tupla_numeros:
    n *= 2
    lista_numeros.append(n)
print(lista_numeros)
print()

# Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela
for numero in range(100, 151, 2):
    print(numero, end=' - ')
print(' FIM')
print()

# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. Enquanto temperatura for maior que 35, 
# imprima as temperaturas na tela

temperatura = 40
while temperatura > 35:
   print(temperatura, end=' ')
   temperatura -= 1



