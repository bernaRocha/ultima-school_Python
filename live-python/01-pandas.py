'''
Link da live: https://www.youtube.com/watch?v=GhKVR72eJmA&ab_channel=EduardoMendes
Array é conhecido como vetor em português

1 dimensão: conhecido como vetor
2 dimensões ou mais: conhecido como matriz
'''

from os import system
from array import array
from numpy import array
from sys import getsizeof
system('clear')

l = list(range(1_000_000))
a = array('i', l)

print(getsizeof(l)) # 8000056
print(getsizeof(a)) # 4000064

print(getsizeof(l)/ 1024/ 1024) # 7.629447937011719 
print(getsizeof(a)/ 1024/ 1024) # 3.81475830078125

# código acima feito antes de importar o numpy 
# parei em 18 min


