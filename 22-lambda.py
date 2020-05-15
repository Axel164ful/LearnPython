#Son funciones anonimas que solo se ejecutan en el momento de la creacion, se deben de ejecutar en una sola linea.
# permiten reducir lineas de codigo o ahorrar bits


li = [1.-2,1,-4]
lo = [5,3, 6]

s = "Hoola mundo"

ss = lambda n,m: n+m

print (map( ss, li, lo ))

print (filter (lambda n: n == 'o', s))

print (reduce(ss, lo))

print (ss(3,4))