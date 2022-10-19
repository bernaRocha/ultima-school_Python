from os import system   
system('clear')

ex = zip([1,2,3,4], [1,2,3])
print(ex)                                   # <zip object at 0x7f1821eedf40>
print(list(ex))                             # [(1, 1), (2, 2), (3, 3)]

x = [4, 7, 8]
y = [4, 90, 54]

print(list(zip(x, y)))                      # [(4, 4), (7, 90), (8, 54)]

d1 = {1: 'python', 2: 'SQL'}
d2 = {3: 'Java', 4: 'Spark'}

print(list(zip(d1, d2)))                    # [(1, 3), (2, 4)]
print(list(zip(d1.values(), d2.values())))  # [('python', 'Java'), ('SQL', 'Spark')]
print(list(zip(d1, d2.values())))           # [(1, 'Java'), (2, 'Spark')]

def trocaValores(d1, d2):
    dictTemp = {}

    for d1key, d2val in zip(d1, d2.values()):
        dictTemp[d1key] = d2val
    
    return dictTemp

print(trocaValores(d1, d2))                 # {1: 'Java', 2: 'Spark'}
