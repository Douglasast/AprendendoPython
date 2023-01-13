print('Descobrindo numeros primos em um intervalo')
print('')
inicio = int(input("Qual o primeiro número do intervalo?:"))
fim = int(input('Qual o ultimo número do intervalo?:'))
soma = 0
for n in range(inicio, fim+1):
    for c in range(2, n):
        if n % c == 0:
            soma = soma + 1
    if soma == 0:
        print(n)
    soma = 0
    


