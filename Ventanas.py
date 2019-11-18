from tkinter import *

from tkinter import messagebox

top = Tk()
frame = Frame(top)
frame.pack()
top.geometry("800x600")
def Mandar_Encuadre():
   msg = messagebox.showinfo( "Elias es joto", "Elias es joto")

bottomframe = Frame(top)
bottomframe.pack( side = BOTTOM )   
#Colocar los botones bien
b1 = Button(frame, text = "Matemáticas", fg = "red", command = Mandar_Encuadre)
b1.pack( side = LEFT) 

b2 = Button(frame, text = "Español", fg="brown", command = Mandar_Encuadre)
b2.pack( side = LEFT )

b3 = Button(frame, text = "Deportes", fg = "blue", command = Mandar_Encuadre)
b3.pack( side = LEFT )

b4 = Button(bottomframe, text = "Ingles", fg = "black", command = Mandar_Encuadre)
b4.pack( side = LEFT)

b5 = Button(bottomframe, text = "Historia", fg = "green", command = Mandar_Encuadre)
b5.pack( side = BOTTOM)



top.mainloop()
