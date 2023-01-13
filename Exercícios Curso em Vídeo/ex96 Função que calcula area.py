#1
def area(largura, comprimento):
    a = largura * comprimento
    print(f'A Área de um terreno {largura}x{comprimento} é de {a}m²')


area(int(input('Largura (m): ')), int(input('Comprimento (m): ')))

#2
def area():
    largura = float(input("Largura (m): "))
    comprimento = float(input('Comprimento (m): '))
    a = comprimento * largura
    print(f'A Área de um terreno {largura}x{comprimento} é de {a}m²')


area()

#3
def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m²')


l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l,c)