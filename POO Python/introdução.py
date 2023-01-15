class Personagem:
    def __init__(self, nome, idade, sexo, personalidade, fala=''):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.personalidade = personalidade
        self.fala = fala
    
    def falar(self):
        print(self.fala)

willow = Personagem('Willow', 19, 'Feminino', 'Flamejante', 'Eu gosto de fogo.')
personagem2 = Personagem('Codsworth', 210, 'Masculino', 'Sistemático' )
personagem3 = Personagem('Reko', 23, 'Feminino', 'Explosiva' )


willow.falar()

