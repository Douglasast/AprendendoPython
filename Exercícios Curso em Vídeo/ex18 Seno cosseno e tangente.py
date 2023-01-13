from math import sin, cos, tan, radians
angulo = int(input('digite o angulo:'))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O angulo de {angulo}° possui seno = {seno:.2f}, cosseno = {cosseno:.2f} e tangente = {tangente:.2f} ')
#O Python usa Radiano para calcular as funções de seno, cosseno e tangente.