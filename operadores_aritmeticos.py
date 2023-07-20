## Operadores Aritméticos

#Básicos
n1, n2 = 5, 2
print (n1+n2+7.9)
print (n1-n2)
print (n1*n2+2)
print (n1/n2)
print (n1//n2)

#Módulo
print (n1%n2)  #resto de divisão = 1

#Exponenciação
print (5**3)  #potência do primeiro número elevado ao segundo, ou seja: 5*5*5 = 125

#Precedência
x = (((9-8*(1+2))+(2**3)+4)/3)  #(3*-8)(+9+8+4)/3 -> (-24+21)/3 -> -3/3 = -1
print (x)