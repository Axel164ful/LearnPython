from tkinter import *

from tkinter import ttk
from tkinter.ttk import *


window = Tk()

window.title("Welcome to LikeGeeks app")

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)

tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='First')

tab_control.add(tab2, text='Second')



lbl1 = Label(tab1, text= 'label1')


lbl = Label(tab2, text="Hello")


combo = Combobox(tab1)
combo.grid(column=0, row=0)

combo['values']= (1, 2, 3, 4, 5, "Text")

lbl1.grid(column=0, row=0)







lbl2 = Label(tab2, text= 'label2')

lbl2.grid(column=0, row=0)

tab_control.pack(expand=1, fill='both')







window.mainloop()