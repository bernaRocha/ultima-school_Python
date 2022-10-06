from os import system
system('clear')

def area_quadrado(L):
    area = L**2
    print(f'A área de uma quadrado de lado {L}cm é: {area:.2f}cm')

area_quadrado2 = lambda x: x**2

area_retangulo = lambda base, altura: base * altura

print(area_retangulo(5, 8)) # 40

# a vantagem é utilizar junto de outras funções como a map
lista_lados = [4, 7, 3, 6, 8, 1, 23, 9]

lista_areas = list(map(lambda x: x**2, lista_lados))

print(lista_areas) # [16, 49, 9, 36, 64, 1, 529, 81]
