## Strings ##

# Maiúsculo, minúsculo, inicio

nome = 'bRunO cHagAs'

print(nome.upper())#todo o nome sera convertido para apenas letras maiúsculas

print(nome.lower())#todo o nome sera convertido para apenas letras minúsculas

print(nome.title())#Somente o começo da palavra será maiúsculo, nesse caso tanto o nome como o sobrenome


# Eliminar espaços em branco

jogo = '       Chrono Trigger   '

print(jogo.strip())#será retirado os "espaços" da string, menos o que separa o nome "Chrono" de "Trigger"

print(jogo.lstrip())#será retirado os "espaços" da string, menos o que separa o nome "Chrono" de "Trigger" e o da esquerda

print(jogo.rstrip())#será retirado os "espaços" da string, menos o que separa o nome "Chrono" de "Trigger" e o da direita

# Junções e centralização

var = 'Bound'

print(var.center(10, '0'))#atribui um tamanho para a string, o primeiro argumento tamanho e o segundo é o tipo de espaçamento
#o primeiro argumento diz respeito ao tamanho da string, e o segundo qual o seu início e fim nesse caso
print('#'.join(var))#introduz um tipo de caractere entre todas as letras da palavra declaraca na variável
#tanto no primeiro como no segundo caso, pode ser inserido qualquer caractere, inclusive letras e números e não apenas sinais











