def nome():
    while True:
        vogais = 'aAáàãâeEéêiIíoOóôõuUúüyY'
        try:
            nome = input('Nome:')
        except (KeyboardInterrupt):
            print('Erro. Nada foi digitado.')
            continue
        else:
            if not nome.replace(" ", "").isalpha():
                print('Nome inválido. Só são permitidas letras.')
                continue
            if not any(letra in vogais for letra in nome):
                print('Erro, nome sem letras vogais.')
                continue
            break
    return nome

def idade():
    while True:
        try:
            idade = int(input('Idade:'))
        except (TypeError, ValueError):
            print('Erro, Digite apenas números.')
            continue
        except (KeyboardInterrupt):
            print('Erro. Nada foi digitado.')
            continue
        else:
            if 1 > idade or idade > 115:
                print('Digite uma idade válida.')
                continue
            else:
                break
    return idade

def CPF():
    cpf = 0
    while True:
        try:
            cpf = int(input('Digite seu CPF (Apenas Números):'))
        except (TypeError, ValueError):
            print('Erro, Digite apenas números.')
            continue
        except (KeyboardInterrupt):
            print('Erro. Nada foi digitado.')
            continue
        except:
            print('Ocorreu um Erro.')
        else:
            if len(str(cpf)) != 11:
                print('Erro, seu CPF não possui 11 dígitos.')
                continue
            else:
                break
    return cpf

def email():
    email = str(input('Email:')).strip()
    while not '@gmail.com' in email[len(email) - 10: len(email): 1]:
        print("Erro, digite um email válido")
        email = str(input('Digite o Email:')).strip()
    return email