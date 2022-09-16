from os import system
from funcoes import *
system('clear')

print(apresentacao('Bernardo')) # Olá, Bernardo
print(apresentacao_com_nome('Bernardo', 34)) # Olá, Bernardo, sua idade é: 34

print(potencia(3)) # 9
print(potencia(3, 5)) # 243

print(juros_simples(1000, 4, 6)) # 240.0

print(junta_com_ampersand('parametro1', 'parametro2')) # parametro1&parametro2

print(junta_com_underscore('eu', 'estudo', 'todo', 'dia')) # eu_estudo_todo_dia

print(fatorial(5)) # 120