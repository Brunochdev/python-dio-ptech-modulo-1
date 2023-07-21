##Operadores de Atribuição##

#Atribuição Simples
saldo = 500  #apenas indicando o valor da variável
print(saldo)

#Atribuição com operadores aritméticos
saldo, gasto, saldo_multiplicado, saldo_modulo = 50, 25, 27, 500 #posso chamar as duas variáves juntas
saldo += 13.5  #não posso inserir o valor da variável gasto na mesma linha de saldo para fazer a soma, mesmo se usar mesmo sinal
gasto -= 10 
saldo_multiplicado *= 2  #possível utilizar em situações com multiplicação e subtração tambem
saldo_modulo %= 201  #útil para útilizar com módulo
print (saldo)  #foi somado o valor das duas variáveis com o mesmo nome
print (gasto)  #do mesmo modo foi somado as duas variáveis com mesmo nome, mesmo com o valor negativo
print (saldo_multiplicado)
print (saldo_modulo)

saldo_exponencial = 3  #lembre-se que é sempre possível fazer a chamada tranquilamente após um bloco 
saldo_exponencial **= 4
print (f'O saldo exponencial será de: {saldo_exponencial}') #frase + "f" para chamar variável entre colchetes