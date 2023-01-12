#Tratamento de erros com Python

try: #tenta realizar um script...
    numerador = int(input('numerador: '))
    denominador = int(input('Denominador: '))
    resultado = numerador / denominador
except: #caso ocorra uma exceção:
    print('Infelimente tivemos um erro.')

else: #caso de certo: (opcinal)
    print(f'O resultado é: {resultado}')

finally: #finalizando o tratamento. (opcional)
    print('Fim, Muito obrigado.')



#Criando uma variavel para receber o erro...

try:
    numerador = int(input('numerador: '))
    denominador = int(input('Denominador: '))
    resultado = numerador / denominador
except Exception as erro: #erro é a variavel que recebe o Erro.
    print(f'infelizmente tivemos um erro, {erro}')



#Também é possivel criar varios "except" para um unico "try"
try:
    numerador = int(input("Numerador: "))
    denominador = int(input("Denominador: "))
    resultado = numerador / denominador
except (ValueError, TypeError): 
    print('Erro, Houve um problema na digitação dos dados')
except ZeroDivisionError: 
    print('Erro, não existe divisão por zero, informe outro denominador.')
except KeyboardInterrupt:
    print('Erro, o usuario interrompeu o programa')
except:
    print('Infelizmente ocorreu um erro.')

