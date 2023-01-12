#aprendendo a importar
#criando uma pasta com modulos e importando suas funções aqui.
from modulo_uteis import fatorial
num = int(input('Digite um numero: '))
resultado = fatorial(num)
print(f'O fatorial de {num} é {resultado}')