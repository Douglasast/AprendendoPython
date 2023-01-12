print('Analisador de Triângulos')
l1 = float(input('Primeiro lado: '))
l2 = float(input('Segundo lado: '))
l3 = float(input('Terceiro lado: '))
if l1 < l2 + l3 and l2 < l3 + l1 and l3 < l1 + l2:
    if l1 == l2 != l3 or l1 == l3 != l2 or l2 == l3 != l1:
        print('É um triângulo isóceles.')
    elif l1 == l2 == l3:
        print('É um triângulo equilatero')
    elif l1 != l2 != l3:
        print('É um triângulo escaleno')
else:
    print('Não é possivel formar um triângulo com esses valores')

