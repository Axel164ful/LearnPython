#Itera sobre acada elemento de la lista y va evaluar segun una condicion asi los que cumplen 
#devuelven true de esta manera podemos filtrar datos.

def filtro (elemento):
	return (elemento>0)



l=[1,-3,.5,3,5]

Lr=filter(filtro,l)


print (l)

print (Lr)




