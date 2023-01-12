from random import sample
a1 = str(input('primeiro aluno: '))
a2 = str(input('segundo aluno: '))
a3 = str(input('terceiro aluno '))
lista = [a1, a2, a3]
a1, a2, a3 = sample(lista, 3) 
print(f'o primeiro aluno é {a1}, o segundo é {a2} o terceiro é{a3}')