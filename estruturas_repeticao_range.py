## Estrutura de Repetição ##

# RANGE

list(range(0, 4)) #vai retornar uma sequência [0, 1, 2, 3]

# Utilizando range com for

inicio = int(input('Digite o número inicial \n'))
for numero in range(inicio, 8):
    print(numero, end=', ') #lembrando que o end determina o "final" da "frase"
# são 11 casa com o início em "inicio"" (inclusivo) e fim em 7 (8 se torna exclusivo)
# ou seja, mesmo que eu inicie com um número negativo como "-3", irá de -3 até 8


print('\n')
tabuada = int(input('Insira o número que deseja saber a tabuada \n'))
print('Tabuada do:',tabuada, '\n')
for numero in range (tabuada, tabuada*10, tabuada):
    print(numero, end='\n')  
#número vai de 9 até 91 no 'passo 9' caso o a variável receba o valor 9    