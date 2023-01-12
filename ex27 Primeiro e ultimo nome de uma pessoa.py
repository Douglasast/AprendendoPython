nome = str(input('Digite seu nome: ')).strip()
ultimo = (nome.rfind(' ') + 1)
primeiro = nome.split() 
print('Seu primeiro nome é {} e seu ultimo nome é {}'.format(primeiro[0], nome[ultimo:]))

#OU para o ultimo nome:
#separado = nome.split()
#.format([len(separado) - 1])
### pos o len(separado) conta em quantas partes foi separado, - 1 para escolher a ultima com os []
