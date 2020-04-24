# Los diccionarios son estructuras de datos que permiten mapear claves con 
#valores de de forma arbitraria (relacionar por ejemplo un valor a con un valor b)
#permiten guardar valores y acceder a ellos de forma ordenada y masiva


#Se pueden representar de la siguiente manera

Dicc = {	
	'Nombre' : "Atheris", 
	'Edad' : 55, 
	'Genero': "femenino", 
	'Padres': ["Gato", "Perro"] #<--- correcto aqui tenemos una lista 
	   }

#Midiccionario = {clave1:valor1, clave2 :valor2. clave3:valor3}

#una vez se tengan almacenados los datos podemos acceder a ellos
print("\n")
print (Dicc ['Nombre'])
print("\n")

# tambien podemos aceder a la informacion dentro de las listas
print("\n")
print (Dicc['Padres'] [1])
print("\n")

#Tambien podemos modificar el diccionario o agregar nuevas claves

print("\n")
Dicc['Muere']= "Si"
print(Dicc['Muere'])
print("\n")
# podemos hacer reemplazos de los metodos
#metodo
Dicc['Muere'] = 'no'
print("\n")
print(Dicc['Muere'])
print("\n")
#metodos de los diccionarios

#El método get() nos sirve para obtener por ejemplo el valor de 
#una clave determinada, entonces le indicamos al intérprete hey! 
#Muéstrame el valor de la clave ‘Nombre’ y nos lo imprimirá en 
#pantalla, veamos:


print(Dicc.get('Muere'))

#Método keys y values (Que en español se traduce como «Claves y Valores»)
#El método keys() nos servirá para imprimir solo las claves del diccionario!

CLAVES1 = Dicc.keys()

#Y el método value() nos permite imprimir solo los valores


