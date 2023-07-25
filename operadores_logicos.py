## Operadores Lógicos ##

#Operador "E" (and)
saldo = 1500
saque = 250
limite = 200

saldo >= saque and saque <= limite
#ira retornar false, pois a condição 'and' necessita que todas as comparações sejam verdadeiras


#Operador "OU" (or)
saldo = 1500
saque = 250
limite = 200

saldo >= saque or saque <= limite
#ira retornar true, pois a condição 'or' necessita que apenas uma das comparações sejam verdadeiras


#Operador "NÃO" (not)
not 1000 > 1500 #retorna true, pq o operador not está negando uma comparação com resultado false

not contatos_emergencia[] #retorna true, pois lista vazia em python é considerado false, e está sendo negado

not 'saque 1500' #retorna false, pois uma string tem valor verdadeiro

#Precedência de Comparação
saldo = 1000
saque = 250
limite = 100
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print (exp)
#passando a expressão acima escrita com uso de parenteses pra ajudar na compreensão
exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print (exp_2)
#fica claro que na expressão, apesar de o primeiro parenteses não retornar true por causa do limite ser menor que o saque 
#vai ser atendido a condição pois no segundo parenteses a condição é true, e o operador lógico empregado é "or"

