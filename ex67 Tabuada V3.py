núm = int(input('Digite um número para ver sua tabuada: '))
confirm = 'sim'
while confirm in 'sim':
    for c in range(1,11):
        print(f'{núm} x {c:2} = {núm * c}')
    confirm = str(input('Deseja ver outro numero?: ')).lower()
    if confirm in 'sim':
        núm = int(input('Digite um número: '))
print('acabou')
#OU 

n = int(input('Digite um número para ver sua tabuada: '))
while True:
    for c in range(1,11):
        print(f'{n} x {c:2} = {n * c}')
    n = int(input('Digite um numero para ver sua tabuada: '))
    if n < 0:
        break

    