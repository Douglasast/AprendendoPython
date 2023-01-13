print('Progressão Aritmética')
print('----' * 5)

PrimeiroTermo = int(input('primeiro termo: '))
UltimoTermo = int(input('ultimo termo: '))
razão = int(input('razão: '))

for c in range(PrimeiroTermo, UltimoTermo+1, razão):
    print(c)