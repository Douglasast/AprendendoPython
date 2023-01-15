class Cliente:
    def __init__(self, nome, plano):
        self.nome = nome

        #Tratando Erro dentro de uma classe
        while True:
            try:
                email = str(input('Digite seu Email:'))
            except Exception (KeyboardInterrupt):
                print('Nada foi digitado')
                continue
            except:
                if '@gmail.com' not in email:
                    print('Email inválido.')
                    continue
            else: 
                print('Email aceito com sucesso.')
                break          
        self.email = email

        self.lista_planos = ['basic', 'premium']
        if plano in self.lista_planos: 
            self.plano = plano
        else:
            raise Exception('Plano inválido')

    def mudar_plano(self, novoplano):
        if novoplano in self.lista_planos:
            self.lista_planos = novoplano
            print('Plano alterado')
        else:
            print('Plano invalido')


cliente = Cliente('Douglas', 'basic')
print(cliente)

