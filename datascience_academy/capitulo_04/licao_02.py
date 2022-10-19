from os import system
system('clear')

# fileName = input('Digite o nome do arquivo: ')

# fileName += ".txt"
# arquivo3 = open(fileName, "w") # w de write
# arquivo3.write("Testando no arquivo 3")
# arquivo3.close()
# arquivo3 = open(fileName, "r") # r de read
# print(arquivo3.read())
# arquivo3.close()

arquivo3 = open("estudando_python", "w")
arquivo3 = open("estudando_python", "a")
arquivo3.write("\n\n estou gostando disso")
arquivo3 = open("estudando_python", "r")
print(arquivo3.read())
arquivo3.close()