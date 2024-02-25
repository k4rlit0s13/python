n=int(input("introduce el numero al que desees crear tabla de multiplicar: "))
for i in range(0,11):
    resultado=i*n
    print(n,"x",i,"=",resultado)
#Explicación: se pone una variable para que pueda ingresar 
#por consola, una variable que servirá del rango de 0 a 10 en 
#python se coloca desde 0 a 11 ya que toma lo que está dentro de
#ese rango colocandolos como puntos de cierre o paredes, tomará de 
#0 a 10, luego la variable resultado como operacion de la variable i mulplicada 
#por el número que se desea sacar la tabla, el rango repite todo hasta el 10, como
#se debe imprimir cada una de las operaciones, se usa una impresion que ayuda a 
#mostrar la operación y el resultado.