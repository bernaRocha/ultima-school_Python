from os import system   
system('clear')

# Exercício 2 - Reescreva o código abaixo, usando a função map(). O resultado final deve ser o mesmo!
'''
palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil'.split()
resultado = [[w.upper(), w.lower(), len(w)] for w in palavras]
for i in resultado:
    print (i)
'''

palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil'.split()

def analisa_frase(frase):
    resultado = [[w.upper(), w.lower(), len(w)] for w in frase]
    for i in resultado:
        print (i)

map(analisa_frase(palavras), palavras)
