num=[]
print("Cual es la cantidad de números que vas a desear sacar su promedio?: ")
n=int(input())
i=0
while i<n:
    print("Dato",i+1)#esto es para hacer un listado de los datos hasta el número indicado(n) =dato 1, dato 2, dato 3...
    Dato=float(input())#aqui dejamos que puedan ser números decimales y se almacenan en la variable Dato
    num.append(Dato)
    i+=1
promedio=sum(num)/len(num) 
print("El promedio es: ",promedio)
#Explicación: El usuario tendrá que entrar una cantidad de ciertos 
#números para que el programa sepa cuantos datos van a hacer(num que 
#actúa como lista vacía) y poder operar, al ingresar la cantidad, se da 
#paso a integrar cada número por separado(Dato), estos serán 
#decimales(para datos precisos) , luego se repetirá el proceso 
#hasta completar la cantidad de números ingresados(num) y la 
#lista que antes estaba vacía se llenará con los datos ingresados 
#por el usuario, luego esa lista se sumará entre sí y se dividirá 
#en el valor del total de datos ingresados, por eso len, vuelve la 
#cantidad un número, ya que la formula del promedio es la suma de 
#los números dividida entre la cantidad de estos mismos.
#(Ejemplo: lista:2,3, son 2 datos, promedio=2+3/2)  