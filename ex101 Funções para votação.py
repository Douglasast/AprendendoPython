def voto():
    from datetime import date
    print('-----' * 5)
    nascimento = int(input('Em que ano você nasceu?: '))
    idade = date.today().year - nascimento
    if idade >= 18 and idade <= 70:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')
    elif 16 >= idade < 18 or idade > 70:
        print(f'Com {idade} anos: VOTO OPCIONAL.')
    elif idade <16:
        print(f'Com {idade} anos: VOTO NEGADO.')

voto()

#Usando return

def voto():
    from datetime import date
    print('-----' * 6)
    nascimento = int(input('Em que ano você nasceu?: '))
    idade = date.today().year - nascimento
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 70:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    elif 18 <= idade <= 70:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'

print(voto())



    