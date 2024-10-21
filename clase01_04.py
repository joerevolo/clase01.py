#operadores
print('el residuo de 7 % 4 es: ' , (7 % 4))
print('el residuo de 12 % 10 es: ' , (12 % 10))
print('divion entera de 24 //10  es: ' , (24 // 10))

'''
realizar un programa que ingrese 
un numero de 2 digitos y hallar el inverso 
y la suma de sus cifras 
'''
# print('La cifra de decenas ', (78//10))
# print('La cifra de decenas ', (78 %10))
print('===========================================')
xnum= int(input('ingresa un numero de 2 cifras: '))
c = xnum % 10
cd= xnum // 10 
print('El numero invertido es: ', (str(c)+ str(cd)))
print('La suma de las cifras: ', (c+cd) )