from os import system
system('clear')

# chave --> valor
# palavra --> significado
# topico --> conteúdo
# nome --> telefone
# cpf --> cadastro

dicionario = {'a': 1,
              'b': 2,
              'c': 3 }

print(dicionario) # {'a': 1, 'b': 2, 'c': 3}
print(dicionario['a']) # 1
print(dicionario['b']) # 2 
print(dicionario['c']) # 3
dicionario['d'] = 4
print(dicionario, type(dicionario)) # {'a': 1, 'b': 2, 'c': 3, 'd': 4} <class 'dict'>
print(dir(dict))
'''
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', 
'__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
 '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', 
 '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', 
 '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', 
 '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys',
  'pop', 'popitem', 'setdefault', 'update', 'values']
'''
print(dicionario.get('e')) # None
print(dicionario.get('e', 'erro')) # erro

print(dicionario.items()) # dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
print(dicionario.values()) # dict_values([1, 2, 3, 4])
print(dicionario.keys()) # dict_keys(['a', 'b', 'c', 'd'])

numero_caractere = {1: 'z', 2: 'x', 3: 'b'} 
print(numero_caractere) # {1: 'z', 2: 'x', 3: 'b'}
print(numero_caractere[1]) # z
print(numero_caractere[2]) # x

#### chaves são imutáveis, valores não

mutavel = {'lista': []}
print(mutavel) # {'lista': []}
mutavel['lista'].append('valor na lista')
print(mutavel) # {'lista': ['valor na lista']}
