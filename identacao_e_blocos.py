#Identação e Blocos

def maioridade(valor):
    idade = 19

    if idade >= valor:
        print ('Apto a dirigir!') #caso essa linha esteja um espaço para frente ou para trás, o código não funcionará
        print ('Dirija-se a auto escola mais próxima') #o mesmo vale para essa linha e qualquer uma do bloco "if"
    print('Tenha um bom dia!') #essa linha sempre será executada, pois, faz parte do método, e não da condição "if"
print('Olá, já temos o resultado da verificação') #essa linha será executada primeiro, pois, está no primeiro bloco/método
    

maioridade(18) #se o valor for > que a variável "idade", a condição não será satisfeita, executando apenas linhas 9, 10       