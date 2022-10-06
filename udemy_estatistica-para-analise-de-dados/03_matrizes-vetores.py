from os import system
import numpy as np
system('clear')

'''
Matriz:
1 2 3
4 5 6
7 8 9

Vetor = [2, 5, 7, 8]
'''

matriz = [[1, 2, 3], 
          [7, 8, 2], 
          [8, 4, 6]]

print(matriz, type(matriz))
# [[1, 2, 3], [7, 8, 2], [8, 4, 6]] <class 'list'>

vetor_02 = np.array([1, 5.6, -3, 9])
print(vetor_02, type(vetor_02))
# [ 1.   5.6 -3.   9. ] <class 'numpy.ndarray'>

matriz_03 = np.diag((2, 6, 7, 4, 5, 7, 8, 9))
print(matriz_03, type(matriz_03))
'''
[[2 0 0 0 0 0 0 0]
 [0 6 0 0 0 0 0 0]
 [0 0 7 0 0 0 0 0]
 [0 0 0 4 0 0 0 0]
 [0 0 0 0 5 0 0 0]
 [0 0 0 0 0 7 0 0]
 [0 0 0 0 0 0 8 0]
 [0 0 0 0 0 0 0 9]] <class 'numpy.ndarray'>
'''