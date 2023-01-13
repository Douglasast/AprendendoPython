palavra = ('Aprender','Python',
            'Saitama', 'Legal', 
            'POO', 'Mettaton',
            'Substance', 'Constant',
            'Sombra', 'Entity',
            'Nudarlet', 'Dreams',
            'Asgore', 'Papyrus', 
            'Snowdin','Pindamonhangaba')
for c in range(0, len(palavra)):
    print(f'A palavra {palavra[c]} tem as vogais: ', end='')
    if 'a' in palavra[c].lower():
        print(' a', end='')
    if 'e' in palavra[c].lower():
        print(' e', end='')
    if 'i' in palavra[c].lower():
        print(' i', end='')
    if 'o' in palavra[c].lower():
        print(' o', end='')
    if 'u' in palavra[c].lower():
        print(' u',end='')
    print('')

#Repetindo letras 
palavra = ('Aprender','Python',
            'Saitama', 'Legal', 
            'POO', 'Mettaton',
            'Substance', 'Constant',
            'Sombra', 'Entity',
            'Nudarlet', 'Dreams',
            'Asgore', 'Papyrus', 
            'Snowdin','Pindamonhangaba')
for c in palavra:
    print(f'\nNa palavra {c} temos as vogais: ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(f'{letra} ', end='')



    