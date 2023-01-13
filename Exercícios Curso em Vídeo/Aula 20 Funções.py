#exemplo de codigo repetitivo
print('='* 20)
print('FUNÇÕES PYTHON')
print('='* 20)
print('='* 20)
print('Cabeçalho')
print('='* 20)
print('='* 20)
print('CADASTRO')
print('='* 20)

print()

#definindo uma função para linha de destaque
def lin():
    print('=' * 15)


lin()
print('Funções python')
lin()
lin()
print('Cabeçalho')
lin()
lin()
print('Cadastro')
lin()

print()

#definindo uma função com parametro
def titulo(txt):
    print('=' * 15)
    print(txt)
    print('=' * 15)

titulo('Funções Python')
titulo('Cabeçalho')
titulo('Cadastro')

#criando uma função de soma
def soma(a,b):
    s = a + b
    print(s)


soma(9, 4)


#caso a soma seja maior do que dois numeros:
def soma(* num):
    s = 0
    for c in num:
        s += c
    print(f'Somando os valores {num} o total é: {s} ')

    


#criando uma função com parametro indefinido
def contador(*num):
    print(f'{len(num)} Números foram contabilizados')
    print(f'Os números do contador são:')
    for c in num:
        print(f'{c} ', end='')
    print()
    print(f'Em ordem crescente: {sorted(num)}')
    total = sum(num)
    print(f'O total é: {total}')

contador(2, 1, 3, 9, 5, 6, 7, 8, 4)

#criando uma lista como parametro de função
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] = lista[pos] * 2
        pos = pos + 1


valores = [1, 4, 5, 6, 3, 2, 8, 7, 9]
dobra(valores)
print(valores)