from os import system
system('clear')

combinacoes = [
    (True, True),
    (True, False),
    (False, True),
    (False, False)
]

print('AND -> e')
for x, y in combinacoes:
    print(f'{x} AND {y} -> {x and y}')

print(end='\n\n')

print('OR -> ou')
for x, y in combinacoes:
    print(f'{x} OR {y} -> {x or y}')
print(end='\n\n')

combinacoes2 = [
    True,
    False
]
print('NOT -> não')
for x in combinacoes2:
    print(f'NOT {x} -> {not x}')
    