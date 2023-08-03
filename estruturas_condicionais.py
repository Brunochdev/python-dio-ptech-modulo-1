##Estruturas Condicionais

#Usando apenas "IF"

classificacao = 8
colocacao = int(input('Qual a colocação do time ao fim da primeira fase?'))

if colocacao <= 8: #sempre atentar para o uso de ":"
    print('Classificado a próxima fase!')

if colocacao > 8: #usar ":" sempre que abrir uma condição
    print('O time está eliminado!')

#Usando "IF-ELSE"

classificacao = 8
colocacao = int(input('Qual a colocação do time ao fim da primeira fase?'))

if colocacao <= 8:
    print('Classificado a próxima fase!')
else: #na condição "else" também é usado ":"
    print('O time está eliminado!')         
#foi feito o mesmo código, só que agora usando o "if=else" o que deixou ele menor e mais limpo (melhor compreensão)

#Usando "ELIF"

opcao = int(input('Qual foi o resultado do time? \n[1] Ganhou \n[2] Empatou \n[3] Perdeu \n'))

if opcao == 1:
    print('Avançou a próxima fase!') #executa se o resultado for = 1
elif opcao == 2: #"elif" tbm usa ":"
    print('Precisa fazer o segundo jogo!') #executa se o resultado for = 2
elif opcao == 3:
    print('O time está eliminado!') #executa se o resultado for = 3
else:
    SystemExit('Opção inválida!') #executa se o resultado for diferente de 1, 2 ou 3   

#pode usar quantos "elif" forem necessários para satisfazer a condição

