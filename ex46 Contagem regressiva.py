from time import sleep
inicio = int(input('Escolha um numero para uma contagem regressiva: '))
for c in range(inicio, 0, -1):
    sleep(1)
    print(c)
print('BOOM')
    
    