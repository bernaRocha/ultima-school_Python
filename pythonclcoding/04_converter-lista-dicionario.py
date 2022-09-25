from os import system
system('clear')

frutas = ['manga', 'banana', 'maça', 'uva']
preco = [8, 9, 5, 12]

preco_fruta = dict(zip(frutas, preco))

print(preco_fruta)
# {'manga': 8, 'banana': 9, 'maça': 5, 'uva': 12}
