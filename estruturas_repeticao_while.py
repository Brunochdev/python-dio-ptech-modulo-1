## Estrutura de Repetição ##

# WHILE

while True: #enquanto a condição se sustentar, o bloco de comando será executado
    numero = int(input('Digite um número: '))
    if numero > 10:
        print('Esse número é maior que 10!')
        break #comando para parar o laço 
    
    else:
        if numero % 2 == 0:
            print('Esse número é par')
        else:
            print('Esse número é ímpar!') 


# Um segundo bloco de comando para testar o comando continue imprimindo apenas números pares 

for numero in range (numero, 11):
    if numero % 2 != 0:
        continue #comando para continuar o laço
    print(numero, end=', ')             