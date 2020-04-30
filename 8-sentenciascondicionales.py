#Las sentencias condicionales permiten ejecutar un bloque de codigo siempre y cuando se cumpla o no 
#una condicion.
#El primer ejemplo a revisar es la sentencia if

edad=17
M_edad=18

if edad >= M_edad:  #<----- la primer sentencia de condicion es if significa "si"
	print("\n")
	print("soy mayor de edad")  #<------ en caso de que no se cumpla la condicion el codigo no se ejecuta

else:
	print ("no eres mayor de edad")

print("\n")
print("siempre se imprime")


#tambien podemos realizar multiples evaluaciones
Edad2 = 22

if Edad2 <= 0:
	print("\n")
	print("no valido")

elif Edad2 >= 0 and Edad2 < 18:

	print("\n")
	print("eres un infante")
elif Edad2 >= 18 and Edad2 < 59:

	print("\n")
	print("eres un adulto")
else:

	print("\n")
	print("Eres tercera edad") # utilizamos esta estructura para multilples evaluaciones incluso usamos 
# and como operador de comparacion, el codigo evalua si el valor proporcionado entra dentro de las condiciones.

