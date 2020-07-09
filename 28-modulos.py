#Un modulo es cualquier archivo que se creee en python, los poyectos grandes los puedes separar en  bloques.
#modulo principal, es donde se importan la mayoria de los otros modulos.
#la condicion es que los modulos esten en la misma carpeta.


import nombredemodulo #<--- de esta manera traemos codigo de otros modulos a python

e = nombredemodulo.ejemplo()

e.imprime()#<--- ejecutaria el hey  

m.fejemplo()#<--- ejecutaria el soy un ejemplo

from nombredemodulo import Ejemplo #<--- esto permite unicamente importar una sola funcion.

from nombredemodulo import * #<-------importa todas las funciones del modulo. (no tan recomendado.)










#<------------------------------supongamos que esto de aqui es un modulo en otro archivo.
class Ejemplo(object):
	"""docstring for Ejemplo"""
	def __init__(self):
		pass
	def imprime(self):
		print (hey)
def fejemplo():
	print("soy un ejemplo")
		
		