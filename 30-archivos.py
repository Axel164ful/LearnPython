


f = open("ejemplo.txt", "W")#< --- la manera de abrir archivos es la siguiente



try:
	f open ('ejemplo.txt', 'w')  
except:
	print ('error')

f.write("hola es un archivo")#<--- permite escribir en un archivo

f.seek(2)# te recorre a la posicion del archivo

f.tell()# indica el numero de caracteres del archivo

f.writelines() #permite agregar cadenas de caracteres