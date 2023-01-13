n1 = int(input('primeiro numero:'))
n2 = int(input('segundo numero: '))
n3 = int(input('terceiro numero:'))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f'o menor valor digitado foi {menor}')
maior = n2 
if n1 > n2 and n1 > n3:
    maior = n1
if n3 > n2 and n3 > n1:
    maior = n3
print(f'o maior numero digitado é {maior}')

# ou 
primeiro = int(input('Digite o primeiro número:'))
segundo = int(input('Digite o segundo número:'))
terceiro = int(input('Digite o terceiro número:'))
numeros = [primeiro, segundo, terceiro]

print('O maior valor digitado foi {}'.format(max(numeros)))
print('O menor numero digitado foi {}'.format(min(numeros)))

#ou colocar na ordem

n1 =int(input('digite o primeiro número:  '))
n2 =int(input('Digite o segundo número: '))
n3 =int(input ('Digite o terceiro número: '))

lista =[n1,n2,n3]
lista_ordenada = sorted(lista)

print('O menor número é {}'.format(lista_ordenada[0]))
print ('O maior número é {}'.format(lista_ordenada[2]))