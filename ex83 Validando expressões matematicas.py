exp = str(input('Escreva uma expressão matematica: '))
pilha = []
for c in exp:
    if c == '(':
        pilha.append('c')
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print("Sua expressão está correta")
else:
    print('Sua expressão é invalida')