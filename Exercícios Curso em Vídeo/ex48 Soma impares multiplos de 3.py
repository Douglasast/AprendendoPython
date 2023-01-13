print('Soma de impares multiplos de 3...')
fim = int(input("Até qual numero você quer somar?:"))
s = 0 
for c in range(0 ,fim + 1, 3):
    print(c)
    s = s + c
print(s)
