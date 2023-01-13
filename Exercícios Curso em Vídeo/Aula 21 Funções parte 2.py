#Criando uma Docstring
def contador(i,f,p):
    '''
    Faz uma contagem e mostra o numero na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    '''
    count = i
    while count <= f:
        print(f'{count} ', end='')
        count = count + p
    print('Fim')
contador(2,10,2)

help(contador)

#parametros opcionais != parametro indefinido
def soma(a=0, b=0, c=0):
    '''
    Soma de 0 à 3 valores e mostra o resultado na tela.
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    '''
    s = a + b + c
    print(f'A soma é: {s}')


#Escopo Local e Global de uma Variavel.
def teste():
    '''
    A função teste tem uma variavel x de escopo local,
    não podendo ser acessada fora da função.

    Caso seja declarado uma variavel n = *qlqr numero* dentro da função, será criado
    uma nova variavel de escopo local, sobresaindo a variavel n global

    Usando o comando:
    global *variavel*  é possivel alterar a variavel global quando a função for chamada

    '''
    
    
    x = 5
    print(f'A função teste mostra n = {n}')
    print(f'A função teste tem uma x = {x}')

n = 2
teste()
print('x')

#Retornando Valores
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s
r1 = somar(5, 4, 3)
r2 = somar(4, 9, 23)
r3 = somar(2, 8)
print(f'Os resultados são: {r1}, {r2} e {r3}')

#pratica
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1 ):
        f = f * c
    return f

f1 = fatorial(4)
f2 = fatorial(7)
f3 = fatorial(6)
print(f'Os resultados são: {f1}, {f2} e {f3}')

