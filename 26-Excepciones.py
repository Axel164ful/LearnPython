#Las excepciones son errores detectados por Python durante la ejecución del programa

Print ("hola")

try:           #<--- la estructura basica de las excepciones es mediante los try except
	print (x)

except:  #<--- se le puede agregregar excepciones en especifico ejem TypeError= que solo funciona con 
#errores de tipo de cadena.
	print( "no existe" )
except ZeroDivisionError:
	print ("error al dividir")
finally:
	print ("me ejecuto pase lo que pase")
print ("si se pudo")  

#<--- tambien podemos crear nuestra propia excepcion requiere hederar de la clase exception


class Unerror(exception):
	def __init__(self, valor):
		self.valorError = valor
	def __str__ (self):
		print (" no se puede dividir entre 1 el numero ", self.valorError)

print ("hola")

d=5
n=1
try:
	if n==1
		raise Unerror(d)
except Unerror:
	print("se producio error")

print("adios")

