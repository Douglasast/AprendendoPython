class Cliente:
    def __init__(self, nome, email, plano):

        #testando tratamento de erro dentro de uma classe
        while nome.isalpha() is False:
            nome = str(input('Erro, Digite o Nome novamente:'))
        self.nome = nome

        while True:
            if '@gmail.com' not in email:
                print('Email inválido.')
                email = str(input('Digite seu email: '))
                if '@gmail.com' in email:
                    print('Email aceito com sucesso.')
            else:
                break
        self.email = email

        self.lista_planos = ['basic', 'premium']
        if plano in self.lista_planos: 
            self.plano = plano
        else:
            raise Exception('Plano inválido')

    def mudar_plano(self, novoplano):
        if novoplano in self.lista_planos:
            self.plano = novoplano
            print('Plano alterado')
        else:
            print('Plano inválido')


cliente = Cliente('Douglas9','douglas@gmail.com', 'basic')
print(cliente.plano)
cliente.mudar_plano('blablabla')
print(cliente.plano)
cliente.mudar_plano('premium')
print(cliente.plano)

