velocidade = int(input('Qual a velocidade atual do carro?:'))
if velocidade < 80:
    print('Tenha um bom dia! dirija com segurança.')
else: 
    print(f'Multado! você excedeu o limite de velocidade de 80km/h. Você pagará uma multa de {(velocidade - 80) * 7} reais') 