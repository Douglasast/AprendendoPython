def nome():
    try:
        nome = str(input('Digite seu nome:'))
    except:

        

def JuntarListas(lista1, lista2):
    if len(lista1) != len(lista2):
        raise Exception ('Erro, as listas não são do mesmo tamanho')
    else:
        lista = []
        dados= []
        for c in range(0, len(lista1)):
            dados.append(lista1[c])
            dados.append(lista2[c])
            lista.append(dados[:])
            dados.clear()
        return lista

        
    