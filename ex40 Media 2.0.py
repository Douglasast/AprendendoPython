n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a segunda nota: '))
media = (n1 + n2 + n3) / 3
if media >= 7:
    print('aprovado')
elif media >= 5 and media < 7: 
    print('em recuperação')
elif media < 5:
    print('REPROVADO')
