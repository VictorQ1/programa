from tkinter import *

from tkinter import messagebox

top = Tk()
frame = Frame(top)
frame.pack()
top.geometry("250x75")
top.title('Encuadres')
top.iconbitmap(r'C:\Users\Alumno 11\Desktop\Encuadre Perron mk 3000\iconochido.ico')

#Funcion correcta
def Mandar_Encuadre():
   msg = messagebox.showinfo("Elias es joto", "Elias es joto")
def read_from_db():
  c.execute('SELECT * FROM tabla1')
  data = c.fetchall()   

bottomframe = Frame(top)
bottomframe.pack( side = BOTTOM )   
#Colocar los botones bien
b1 = Button(frame, text = "Matemáticas", fg = "green", command = Mandar_Encuadre,height = '2', width = '10' )
b1.pack( side = LEFT) 

b2 = Button(frame, text = "Español", fg="blue", command = Mandar_Encuadre,height = '2', width = '10')
b2.pack( side = LEFT )

b3 = Button(frame, text = "Deportes", fg = "#6f9dab", command = Mandar_Encuadre,height = '2', width = '10')
b3.pack( side = LEFT )

b4 = Button(bottomframe, text = "Ingles", fg = "purple", command = Mandar_Encuadre,height = '2', width = '10')
b4.pack( side = LEFT)

b5 = Button(bottomframe, text = "Historia", fg = "#caae6b", command = Mandar_Encuadre,height = '2', width = '10')
b5.pack( side = BOTTOM)




top.mainloop()
