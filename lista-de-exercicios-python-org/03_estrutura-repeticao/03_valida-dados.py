'''
Faça um programa que leia e valide as seguintes informações:

    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd'; 
'''
from os import system
from time import sleep
system('clear')

print('Vamos registrar seus dados.')

nome = input('Seu primeiro nome: ').capitalize()
while len(nome) <= 3:
    print('Nome muito curto, tente novamente.')
    nome = input('Seu primeiro nome: ').capitalize()

idade = int(input('Qual sua idade? '))

while idade < 0 or idade >= 150:
    print('Idade inválida.')
    idade = int(input('Qual sua idade? '))

salario = float(input('Qual seu salário atualmente? (xxxx.xx) '))
while salario < 0:
    print('Valor inválido, tente novamente')
    salario = float(input('Qual seusalário atualmente? '))

genero = input('Qual seu gênero? [M/F] ').strip().upper()[0]
while genero not in 'MmFf':
    print('Informação inválida, tente novamente.')
    genero = input('Qual seu gênero? [M/F] ').strip().upper()[0]

if genero in 'Mm':
    genero = 'Masculino'
if genero in 'Ff':
    genero = 'Feminino'

estado_civil = input('Qual seu estado civil? [s-solteiro c-casado v-viúvo d-divorciado]: ').strip().upper()[0]
while estado_civil not in 'SCVD':
    print('Informação inválida, tente novamente.')
    estado_civil = input('Qual seu estado civil? [s-solteiro c-casado v-viúvo d-divorciado]: ').strip().upper()[0]

if genero == 'Masculino' and estado_civil == 'S':
    estado_civil = 'Solteiro'
if genero == 'Feminino' and estado_civil == 'S':
    estado_civil = 'Solteira'

if genero == 'Masculino' and estado_civil == 'C':
    estado_civil = 'Casado'
if genero == 'Feminino' and estado_civil == 'C':
    estado_civil = 'Casada'


if genero == 'Masculino' and estado_civil == 'V':
    estado_civil = 'Viúvo'
if genero == 'Feminino' and estado_civil == 'V':
    estado_civil = 'Viúva'

if genero == 'Masculino' and estado_civil == 'D':
    estado_civil = 'Divorciado'
if genero == 'Feminino' and estado_civil == 'D':
    estado_civil = 'Divorciada'

sleep(1)
print(f'#### Dados cadastrados com sucesso #### \n')
sleep(1)

print(f'Nome: {nome}\n' 
f'Idade: {idade} anos\n'
f'Gênero: {genero}\n'
f'Estado civil: {estado_civil}\n'
f'Salario atual: R$ {salario}')
