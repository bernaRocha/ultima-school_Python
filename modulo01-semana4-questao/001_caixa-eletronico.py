class CaixaEletronico:

    def __init__(self, nome):
        print(f'Objeto sendo construido: {self}')
        self.notas = [100, 50, 20, 10, 5]
        self.nome_banco = nome

    def sacar(self, valor):
        ...