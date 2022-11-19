import datetime
from os import system
system('clear')

# funciona no IPython e no shell do Python

agora = datetime.datetime.now()
print(agora)

t = datetime.time(7, 43, 27)
print(t)

print(f'Hora {t.hour}')
