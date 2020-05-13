# L a funcion map forma parte de interacciones de orden superior
# permite reemplazar algunos ciclos para operar listas.
#La función map() La función incorporada (i.e no necesita importarse) map() ejecuta una función 
#sobre cada uno de los elementos de un iterador (generalmente una lista o tupla) y retorna un nuevo 
#iterador cuyos elementos son el resultado de dicha operación.

def operador(n,m):
	if n == None or m == None:
		return 0

	return n+m

l1=[1,2,3,4]

t1=(1,2,3)

R = map(operador,l1,t1)

print(l1)
print(t1)

print (R)
