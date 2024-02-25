#vamos a sacar el factorial de un numero 
print("Este programa va a calcular el factorial del numero que desees poner")
print()
print("introduce el numero:")
#ahora el lugar para meter datos a la consola
numero= int(input("ingresa un numero: "))
#ahora el valor del factorial
factorial=1
#un dato para poder sumar y operar.
i=1
#toca agregar un bucle para multiplicar cada una de las sumas de la secuencia de 1 al numero mencionado /
while(i<=numero):
    factorial=factorial*i
    i=i+1
#por ultimo imprimir en consola.
print("El factorial del tu numero ",numero, " es ", factorial)


#Explicación: hay un bucle que va a hacer que una variable “i” hasta 
#ser igual que el numero que coloquemos “numero” va a operar de modo 
#que otra variable se multiplique cada que va sumando 1 a la 
#variable “i” hasta llegar al numero insertado(num) ya que un factorial 
#es la multiplicación de cada numero de 1 hasta el numero que 
#se desea(ejemplo 5!:1x2x3x4x5=120) 