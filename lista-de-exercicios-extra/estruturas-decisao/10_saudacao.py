'''
Faça um Programa que pergunte em que turno você estuda. 
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso. 
'''
from os import system
system('clear')

turno = '''
[ M ] - Matutino
[ V ] - Vespertino
[ N ] - Noturno
'''

print(turno)
pergunta = input('Em qual turno você estuda? ').strip().upper()

if 'M' in pergunta:
    print('Bom dia!')
elif 'V' in pergunta:
    print('Boa tarde!')
elif 'N' in pergunta:
    print('Boa noite!')
else:
    print('Valor inválido')
