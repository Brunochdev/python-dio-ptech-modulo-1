## Strings ##

# Interpolação de variáveis

# Old Style %

nome = 'Bruno Chagas'
idade = 35
profissao = 'engenheiro civil'
linguagem = 'python'

print ('Olá, me chamo %s, tenho %d anos de idade e sou %s de formação. Estou migrando para a área da tecnologia, '
       '\ne gostaria de aprender análise de dados com o uso de %s.' %(nome, idade, profissao, linguagem)) 
#este método de declaração não é mais usual
#usa-se o argumento ao fim da frase "%" e as variáveis em ordem

# Método Format

nome = 'Bruno Chagas'
idade = 35
profissao = 'engenheiro civil'
linguagem = 'python'

dados = {'nome': 'Bruno', 'idade': '35','profissao': 'engenheiro civil', 'linguagem': 'python'}

print ('Olá, me chamo {}, tenho {} anos de idade e sou {} de formação. Estou migrando para a área da tecnologia, '
       '\ne gostaria de aprender análise de dados com o uso de {}.'.format(nome, idade, profissao, linguagem))
#o método format nem apresenta tanta vantagem assim em relação ao "%", já que fica difícil identificar em frases maiores
print ('Olá, me chamo {3}, tenho {2} anos de idade e sou {1} de formação. Estou migrando para a área da tecnologia, '
       '\ne gostaria de aprender análise de dados com o uso de {0}.'.format(linguagem, profissao, idade, nome))
#tem uma vantagem já que é possível ordenar a posição da variável dentro do colchetes através de um índice
print ('Olá, me chamo {name}, tenho {age} anos de idade e sou {work} de formação. Estou migrando para a área da tecnologia, '
       '\ne gostaria de aprender análise de dados com o uso de {language}.'.format(language=linguagem, work=profissao, age=idade, name=nome))
#nesse exemplo precisa declarar o identificador com a variável
print ('Olá, me chamo {nome}, tenho {idade} anos de idade e sou {profissao} de formação. Estou migrando para a área da tecnologia, '
       '\ne gostaria de aprender análise de dados com o uso de {linguagem}.'.format(**dados))
#nesse exemplo precisa declarar um identificador completo com todos os dados


# Método f-string

nome = 'Bruno Chagas'
idade = 35
profissao = 'engenheiro civil'
linguagem = 'python'

print (f'Olá, me chamo {nome}, tenho {idade} anos de idade e sou {profissao} de formação. Estou migrando para a área da tecnologia, '
       f'\ne gostaria de aprender análise de dados com o uso de {linguagem}.')
#usando o "f" de "format", as variáveis são declaradas conforme a chamada

# Formatar strings com f-string

numero = 3.14159

print (f'O valor de PI é: {numero:.2f}')
#será imprimido apenas duas casas do valor da variável
print (f'O valor de PI é: {numero:10.2f}')
#será imprimido apenas duas casas do valor da variável, mas nesse caso com espaçamento de 10 casas