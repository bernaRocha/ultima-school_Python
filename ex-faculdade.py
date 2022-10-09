from os import system
system('clear')
x = 3
y = (3**2) + ((14+4)/2) * 9-10

z = 'Lógica'
w = z + ' Programação'

t = (x <= y) and (not(y != x)) == (y >= x)
k = not t or (x > y)
print(t, k)