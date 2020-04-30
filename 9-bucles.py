#Permiten ejecutar bloques de codigo de manera ciclica o repetitiva hastq que se cumpla
#una condicion

condicion = 0

while condicion <= 35:     #<------ garantiza la repeticion del ciclo hasta cumplir condicion

	if condicion == 10:    #<------  dentro del ciclo tambien es posible meter condiciones de tipo if
		condicion = condicion + 1
		continue           #<------ sirve para saltar ejecucion de codigo tambien existe -->break

	print ("la condicion" + str (condicion))

	condicion = condicion + 1

# El segundo ciclo es el for---- in  para recorrer listas tuplas, diccionarios y caracteres

lista = ['elem1', 'elem2', 'elem3', 'elem4']

for variable in lista:  #variable es una variable temporal solo aplicable para el ciclo
	
	print("\n")
	print (variable)

	if variable == "elem2":
		lista[1] = "modificado"
		print("\n")
		print(lista[1])        #permite modificar elementos dentro de las listas a travez de un ciclo
	

