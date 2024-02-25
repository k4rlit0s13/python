n=int(input("Por favor ingresa un numero mayor a 1 para ver hasta que ciclo deseas conocer: "))
a=0#creamos 3 variables con los números 0,1 y 1 ya que con estos son los primeros en toda la serie y su uso es primordial
b=1
c=1
while c<=n:#cuando la variable c sea menor o igual al número metido por consola se toman 2 caminos
    if c%2==1:#si la división entre c(1) y 2 sea igual a 1
        print(a,end=" , ")#se mostrará el valor 0 seguido de comas y hasta donde llega n
        a=a+b#este define cada número despues del 0
    else:#sino pasa esto osea que si c ya es igual a n...
        print(b,end=" , ")#se imprime hasta el último valor que se deja 
        b=b+a
    c=c+1