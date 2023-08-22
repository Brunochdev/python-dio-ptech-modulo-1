## Strings ##

# Strings de múltiplas linhas (Strings triplas)

nome = 'Bruno'
linguagem = 'python'

msg = f'''
    Olá, meu nome é {nome}.
Eu estou aprendendo {linguagem},
            e esse recurso da linguagem, permite retornar uma mensagem com diferentes recuos.     
'''

print(msg)

#aspas triplas irá retornar exatamente o que foi escrito e na formatação que está dentro das aspas


jogo1 = 'Chrono Trigger'
jogo2 = 'Earthbound'
jogo3 = 'Final Fantasy 6'

print (f'''

########### RPG's ###########

           SNES
       
    1 - {jogo1}
    2 - {jogo2}
    3 - {jogo3}

########### RPG's ###########                  


''')
#economiza muito espaço de código nesse caso, já que não usa "print" para cada linha