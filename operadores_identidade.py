#Operadores de Identidade
nome_sobrenome = 'Bruno Chagas'
nome_com_sobrenome = nome_sobrenome
idade, anos , ano_nascimento= 35, 35, 1987

print(nome_sobrenome is nome_com_sobrenome) #retorna true, pois, tem o mesmo valor string

print(anos is not ano_nascimento) #retorna true, pois, os valores numéricos das duas variáveis são diferentes

print(anos is idade) #retorna true, pois, os valores numéricos das duas variáveis são iguais