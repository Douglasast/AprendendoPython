def menu():
    lista = []
    dados = {}
    while True:
        print('')
        print('=======' * 5)
        print('   MENU PRINCIPAL   ')
        print('=======' * 5)
        print('1 - Ver pessoas cadastradas')
        print('2 - Cadastrar nova pessoa')
        print('3 - Sair do sistema')
        print('=======' * 5)
        opção = str(input('Sua Opção:'))
        if opção == '1':
            print('')
            print('Mostrando Cadastro:')
            print('')
            for pessoa in lista:
                print(f'{pessoa["nome"]}, {pessoa["idade"]} anos.')
                
        elif opção == '2':
            dados['nome'] = str(input('Nome:')).strip().capitalize()
            while True:
                try:
                    dados['idade'] = int(input('Idade:'))
                    if 1 > dados['idade'] or dados['idade'] > 115:
                        print('Erro, Idade inválida, digite novamente.')
                        continue
                except (ValueError, TypeError):
                    print('Houve um erro na digitação, tente novamente.')
                    continue
                else:
                    lista.append(dados.copy())
                    print('')
                    print(f'{dados["nome"]} de {dados["idade"]} anos foi cadastrado com sucesso')
                    dados.clear()
                    break
                    

        elif opção == '3':
            print('Fechando programa...')
            print('Fim.')
            break
        else:
            print('Opção inválida')


menu()

            
                    