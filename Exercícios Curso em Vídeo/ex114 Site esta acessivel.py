import urllib.request
try:
    site = urllib.request.urlopen('https://google.com')
except:
    print('O site não está acessivel')
else:
    print('Consegui acessar o site hehe')


#Com identificação do navegador para evitar confusão com bots:

import urllib.request

def conecta(host):
    try:
        url = host
        req = urllib.request.Request(url, headers={"*identificação aqui*"})
        urllib.request.urlopen(req)
        # o Request faz a identificação como browser perante o site e assim o acesso fica liberado.
    except:
        return False
    else:
        return True

# Programa principal
site = 'http://www.pudim.com.br'
conecta(site)
print(f'O site {site} está acessivel.' if conecta(site) else f'O site {site} NÃO está acessível.')