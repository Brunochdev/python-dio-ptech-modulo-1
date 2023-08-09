## Estrutura de Repetição ##

# RANGE

list(range(0, 4)) #vai retornar uma sequência [0, 1, 2, 3]

# Utilizando range com for

for numero in range(-3, 8):
    print(numero, end=', ') #lembrando que o end determina o "final" da "frase"
# são 11 casa com o início em -3 (inclusivo) e fim em 7 (8 se torna exclusivo)


print('\n')
print('Tabuada do 9: \n')
for numero in range (9, 91, 9):
    print(numero, end='\n')  
#número vai de 9 até 91 no 'passo 9'     