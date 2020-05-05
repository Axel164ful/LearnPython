#<----Inicio de la programacion orientada a objetos
#Paradigma de programacion en la que utilizamos objetos e interaciones para desarrollo


#<---objeto en programacion orientada objetos tiene caracteristicas y funciones.

#Objeto: Se trata de un ente abstracto usado en programación que permite separar los diferentes 
#componentes de un programa, simplificando así su elaboración, depuración y posteriores mejoras. 
#Los objetos integran, a diferencia de los métodos procedurales, tanto los procedimientos como 
#las variables y datos referentes al objeto. Las acciones que realiza el objeto se conocen como metodos.

# la clase es una plantilla o un molde de nuestro objeto, establecemos atributos y metodos.

class Clase:      #<-------- esto es una clase  dentro de ella establecemos los atributos y metodos
	def __init__(self, tiempo):  #<---El archivo __init__.py se utiliza para realizar configuraciones de importación. Algo que se utiliza mucho en este archivo es la importación de clases, funciones, etc, para que puedan ser utilizadas en otros paquetes.
		# self es unicamente una convencion elf indica que la función requerirá de los atributos contenidos en la clase
		print("\n")

		self.tiempo = tiempo  #<--- aqui estamos definiendo un atributo en el objeto

		print ("soy un objeto")

	def dialogo(self, mensaje):
 		
		print("\n")
		print ("mensaje1")









objeto  = Clase(1) #<--- creacion de objeto con la platilla de la clase hunano
objeto2 = Clase(2) 

print( objeto.tiempo )

print(objeto2.tiempo )  #---- dos onjetos herederos del mismo metodo con diferentes atributos.


objeto.dialogo("")  #<--- se utiliza el operador punto para poder acceder a el metodo del objeto o clase

#print( objeto.tiempo) #<--- asi podemos llamar un atributo dentro de la clase para cualquier fin

#-----------------------------------------





