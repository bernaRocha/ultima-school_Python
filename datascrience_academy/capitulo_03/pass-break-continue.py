from os import system
system('clear')

counter = 0
while counter < 100:
    if counter == 7:
        break
    else:
        pass
    print(counter, end=' ')
    counter += 1

print()

for verificador in 'Python':
    if verificador == 'h':
        continue
    print(verificador, end=' ')

print()

for i in range(2, 30):
    j = 2
    counter = 0
    while j < i:
        if i % j == 0:
            counter = 1
            j += 1
        else:
            j += 1
    
    if counter == 0:
        print(f'{str(i)} é um número primo.')
        counter = 0
    else:
        counter = 0