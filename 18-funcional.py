# Al igual que la mayoría de lenguajes de programación nuestro código lo podemos
# estructurar en fragmentos que luego llamaremos en determinados puntos de nuestro código, estos 
# fragmentos de códigoreciben el nombre de funciones.

def f (x):
   return x+3  #<--- la funcion return regresa o almacena un determinado valor dentro o desde una funcion
 # si yo le doy un valor de 3 a x almacenara unicamente el resultado que es 6  



def g (fu, x):  #<--- esta funcion esta declarando una variable fu y hederando el valor del argumento x

   return fu (x) * fu (x) #<---fu almacena el valor de x dos veces y lo multiplica 


print(g (f,7)) #<--- asignamos valores a la funcion g fu toma el valor de la funcion f y x toma el valor 7


#la operacion almacena el valor de fu de acuerdo a la def de f la cual esta definida con 7+3 lo cual es 10
# posterior a eso lo reemplaza con el valor de funcion x que igual es 10 despues hace la operacion

def prueba (f):
	return f()  #<--- los parentesis indican que la funcion se esta ejecutando y debe regresar el valor


def mandar():
	return 2+2

print (prueba(mandar))


#----------------------------

def seleccion (operacion):
	def suma(n,m):
		return n+m


	def multiplicacion(n,m):
		return n*m

	if operacion == 'suma':
		return suma
	elif operacion =='multi':
		return multiplicacion #<--- el que no existan parentesis indica que regresara toda la funcion


eleccion = seleccion('suma')

print(eleccion(5,6))










