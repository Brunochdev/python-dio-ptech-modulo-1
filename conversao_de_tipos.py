##Conversão de Tipos

#int para float
preco = 35  #simplesmente declarando uma variável
print(preco)   #retorno dessa variável

preco = float(preco)   #transformando a variável int em float, chamando o tipo antes de declarar a variável
print(preco)

#float para int
preco = 35.9   #simplesmente declarando uma variável
print(preco)   #retorno dessa variável

preco = int(preco)   #transformando a variável float em int, chamando o tipo antes de declarar a variável
print(preco)

#numérico para string
preco, idade = 15.9, 27   #declarando duas variáveis na mesma linha
print(str(preco))   #retorno
print(str(idade))   #retorno

texto = f"idade {idade} preço {preco}"   #o "f" no começo da declaração, indica a inserção de variáveis
                                         #essas variáves devem estar dentro de "{}" para concatenar   
print(texto)

#string para número
preco, idade = '18.9', '21'   #declarando duas variáveis na mesma linha
print(float(preco))   #transformando a variável str em float, chamando o tipo antes de declarar a variável 
print(int(idade))   #transformando a variável str em int, chamando o tipo antes de declarar a variável 
print(float(preco)+int(idade))   #somando variável float+int, chamando o tipo antes das variáveis

##Conversão pro divisão
preco = 35
print(preco)
print(preco/2)   #retorna o número 17.5 (float)
print(preco//2)   #retorna o número 17 (int), pois quando a divisão é feita com dois sinais "//", retorna inteiro


##Erro de Conversão
#Não é possível                        
#preco = 'python'          ou         preco='19.9'
#print(float(preco))                  print(int(preco))
#pois a variável é uma frase, e não pode ser transformada em número ponto flutuante.
#                e o número 19.9 é float e não passa para int quando chamado assim.

