'''
O caixa no bar do Sr. João está cheio de diversas moedas. 
O Sr. João precisa fechar o caixa, mas está com dificuldade de fazer os cálculos 
do tanto de dinheiro que ele possui em moedas. Enquanto estava organizando ele conseguiu 
separar as moedas e contar a quantidade delas conforme a tabela:

Moeda               Quantidade
5 centavos              35
10 centavos             50
25 centavos             30
50 centavos             15
1 real                  19

'''
from os import system
system('clear')

total_em_caixa = (0.05 * 35) + (0.10 * 50) + (0.25 * 30) + (0.50 * 15) + (1 * 19)
print(f'O Sr. João tem um total em caixa de R$ {total_em_caixa}.')
