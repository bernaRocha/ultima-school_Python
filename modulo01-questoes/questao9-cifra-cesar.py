'''
Extra: A Cifra de César foi uma das primeiras técnicas de criptografia criadas pela humanidade. 
Essa técnica consiste em aplicar um deslocamento de caracteres em uma mensagem, por exemplo, 
se aplicarmos o deslocamento de 3 caracteres:
A letra 'A' fica como letra 'D';
A letra “I” fica como letra “L”;
A letra “Z” fica como letra “C”
E assim por diante.
A palavra “OI” aplicando o deslocamento de 3 caracteres em cada um dos caracteres ficaria como “RL”.
Sua tarefa é criar uma aplicação que possa descriptografar a seguinte frase 
(não aplicamos deslocamento para o caractere espaço): “HVWRX HPSROJDGR FRP R FXUVR GH SBWKRQ”. 
Considere que o deslocamento de caracteres usado foi 3 caracteres.

#### Consegui pesquisando pelos scripts, fiz de criptografar e descriptografar

'''

from os import system
system('clear')

#criptografar
def cifra_cesar(texto, chave):
    texto_entrada = ""
    for i in texto:
        if i.isupper():
            temp = 65 + ((ord(i) - 65 + chave) % 26)
            texto_entrada = texto_entrada + chr(temp)
        elif i.islower():
            temp = 97 + ((ord(i) - 97 + chave) % 26)
            texto_entrada = texto_entrada + chr(temp)
        else:
            texto_entrada = texto_entrada + i
    
    print(f'O texto encriptado é: {texto_entrada}')

input_texto = input('Entre com o texto a ser criptografado: ')
chave = int(input('Entre com a chave: '))
cifra_cesar(input_texto, chave)

#descriptografar
def descripto_cesar(texto, chave):
        texto_encripto = ""
        for i in texto:
            if i.isupper():
                if ((ord(i) - 65 - chave) < 0):
                    temp = 65 + ((ord(i) - 65 - chave + 26) % 26)
                else:
                    temp = 65 + ((ord(i) - 65 - chave) % 26)
                texto_encripto = texto_encripto + chr(temp)
            elif i.islower():
                if ((ord(i) - 97 - chave) < 0):
                    temp = 97 + ((ord(i) - 97 - chave + 26) % 26)
                else:
                    temp = 97 + ((ord(i) - 97 - chave) % 26)
                texto_encripto = texto_encripto + chr(temp)
            else:
                texto_encripto = texto_encripto + i
        
        print(f'O texto descriptografado é: {texto_encripto}')

texto = input('Digite o texto a ser descriptografado: ')
chave = int(input('Entre com a chave de descriptografação: '))
descripto_cesar(texto, chave)
