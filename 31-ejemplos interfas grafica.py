#para interfaces graficas conmenzamos con TKinter
#Lo primero que debemos hacer al igual que con otros módulos, es que debemos importarlo para 
#poder comenzar a utilizarlo, y al igual que con otros módulos no hay una sola forma de hacerlo

#la forma correcta es from tkinter import *

try:
	from tkinter import *
except ImportError :
	raise ImportError("Se requiere modulo Tkinter")




ventana = Tk()  #Instacio objeto llamado ventana y le guardo el valor de tk para uso futuro

ventana.geometry('480x360') # permite dimencionar la ventana a un tamaño de inicio defecto

ventana.title("Primera vez") # dentro del objeto ventana en la variable titulo, guardamos la 
# cadena de texto para mostrarla en la parte superior.





#-----> ahora vamos a agregar una etiqueta

etiqueta = Label(ventana, text = "Etiqueta", font =("comic sans", 18)) #<--- funcion que permite la 
# entrada de una etiqueta dentro del grafico
etiqueta.grid(column=0, row=0) # sin esta funcion la etique no saldria es indispensable




# ---->  usaremos entrada de datos a tkinter
texto1 = Entry(ventana, width= 10)
texto1.grid(column= 3, row = 3)
texto1.focus()# --- permite que el apuntador de texto funcione directamente 
# tambien se puede des habilitar el texto con txt = Entry(window,width=10, state='disabled')




####ahora agregaremos un boton de prueba

def Respuesta(): #<--- esta es la funcion de respuesta configurada.
	etiqueta = Label(ventana, text = "Cambio  " + texto1.get() , font =("comic sans", 18))
	etiqueta.grid(column=0, row=2)
# la funcion get permite obtener los valores de entry

boton= Button(ventana, text="tocame", font =("comic sans", 18), bg="beige", fg="black", command=Respuesta) #permite llamar una funcion que crea el boton se puede modificar color y fuente
# dentro de nuestro boton comand nos permite o nos regresa un 0 y cuando se toca nos regresa 1 si es tocado nos permite 
# configurar una respuesta que debe ser traida mediante una funcion
boton.grid(column=2, row=0) #<----la estructura es similar a la de la etiqueta.
#al boton le podemos poner un evento cuando se cliquea.



#<--- Ejemplo de widget comb-box
from tkinter.ttk import *  #<----permite importar las opociones requeridas

cajacombo = Combobox(ventana) #creas un objeto que permite manipular la ventana
cajacombo['values']= (1,2,3,4,5, "text") #<--- cras una tupla con  los valores de la caja
cajacombo.current(1) #set the selected item
cajacombo.grid(column=3, row=0) #funcion de posicion 


#  widget Checkbutton

chk_state = BooleanVar()#---- Establece estado de boton checar
#chk_state = IntVar()
#chk_state.set(0) #uncheck
#chk_state.set(1) #check<---- respuesta similar. 

checar= Checkbutton(ventana, text="visto", var=chk_state)
checar.grid(column= 3, row = 6)



# <----  selector de radio

radio = Radiobutton(ventana, text= "uno" , value= 1)
radio2 = Radiobutton(ventana, text= "dos" , value= 2)
radio3 = Radiobutton(ventana, text= "tres" , value= 3)

radio.grid(column= 4, row=0)

radio2.grid(column=5, row=0)

radio3.grid(column=6, row=0)
# Para obtener un valor del radio button se puede utilizr el sig comando
# rad1 = Radiobutton(window,text='First', value=1, variable=selected)



#----> Adicionar un widget ScrolledText (Tkinter textarea)


from tkinter import scrolledtext

barratexto =  scrolledtext.ScrolledText(ventana, width = 40, height= 10)

barratexto.grid(column = 7, row = 7)





#------> caja de mensajes
from tkinter import messagebox

def botonazo():
	 messagebox.showinfo('pito', 'esto es un mensaje') 


botonsz = Button(ventana, text="button", command=botonazo)
botonsz.grid(column= 3, row =8)
# messagebox.showwarning('Message title', 'Message content')  <<<---shows warning message

# messagebox.showerror('Message title', 'Message content')    <<<---shows error message
 #Mostrar diálogos de pregunta-respuesta

#from tkinter import messagebox
# res = messagebox.askquestion('Message title','Message content')
#res = messagebox.askyesno('Message title','Message content')
#res = messagebox.askyesnocancel('Message title','Message content')
#res = messagebox.askokcancel('Message title','Message content')
#res = messagebox.askretrycancel('Message title','Message content')


#------------------------------------------------------------------------

#Agregar un SpinBox (widget de números)

giro = Spinbox(ventana, from_=0, to = 100, width=6)
giro.grid(column=2, )
# Establecer el valor por defecto del Spinbox
# var =IntVar()
# var.set(36)
# spin = Spinbox(window, from_=0, to=100, width=5, textvariable=var)




#Adicionar el widget Progressbar

from tkinter.ttk import Progressbar


progreso=Progressbar(ventana, length=200, style='black.Horizontal.TProgressbar')

progreso.grid(column=0, row=0)
# adicionar mas adelante formas de personalizar la barra de progreso
#---
#---
#---
#---
progreso['value'] = 70





#Adicionar un diálogo para archivos (elegir archivo y directorio)
imi = 0
if imi ==1 :
	from tkinter import filedialog
	archivos = filedialog.askopenfilename() #askopenfinlenames para multiples archivos
	pass


#Especificar los tipos de archivo (filtro por la extensión del archivo)
#file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))


#Puedes solicitar el directorio a usar con el método askdirectory:
#dir = filedialog.askdirectory()


#Puedes especificar el directorio inicial del diálogo especificando el initialdir, de esta manera:
#from os import path
#file = filedialog.askopenfilename(initialdir= path.dirname(__file__))





##<---Adicionar una barra de menú

from tkinter import Menu

#menu = Menu(ventana)

#new_item = Menu(menu)#  <--- segundo elemento

#new_item.add_command(label='uno')

#new_item.add_separator()

#new_item.add_command(label='dos')#estruccura para nuevos elementos 

#new_item.add_separator()

#new_item.add_command(label='tre')

#menu.add_cascade(label='barra', menu=new_item)


#ventana.config(menu=menu)





#<-----------Adicionar un widget Notebook (control de pestañas)

from tkinter import ttk


controlpestanas = ttk.Notebook(ventana)

venta1 = ttk.Frame(controlpestanas)

controlpestanas.add(venta1, text = "primero")

controlpestanas.pack(expand=1, fill='both')






ventana.mainloop()







