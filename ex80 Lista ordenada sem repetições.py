lista = []
for c in range(0,5):
    valor = int(input("Digite um valor:"))
    if c == 0 or valor > lista[-1]:
        lista.append(valor)
    else:
        p = 0
        while p < len(lista):
            if valor <= lista[p]:
                lista.insert(p, valor)
                break
            p = p + 1
print(lista)
     