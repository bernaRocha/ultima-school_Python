from os import system
system('clear')

# pip install better_profanity

### Só funciona com textos em inglês

from better_profanity import profanity
texto = input('Entre com o texto: ')
censurado = profanity.censor(texto)
print(censurado)
