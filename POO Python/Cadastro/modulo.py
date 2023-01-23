def JuntarListas(lista1, lista2):
    if len(lista1) != len(lista2):
        raise Exception ('Erro, as listas não são do mesmo tamanho')
    else:
        lista = []
        dados= []
        for c in range(0, len(lista1)):
            dados.append(lista1[c])
            dados.append(lista2[c])
            lista.append(dados[:])
            dados.clear()
    return lista

def email():
    email = str(input('Digite seu email:')).strip()
    while not '@gmail.com' in email[len(email) - 10: len(email): 1]:
        print('Erro, digite um email válido')
        email = str(input('Digite seu email:')).strip()
    return email

def nome():
    nome = str(input('Digite seu nome:'))
    while True:
        vogais = 0
        for letra in nome:
            if letra in '123456789,.;/[{)}]<>:':
                print('Números e Simbolos não são aceitos. Nome inválido.')
                nome = str(input('Digite seu nome:'))
                continue
            if letra.lower() in 'aãeéiíoôuúyí':
                vogais = vogais + 1
        if vogais == 0:
            print('Erro, nome sem letras vogais.')
            nome = str(input('Digite seu nome:'))
            continue
        break
    return nome

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
                return cpf
            

teste = CPF()
print(teste)


            

        




    



        
    