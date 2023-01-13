def notas(*num, sit=False):
    total = len(num)
    media = sum(num) / total
    for c, n in enumerate(num):
        menor = 0
        maior = 0
        if c == 1:
            menor = n
            maior = n
        else:
            if maior < n:
                maior = n
            if menor > n:
                menor = n
    situação = ''
    if media >= 7:
        situação = "BOA"
    elif 5 <= media < 7:
        situação = 'RAZOAVEL'
    elif media < 5:
        situação = 'RUIM'
    
    if sit == False:
        return f'Total: {total} , maior: {maior }, menor: {menor}, media: {media}'
    elif sit == True:
        return f'Total: {total} , maior: {maior }, menor: {menor}, media: {media}, situação: {situação}'


resp = notas(6, 8, 4, 2)
print(resp)

#Usando dicionario
def notas(*num, sit=False):
    dados = {}
    dados['total'] = len(num)
    dados['media'] = sum(num) / len(num)
    dados['maior'] = 0
    dados['menor'] = 0
    for c, v in enumerate(num):
        if c == 1:
            dados['menor'] = v
            dados['maior'] = v
        else:
            if dados['maior'] < v:
                dados['maior'] = v
            if dados['menor'] > v:
                dados['menor'] = v
    situação = ''
    if dados['media'] >= 7:
        situação = 'BOA'
    elif 5 <= dados['media'] < 7:
        situação = 'RAZOAVEL'
    elif dados['media'] < 5:
        situação = 'RUIM'

    if sit == False:
        return dados
    if sit == True:
        dados['situação'] = situação
        return dados

resp = notas(8, 9, 10, sit=True)
print(resp)


    