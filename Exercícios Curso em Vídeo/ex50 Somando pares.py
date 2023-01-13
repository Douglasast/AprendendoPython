print('Somando apenas pares')
s = 0
for c in range(0,6):
    n = int(input('Digite um numero:'))
    if n % 2 == 0:
        s = s + n
print(f'A soma de todos os pares foi: {s}')
print('fim!')