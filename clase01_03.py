#ingresar la edad
#int (integer) es una funcion que convierte a numero entero 
xedad =  int(input('Ingrese edad: '))
#float es una funcion que convierte a numero decimal
xdeuda = float(input('ingrese deuda: '))
xnota = int(input('ingrese nota final: '))
if (xedad >= 18):
    print('es mayor de edad')
else:
    print('es menor de edad')
#trabajando con la deuda
if (xdeuda<=1000):
    print('eres un deudor comun ')
else:
    if(xdeuda >1000 and xdeuda <=4000 ):
        print('deudor con notificion')
    else:
        print('deudor para embargar bienes ')

if (xdeuda<=1000):
    print('eres un deudor comun ')
elif(xdeuda >1000 and xdeuda <=4000 ):
        print('deudor con notificion')   
else:
    print('deudor para embargar bienes ')    
    




if (xnota >= 0 and xnota <= 20 ):
    print('Es una nota valida')   
else:
    print('Nota errada')        

#practica
xnum = int(input('ingrese un numero del 1 al 3: '))
if(xnum ==1):
    print('uno')
elif(xnum ==2):
    print('dos')
elif(xnum ==3):
    print('tres')
else:
    print('numero no valido')        

#practica2
numero = int(input("Ingrese un número entero: "))

# Verificar si el número tiene 2 cifras
if 10 <= abs(numero) < 100:
    # Calcular el inverso del número
    inverso = int(str(numero)[::-1])
    print(f"El inverso del número es: {inverso}")
else:
    # Calcular el triple del número
    triple = numero * 3
    print(f"El triple del número es: {triple}")







