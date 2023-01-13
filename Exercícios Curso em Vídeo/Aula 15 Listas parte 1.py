#Manipulação de listas
lista = ['banana', 'maça', 'uva', 'pessego']
print(lista)
print('')

print('Adicionando uma fruta nova à lista')
lista.append('manga')
print(lista)
print('')

print('Adicionando uma fruta nova na posição especifica da lista')
lista.insert(0,'carambola')
print(lista)
print('')

print('Para eliminar um item da lista:')
del lista[1]
print(lista)
print('')

print('apagando o terceiro item da lista')
lista.pop(2)
print(lista)
print('')

print('apagando o item pelo nome')
lista.remove('maça')
print(lista)
print('')

print('Substituindo item da lista')
lista[0] = 'cereja'
print(lista)
