fatorial = int(input('Digite um número:'))
soma = fatorial
for count in range(fatorial - 1, 1, -1):
    soma = soma * count
print(soma)

#OU PREGUIÇA

from math import factorial
n = int(input('digite um numero:'))
print(factorial(n))

#OU WHILE

num = int(input('Digite um número: '))
fatorial = 1
while num > 0:
    fatorial = fatorial * num
    num = num - 1
print(fatorial)

