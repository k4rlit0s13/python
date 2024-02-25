#algoritmo para saber si un numero es primo python
#ingresar los datos 
num=int(input("introduce un numero: "))
#el numero que es primo debe ser divisible entre 1 y si mismo(num) por lo que se agrega 2 variables 1 y 0, resultados de las divisiones entre 1 y num
x=1
c=0
#ahora un bucle para operar
#si la division es exacta deveria dar 2
while x<=num:
    if num%x==0:
# c debe de dar 2 que quiere decir la cantidad de divisores que puede tener
        c=c+1
    x=x+1
if c==2:
    print("El numero ", num, " es primo")
else:
    print("El numero ", num, " no es primo")
#si se divide entre 2 digitos es primo si no, no lo es
    
#Explicación: hay un bucle que repetirá hasta que una variable en este 
#caso 1 sea mayor que el numero que coloquemos tendrá que generar una 
#condición de que otra variable sea igual a 2 osea la cantidad de divisibles 
#que pueda tener el numero entrado en consola generando así su conclusion 
#si es o no primo.