DiasAlugado = int(input('Durante quantos dias o carro foi alugado?: '))
quilometragem = float(input('Quantos quilometros rodados?: '))
PreçoAluguel = DiasAlugado * 60
PreçoQuilometragem = quilometragem * 0.15
print(f'O carro foi alugado por {DiasAlugado} por R${PreçoAluguel:.2f}. Percorreu {quilometragem}Km por R${PreçoQuilometragem:.2f}. Com o custo total de R${PreçoAluguel + PreçoQuilometragem:.2f}')

