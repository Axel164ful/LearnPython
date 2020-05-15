#una funcion decoradora es aquella que recibe una funcion y retorna 
#otra funcion 


def debug(j):  #<--- este es el codigo del decorador, recordar que debe ser una funcion con
# argumentos en otra funcion f representa a la funcion add
    def new_function(a, b):#<---- debe retomar otra funcion
        print("Function add() called!")
        return j(a, b)

    return new_function



#---------------
@debug  #<----  nuestro decorador  permite usar otra funcion cada que suma sea llamada 
#-------------
def add(a, b):  #<--- definir la funcion de suma
    return a + b   #<--- da como resultado el guardado de los valores a + b  




print( add(7, 5) )  #<--- cuando le doy argumentos primeramente manda a llamar la funcion debug



## los decoradores pueden ser metidos en clases de esta manera

def Decorador(funcion):
	def funcionDecorada(*args, **kwargs):
		print ("funcion ejecutada", funcion.__name__)
		return funcion(*args, **kwargs)
	return funcionDecorada
@Decorador
def resta (n+m):
	return n-m

print resta( 3 , 5 )
#####################################################
class Decorador(object):
	
	def __init__(self, funcion):
		self.funcion = funcion 
	def __call__(self, *args, *kwargs):#args y kwargs permiten recibir n cantidad de parametros
		print ("funcion ejecutada", self.funcion.__name__)
		self.funcion(*args, **kwargs)

@Decorador
def resta(n,m):
	print(n-m)