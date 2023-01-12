frase = 'Curso em Video Python'
print('fatiando string')
print(frase[4:8:2])

print('fatiando string')
print(frase[4:])

print('contando as letras da string')
print(len(frase))

print('contagem de letra/word especifica')
print(frase.count("o",5))

print('encontrando uma palavra na string')
print(frase.find('Py'))

print('substituindo uma palavra na string')
print(frase.replace('Python','sem som'))

print('Colocando todas as letras em Maiusculas')
print(frase.upper())

print('Tranformando as letras em minusculas')
print(frase.lower())

print('deixando apenas a primeira letra maiuscula')
print(frase.capitalize())

print('Transformando todas as letras iniciais das palavras em maiusculas')
print(frase.title())

print('Apaga os espaços nas bordas')
print(frase.strip())

print('Apaga os espaços na borda direita')
print(frase.rstrip())

print('Apaga os espaços na borda esquerda')
print(frase.lstrip())

print('transforma cada palavra em uma string separada')
print(frase.split())

print('-'.join(frase))
print(frase.split() , "-".join(frase))


