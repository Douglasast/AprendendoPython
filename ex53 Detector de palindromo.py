frase = str(input('Digite a frase: ')).lower().strip()
frase = frase.replace(' ', '')
inverso = ''
for letra in range(len(frase) -1, -1, -1 ):
    inverso = inverso + frase[letra]
if inverso == frase:
    print('palindromo')
else:
    print('nãolindromo')
    
   
