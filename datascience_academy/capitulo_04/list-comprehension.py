from os import system   
system('clear')

lst = [x for x in 'python']
print(lst, type(lst)) # ['p', 'y', 't', 'h', 'o', 'n'] <class 'list'>

num = [x for x in range(11) if x % 2 == 0]
print(num, type(num)) # [0, 2, 4, 6, 8, 10] <class 'list'>

celcius = [0, 10, 16.8, 23.5, 32.5, 42.1, 100]

fahrenheit = [((float(9)/5)* temp + 32) for temp in celcius]

print(fahrenheit) # [32.0, 50.0, 62.24, 74.30000000000001, 90.5, 107.78, 212.0]

aninhada = [x ** 2 for x in [x ** 2 for x in range(11)]]

print(aninhada) # [0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561, 10000]
