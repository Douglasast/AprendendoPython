r1 = float(input('primeira reta: '))
r2 = float(input('segunda reta: '))
r3 = float(input('terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2: 
    print('Essas retas podem formar um triângulo!')
else: 
    print('Essas retas não podem formar um triângulo!')