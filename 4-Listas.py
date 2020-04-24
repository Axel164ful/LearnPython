#las listas son recursos usados para almacenar de forma 
#ordenada los datos de cualquier tipo su forma es la siguiente

lista1= [0, "hola", 2.5, 5, ["tres", 55, 26]]

#la manera de mostrar una lista es la siguiente

print ("\n")
print (lista1[0])

#la manera de mostrar una lista dentro de otra lista es la siguiente

print ("\n")
print (lista1[4][1])

#Cambiar el contenido de una lista es tan sencillo como
# pueden ser varios elementos de la lista
lista1[1] = "hola modificado"

print ("\n")
print (lista1)

#para mostrar, llamar o modificar varios elementos de la lista 
# el primero y el segundo elemento son un rango el tercer elemento nes un intervarlo de salto
print ("\n")

print (lista1[1:3:1])

#tambien se puede hacer de manera inversa

lista2 = lista1

lista2 = lista1[-1]

print ("\n")
print (lista2[-1:-11:-1])