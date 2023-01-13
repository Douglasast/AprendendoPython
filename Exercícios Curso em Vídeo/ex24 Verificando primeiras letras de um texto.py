cidade = str(input('Digite o nome da sua cidade: ')).strip().lower()
teste = cidade.split()
print('A sua cidade começa com o nome Santo?')
print(teste[0] == "santo")

#Ou
#cidade = str(input("Digite o nome da sua cidade:"))
#print('A sua cidade começa com o nome Santo?')
#print(cidade[:5].lower() == "santo")


