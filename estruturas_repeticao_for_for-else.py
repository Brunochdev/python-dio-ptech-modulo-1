## Estruturas de Repetição ##

# FOR

texto = input('Informe as siglas da capitais desejadas: ')
CAPITAIS = 'PRT'

for alfa in texto:
    if alfa.upper() in CAPITAIS: #irá procurar a partir das letras maiúsculas 'PRT' por causa do 'upper'
        print (alfa, end = ', ') #o retorno será tanto as letras iguais maiúsculas, como minúsculas
                                 #a ',' é usada como espaçamento

print () #após o loop imprime uma nova linha em branco 
print ('A linha acima foi pulada')         

#caso a resposta seja 'Sp, MT, pr', irá retornar 'p,T,p,r'
#caso não tenha nenhuma letra 'prt' não irá retornar nada

# FOR-ELSE

texto = input('Informe as siglas da capitais desejadas: ')
CAPITAIS = 'PRT'

for alfa in texto:
    if alfa.upper() in CAPITAIS: #irá procurar a partir das letras maiúsculas 'PRT' por causa do 'upper'
        print (alfa, end = ', ') #o retorno será tanto as letras iguais maiúsculas, como minúsculas
else:      
    print ()                           
    print ('Executa no final do laço') #executa no final do laço