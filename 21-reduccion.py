# La funcion reduce, permite reducir listas o ssecuencias a un solo elemento 
#toma elementos de dos en dos hasta acabar

t = ("h","o","l","a","_","m","u","n","d","o")


def  unir (a,b):
	return(a+b)


tr = reduce(unir,t)

print (type(tr))

print (tr)