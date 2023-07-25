#Operadores de Associação
nome = 'Bruno Chagas'
estados = ['Paraná', 'São Paulo', 'Mato Grosso do Sul']
valor = 1000, 17, 12.6

print('Chagas' in nome) #retorna true, pois, a palavra está contida na string
print('bruno' in nome) #retorna false, pois, é case sensitive
print('Paulo' in estados) #retorna false (mas não entendi ainda o motivo, talvez por ser uma opção e não string)
print(12 in valor) #retorna false, pois não tem o mesmo valor numérico (falta .6)
print(12.6 in valor) #retorna true