print ("Bienvenido usuario a sacar el mayor entre 3 numeros")
print()
#primero ingresar valores para comparacion

num1= input("Digita el primer numero: ")
num2= input("Dijita el segundo numero: ")
num3= input("Dijita el tercer numero: ")

##profe una cosa, la mala ortografia es porque aun no configuro teclado y solo uso el de ingles
#Ahora viene el codigo para la comparacion
#if= si esto es...
#elif= en caso que...
if num1>num2 and num1 >num3:
    print("El numero mayor es ",num1)
elif num2>num1 and num2>num3:
    print("El numero mayor es ",num2)
elif num3>num1 and num3>num2:
    print("El numero mayor es ",num3)

#en el caso de ser todos iguales se dira que no hay numero mayor.


elif num1==num2 and num1==num3:
    print("no hay numero mayor")
elif num2==num1 and num2==num3:
    print("no hay numero mayor ")
elif num3==num1 and num3==num2:
    print("no hay numero mayor ")