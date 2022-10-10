from os import system
system('clear')

arq1 = open("arquivo1.txt", "r")
print(arq1.read())
print(arq1.tell())
print(arq1.seek(0,0))
print(arq1.read(10))

arq2 = open("arquivo1.txt", "w")
#print(arq2.read())
arq2.write("Testando uma nova função") # sobreescreveu oa frase anteior
arq2.close()
arq2 = open("arquivo1.txt", "r")
print(arq2.read())

arq2 = open("arquivo1.txt", "a") # a de append
arq2.write("mais uma frase")
arq2 = open("arquivo1.txt", "r")
print(arq2.read())
