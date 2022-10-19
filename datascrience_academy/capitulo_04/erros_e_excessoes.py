from os import system   
system('clear')

try:
    8 + 's'
except TypeError:
    print("Não é possível somar um número com uma string")


try:
    f = open('arquivos/naoexiste.txt', 'w')
    f.writable('Gravando onde não existe')
except IOError:
    print("O arquivo não existe ou não pode ser encontrado")
else:
    print("Conteúdo gravado com suecesso")
    f.close()

def pergunta():
    try:
        valor = int(input("Digite um número: "))
    except UnboundLocalError:
        print("Não digitou um número")
    finally:
        print("Obrigado")
    print(valor)

def pergunta():
    try:
        valor = int(input("Digite um número: "))
    except:
        print("Não digitou um número")
        valor = int(input("Digite um número: "))
    finally:
        print("Obrigado")
    print(valor)

#pergunta()

def pergunta_num():
    while True:
        try:
            num = int(input("Digite um número inteiro: "))
        except:
            print("Não digitou!")
            continue
        else:
            print("Obrigado")
            break
        finally:
            print("Fim da execução!")
    print(f'Número digitado: {num}')
    
pergunta_num()

tupla = (1, 2, 3)
try:
    tupla.append(4)
    for each in tupla:
        print(each)
except AttributeError as e:
    print('Erro: ', e)
except IOError as e:
    print('Errio de I/O: ', e)
    