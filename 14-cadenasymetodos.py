

S = "hola mundo" ##-----tomemos un ejemplo


s.lent() #<--- permite saber la dimencion en caracteres de unacadena u objeto

s.count(valor, inicio, fin) #<--- permite contar el numero de veces que se repita determinado caracter 

s.lower() #<--- conbierte caracteres en minusculas

s.uperr() #<--- conbierte caracteres en mayusculas

s.replace(valor, nuevo, repeticiones) #permite reemplazar valores de alguna cadena por nuevos valores.
#el ultimo argumento indica el numero de veces que se repite el reemplazo

s.split(separador, maxsplit) # <--- permite dividir la cadena en sub cadenas cada que se encuentre el argumento separador
# pasa de ser una dadena a una tupla de cadenasm el ultimo argumento limita el numero de veces que se 
#repite la cadena.

s.find(valor, inicio, fin) #rfind() en reversa<--- busca cadena o caracter dentro de un objeto cadena 
#proporciona la ubicacion/indice del argumento buscado


t= ("a","b","c")
j:";"

j.join(t) #<---permite separar la tupla t en sus argumentos mediante el separadr j
