from os import system
system('clear')

'''
def -> cria um objeto e atribui um nome a ele (nome da função)
lambda -> cria um objeto mas o retorna como um resultado em tmepo de execução
'''

def aoQuadrado(numero):
    return numero ** 2

print(aoQuadrado(2)) # 4

def potencia(num): return num ** 2

print(potencia(5)) # 25

########### ou #############

terceira_potencia = lambda num: num**3
print(terceira_potencia(2)) # 8

verifica_par = lambda x: x% 2==0
print(verifica_par(8)) # True

reverso = lambda string: string[::-1]
print(reverso('disco da xuxa')) # axux ad ocsid

adicao = lambda x, y: x + y
print(adicao(5, 7)) # 12
