from time import sleep
def contagem(inicio, fim, passos):
    print('-' * 20)
    print(f'Contagem de {inicio} a {fim} de {passos} em {passos}')
    if fim < inicio:
        for c in range(inicio, fim + 1, -passos):
            print(f'{c} ', end='', flush=True)
            sleep(0.5)
        print()
    else: 
        for c in range(inicio, fim + 1, passos):
            print(f'{c} ', end='', flush=True)
            sleep(0.5)
        print()
    print('-' * 20)

contagem(0, 10, 1)
contagem(10, 0 , 2)

print('Agora é sua vez de personalizar a Contagem.')
contagem(int(input('Inicio: ')), int(input('Fim: ')), int(input('Passos: ')))

#Usando While

from time import sleep
def contagem(inicio, fim, passos):
    print('-' * 20)
    print(f'Contagem de {inicio} a {fim} de {passos} em {passos}')
    if inicio < fim:
        count = inicio
        while count <= fim:
            print(f'{count} ', end='', flush=True)
            sleep(0.5)
            count = count + passos
        print()
    else:
        count = inicio
        while count >= fim:
            print(f'{count} ', end='', flush=True)
            sleep(0.5)
            count = count - passos
        print()
    print('-' * 20)
contagem(0, 10, 1)
contagem(10, 0 , 2)

print('Agora é sua vez de personalizar a Contagem.')
contagem(int(input('Inicio: ')), int(input('Fim: ')), int(input('Passos: ')))



