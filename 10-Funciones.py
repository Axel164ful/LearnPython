# funcion es un fragmento de codigo al cual podemos referenciar para poder usarlo despues, contienen
# valores

def suma(num1, num2):  #<--- la funcion define dos variables
	print("\n")
	print (num1+num2)  #<----nuestra funcion ejecuta la suma de dos variables
	pass



a = int(input("dame un numero   "))  #<---aqui usamos un ejem de captura de datos
#se utiliza int(input()) para captura de datos tipo numericos

b = int(input("dame otro numero  ")) #<----utilizamos unicamente input() para captura de caracteres


suma(a,b) #<-- en la ultima parte del codigo  unicamente mandamos llamar la funcion

#tambien podemos mandar cadenas un numero determinado de veces en el ejemplo 

def cadena(cad, n = 5):
	print (cad * n)

cadena('cadena', 5)

# Si deceamos declarar variables conforme el programa queda de la siguiente manera

def ejemplo (va1, va2, *x):
	
