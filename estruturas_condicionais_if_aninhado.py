## IF aninhado ##

saldo = 1000.0
limite1 = 500.0
limite2 = 1500.0
limite3 = 2500.0


opcao = int(input('Qual seu tipo de conta? \n[1]Universitária \n[2]Normal \n[3]Aposentado \n'))
if opcao == 1:
    operacao = int(input('Qual operação deseja realizar? \n[1]Verificar Saldo \n[2]Verificar Limite \n'))
    if operacao == 1:
        print(f'O valor em conta é: {saldo}')
    elif operacao == 2:
        print (f'O limite da conta é: {limite1}')

elif opcao == 2:
    operacao = int(input('Qual operação deseja realizar? \n[1]Verificar Saldo \n[2]Verificar Limite \n'))
    if operacao == 1:
        print(f'O valor em conta é: {saldo}')
    elif operacao == 2:
        print (f'O limite da conta é: {limite2}')

elif opcao == 3:
    operacao = int(input('Qual operação deseja realizar? \n[1]Verificar Saldo \n[2]Verificar Limite \n'))
    if operacao == 1:
        print(f'O valor em conta é: {saldo}')
    elif operacao == 2:
        print (f'O limite da conta é: {limite3}') 

else:
    print ('Opção inválida!')             
      
#A cada "elif" com identação igual ao primeiro if, é gerada uma nova escolha de caminho

#IF ternário
colocacao = int(input('Qual a colocação do time?'))

campeonato = 'Continua' if colocacao <= 8 else 'Não continua'
print(f'{campeonato} na competição')
#método mais simples quando apenas quer fazer uma comparação