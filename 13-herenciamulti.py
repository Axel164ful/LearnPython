
#La herencia en Python nos permite a los programadores crear una clase general primero y luego más 
#tarde crear clases más especializadas que re utilicen código de la clase general. 
#La herencia también nos permite escribir un código más limpio y legible.

class Clase:      
	def __init__(self, tiempo): 
		
		print("\n")

		self.tiempo = tiempo  

		

	def dialogo(self, mensaje):
		mensaje = mensaje 
		



#----------

class Ing(Clase):    #<----- primeramente la clase ingeniero hedera de la clase, Clase los metodos int y dialogo 
# al ejecutar Ing automaticamente se ejecuta ing y opcionalmente podemos ejecutar dialogo
	def programa(self, lenguaje):
		print("voy a trabajar en", lenguaje)


class Lic(Clase):
	def demanda(self, caso):
		print ("debo estudiar el caso ", caso)

objeto  = Ing(25)

objeto2 = Lic(22) 


#-----------------------------------------herencia multiple.

print( objeto.programa('python'))  #<-----primeramente utilizamos el metodo demanda de la clase Ing

print ("mi edad es", objeto.tiempo) # <---- de aqui estamos hederando el metodo init de Clase y usandolo en Ing

objeto2.demanda('de las drogas')


#<-------- herencia multiple consiste en hederar metodos de multiples clases en el ejemplo se hedera de 
#estudioso hedera los metodos ing y lic asi como lic hedera de clase
class Estudioso(Ing, Lic):
	pass  #<----- si solo se van a heredar metodos se usa esta funcion.

Axel = Estudioso('')#<---- estos dos metodos probienen de herencia multiple

Axel.programa('c++')

Axel.demanda('dalas')