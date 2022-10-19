from os import system   
system('clear')

sequencia = ['Python', 'SQL', 'Spark']

print(list(enumerate(sequencia))) # [(0, 'Python'), (1, 'SQL'), (2, 'Spark')]

for indice, valor in enumerate(sequencia):
    print(indice, valor)
''' # Cria uma tabela
0 Python
1 SQL
2 Spark
'''

for indice, valor in enumerate(sequencia):
    if indice >= 2:
        break
    else:
        print(indice, valor)
'''
0 Python
1 SQL
'''      

for i, item in enumerate("Estou cansado hoje"):
    print(i, item, sep=" - ")

'''
0 - E
1 - s
2 - t
3 - o
4 - u
5 -  
6 - c
7 - a
8 - n
9 - s
10 - a
11 - d
12 - o
13 -  
14 - h
15 - o
16 - j
17 - e
'''

for i, item in enumerate(range(8)):
    print(i, item, sep=" - ")
'''
0 - 0
1 - 1
2 - 2
3 - 3
4 - 4
5 - 5
6 - 6
7 - 7
'''
