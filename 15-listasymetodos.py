

lista[1, "dos", "tres", 4, 5]

busca = 4  

busca in lista #<--- de esta manera buscamos informacion dentro de una lista 
#si es correcto regresa true.

lista.index(busca) #<--- buscas el indice de algun elemento de una lista, de 
#debes confirmar que si exite por ejemplo asi

if busca in lista:
	print(lista.index(busca))
else:
	print("no esta lo que buscas")


lista.append("nuevo")# <--- permite reemplazar un elemento de la lista

lista.count("argumento") #<--- permite contar elementos de la lista

lista.insert(posicion, nuevo)#<---´permite reemplazar un argumento en especifico de la lista. 

lista.extend()#<---transforma la lista en este caso permite agregar mas elementos a la lista 

lista.pop()#<--- elimina un elemento de la lista  y lo extrae para almacenar

lista.remove()#<--- Simplemente elimina un elemento de la lista.

lista.reverse()#<--- invierte cada uno de los elementos de la lista.