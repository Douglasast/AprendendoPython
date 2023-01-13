from time import sleep
nome = str(input('Digite seu nome completo: ')).strip()
PrimeiroNome = nome.split()
print('analisando seu nome...')
sleep(1)
print(f'Seu nome em maiusculas é {nome.upper()}.')
print(f'Seu nome em minusculas é {nome.lower()}.')
print(f'Seu nome ao todo tem {len(nome) - nome.count(" ")} letras.')
print(f'Seu primeiro nome é {PrimeiroNome[0].capitalize()} e ele tem {len(PrimeiroNome[0])} letras.' )
