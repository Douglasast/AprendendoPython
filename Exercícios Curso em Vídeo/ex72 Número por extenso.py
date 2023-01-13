tupla = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
número = int(input('Digite um número de 0 à 20 para ver seu nome por extenso:'))
while 0 > número or número > 20:
    print('Erro, número inválido!')
    número = int(input('Digite um número de 0 à 20:'))
print(f'Você digitou o número {tupla[número-1]}')
