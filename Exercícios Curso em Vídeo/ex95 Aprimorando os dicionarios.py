jogador = {}
lista = []
while True:
    jogador['nome'] = str(input('Nome: ')).strip().capitalize()
    p_nome = jogador['nome'].split()
    jogos = int(input(f'Quantas partidas {p_nome[0]} jogou?: '))
    gols = []
    for c in range(0,jogos):
        gols.append(int(input(f'Quantos gols na partida {c + 1}?: ')))
    jogador['gols'] = gols
    jogador['total'] = sum(gols)
    lista.append(jogador.copy())
    jogador.clear()

    confirm = str(input('Quer continuar? [S/N]')).upper()
    while confirm not in 'SN':
        print('Erro! Digite apenas S ou N.')
        confirm = str(input('Quer continuar? [S/N]')).upper()
    if confirm == 'N':
        break

# tres modos de chamar dados de dicionarios em listas

#simples#varios prints para formatar
for c in range(0,len(lista)):
    print(f'Cod: {c + 1} ', end='')
    print(f'Nome: {lista[c]["nome"]} ', end='')
    print(f'Gols: {str(lista[c]["gols"]):<15} ', end='')
    print(f'Total: {lista[c]["total"]} ')
print('')
#valores
# for k, v in enumerate(lista):
    #O K é um contador, 0 1 2 3 4... ele escolhe o numero da lista, ex:lista[0]
    #O V é os valores da lista, tudo dentro de ex:lista[0]
    #O C é um contador, IN V.VALUES() ele funciona como um corte de cada dado da lista
    #mostrando o mesmo que lista[k][c] = nome depois lista[k][c]
    # for k, v in enumerate(lista):
    # print(f'cod: {k}')
    #   for c in v.values():
    #   print(f'{str(c)}')###
while True:
    busca = int(input('Qual jogador você quer buscar? [999 encerra]: '))
    if busca == 999:
        break
    if busca > len(lista):
        print('Erro!, esse jogador não existe.')
    else:
        print(f'levantamento dos dados do jogador {lista[busca - 1]["nome"]}')
        for i, g in enumerate(lista[busca - 1]["gols"]):
            print(f'Na partida {i+1} ele fez: {g} gols')








