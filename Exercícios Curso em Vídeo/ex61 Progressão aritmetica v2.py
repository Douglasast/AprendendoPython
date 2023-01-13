primeiro_termo = int(input('Digite o primeiro termo:'))
razão = int(input('Digite a Razão:'))
n = 2
print(f' 1° termo: {primeiro_termo}')
while n < 11:
    primeiro_termo = primeiro_termo + razão
    print(f'{n:2}° termo: {primeiro_termo}')
    n = n + 1
