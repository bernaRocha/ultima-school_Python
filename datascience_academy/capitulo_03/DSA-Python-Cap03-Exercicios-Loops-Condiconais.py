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
print()
# Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela,
# mas quando for encontrado o valor 23, interrompa a execução do programa

contador = 0
while contador < 100:
    contador += 1
    print(contador, end=' ')
    if contador == 23:
        break
print()

# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20, 
# adicione à lista, apenas os valores pares e imprima a lista

lista = []
valor = 4
while valor <= 20:
    valor += 1
    if valor % 2 ==0:
        lista.append(valor)
print(lista)

print()

# Exercício 8 - Transforme o resultado desta função range em uma lista: range(5, 45, 2)
#nums = range(5, 45, 2)

numeros = []
for n in range(5, 45, 2):
    numeros.append(n)

print(numeros, end=' ')
print()

# Exercício 9 - Faça a correção dos erros no código abaixo e execute o programa. Dica: são 3 erros.
#temperatura = float(input('Qual a temperatura? '))
#if temperatura > 30
#print('Vista roupas leves.')
#else
#    print('Busque seus casacos.')

temperatura = float(input('Qual a temperatura? '))
if temperatura > 30:
    print('Vista roupas leves.')
else:
    print('Busque seus casacos.')

print()

# Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. Use um placeholder na 
# sua instrução de impressão

# “É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a 
# vantagem de existir.” (Machado de Assis)

frase = "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir." 

quantidade_r = frase.count('r')

print(f"Na frase há uma quantidade de r's de: {quantidade_r}")
print()
##### ou 
contador = 0
for erre in frase:
    if erre == 'r':
        contador += 1
print(f"Na frase há uma quantidade de r's de: {contador}")
