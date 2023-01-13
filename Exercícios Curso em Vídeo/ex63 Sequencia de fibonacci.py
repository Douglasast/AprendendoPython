anterior = 0
atual = 1
soma = anterior + atual
termos = int(input('quantos termos você quer ver: '))
count = 1
while count <= termos:
    print(soma)
    anterior = atual
    atual = soma
    soma = anterior + atual
    count = count + 1

    