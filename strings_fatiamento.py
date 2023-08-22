## Strings ##

# Fatiamento de strings

nome = 'Bruno Lucio Chagas'

print(nome[0]) #retorna a primeira letra da string
print(nome[-5]) #retorna a quinta letra de trás para frente
print(nome[:7]) #retorna string do início até o sétimo caractere 
print(nome[6:]) #retorna string a partir do sexto caractere até o fim
print(nome[12:17]) #retorna string da posição 12 até a posição 17
print(nome[5:18:2]) #retorna string da posição 5 até posição 18 no passo 2
print(nome[:]) #retorna toda a string
print(nome[::-1]) #retorna a string espelhada (escrita de trás para frente)

#Lembrar que sempre começa em 0 e termina com o último número sendo exclusivo
#Todo posição de caractere é contada, inclusive espaços vazios
