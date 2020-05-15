#Son funciones que nos permitirán obtener sus resultados poco a poco. Es decir, cada vez que llamemos #a la función nos darán un nuevo resultado. Por ejemplo, una función para generar todos los números #pares que cada vez que la llamemos nos devuelva el siguiente número par. ¿Podemos construir una #función que nos devuelva todos los números pares? Esto no es posible si no usamos generadores. Como #sabemos los números pares son infinitos

l =[1,2,3,4,5]

s = ["h","o","l","a"]

l2 = (c* num  for  c in s
					for num in l
						if num > 0 )


print (l)

print (l2.next)


print (l2.next)