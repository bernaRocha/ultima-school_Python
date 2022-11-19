#import numpy as np
from os import system   
system('clear')

# Exercício 3 - Calcule a matriz transposta da matriz abaixo.
# Caso não saiba o que é matriz transposta, visite este link: https://pt.wikipedia.org/wiki/Matriz_transposta
# Matriz transposta é um conceito fundamental na construção de redes neurais artificiais, base de sistemas de IA.

matrix = [[1, 2],[3,4],[5,6],[7,8]]

print("Matriz original: ")
for i in matrix:
    print(i)

matriz_t = [[k[0] for k in matrix], [k[1] for k in matrix]]
print("\n\n")
print("Matriz transposta: ")
for i in matriz_t:
    print(i)

######## usando numpy ############
# matrix = [[1, 2],[3,4],[5,6],[7,8]]

# matrix_t = np.array(matrix).T

# print("Usando o numpy: ")
# print(matrix_t)

*matrix_t, = zip(*matrix)
print("\n\nCom *: ")
print(matrix_t)
