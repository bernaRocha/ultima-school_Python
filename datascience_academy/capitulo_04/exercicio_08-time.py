from os import system   
system('clear')

# Exercício 8 - Considere o código abaixo. Obtenha o mesmo resultado usando o pacote time. 
# Não conhece o pacote time? Pesquise!

####### Só funciona no interpretador Python
import datetime
print (datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))

from time import strftime
print(strftime("%d/%b/%Y %H:%M:%S"))
