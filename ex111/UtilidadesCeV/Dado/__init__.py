def leiadinheiro(msg):
    while True:
        try:
            dinheiro = float((input('Digite o valor monetário: R$')).replace(',','.'))
        except (ValueError, TypeError):
            print('ERRO! você digitou o valor de forma incorreta.')
            continue
        except:
            continue
        else:
            return dinheiro
            