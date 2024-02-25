#sabemos que un numero es par cuando la resta de la division es igual a 0  entonces la operacion es una vasiable dividida entre 2 =0
num=int(input("ingresa un numero para saber si es par o impar: "))
if num % 2 ==0:
    print("Este numero es par, prueba otro numero")
else: 
    print("no es par")
#Explicación, para saber si un numero es impar podemos 
#usar la formula de dividirlo entre 2 para saber que si 
#la resta de la division es igual a 0 concluiremos que es 
#par de lo contrario sera impar lo cual buscamos obtener 