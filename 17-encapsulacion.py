#La encapsulación es uno de los conceptos fundamentales de la programación orientada a objetos (OOP).
# Describe la idea de encapsular datos y los métodos que funcionan con datos dentro de una unidad. 
# Esto pone restricciones en el acceso a variables y métodos directamente 
# y puede evitar la modificación accidental de datos. Para evitar cambios accidentales,
# la variable de un objeto solo se puede cambiar mediante el método de un objeto.
# Ese tipo de variables se conocen como varibale privado.

class Prueba(object):
	def __init__(self):
		self.__privado = "soy privado" #<--- la nomenclatura en python indica que con dos guiones bajos seguidos
		# el atributo se convierte en privado. 
		self.publico = " soy publico"

	def getprivado(self):
		return self.__privado

	def setprivado(self, valor):
		self.__privado = valor  # <-- la forma de obtener el valor es mediante estas funciones pero 
		#solo es posible hacer dontro de su clase.




obj = Prueba()

#print(obj.publico)

#print(obj.__privado)  #<--- cuando intentamos hacer un llamado no nos es posible puesto que elmetodo quedo
#encapsulado


obj.setprivado("ya no soy privado")

print(obj.getprivado())

