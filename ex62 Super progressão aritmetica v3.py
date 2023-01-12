primeiro_termo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
n = 2
mais = 10
print(f'1° termo: {primeiro_termo}')
while n <= mais:
    primeiro_termo = primeiro_termo + razão
    print(f'{n}° termo: {primeiro_termo}')
    n = n + 1
    if mais + 1 == n:
        opção = str(input('Quer ver mais 10 termos?: [sim/não]')).lower()
        if opção in 'sim':
            mais = mais + 10
