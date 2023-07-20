nome = input ('Informe seu nome: ')  #input lê o dado de entrada(teclado) e atribui a variável
print (nome) #exibe o que foi "inputado" na variável

nome = input ('Informe o seu nome: ')
sobrenome = input ('Informe seu sobrenome: ')
idade = input ('Informe sua idade: ')
print(nome, sobrenome, idade)  #pula a linha por padrão
print(nome, sobrenome, end=' - continua - ')  #por padrão pula a linha de código, mas é possível terminar diferente sem pular
print(nome, sobrenome, end='...\n')  #indica pelo parâmetro "end" que finaliza com "...", e o "\n" é parâmetro pula a linha 
print(nome, sobrenome, idade, sep='#')  #"sep" é parâmetro de separação, que por padrão é um espaço vazio