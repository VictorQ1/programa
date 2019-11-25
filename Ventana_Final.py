from tkinter import *

from tkinter import messagebox, Entry, mainloop, StringVar


top = Tk()
frame = Frame(top)
frame.pack()
top.geometry("250x75")
top.title('Encuadres')
top.iconbitmap(r'C:\Users\alank\Desktop\programa\iconochido.ico')

#Funcion correcta
def Elias():
   msg = messagebox.showerror("Lo sentimos", "Estamos trabajando en ello")   
   
def Mandar_Encuadre():
   frame = Frame(top)
   frame.pack()
   top.geometry("1280x720")
   top.title('Encuadre 1')
   imagen=PhotoImage(file=r'C:\Users\alank\Desktop\Encuadre.png')
   fondo=Label(top,image=imagen).place(x=0,y=0)
   top.mainloop()
            

bottomframe = Frame(top)
bottomframe.pack( side = BOTTOM )   
#Colocar los botones bien
b1 = Button(frame, text = "Matemáticas", fg = "green", command = Mandar_Encuadre, height = '2', width = '10',)
b1.pack( side = LEFT)

b2 = Button(frame, text = "Español", fg="blue", command = Elias,height = '2', width = '10')
b2.pack( side = LEFT )

b3 = Button(frame, text = "Deportes", fg = "#6f9dab", command = Elias,height = '2', width = '10')
b3.pack( side = LEFT )

b4 = Button(bottomframe, text = "Ingles", fg = "purple", command = Elias,height = '2', width = '10')
b4.pack( side = LEFT)

b5 = Button(bottomframe, text = "Historia", fg = "#caae6b", command = Elias,height = '2', width = '10')
b5.pack( side = BOTTOM)




top.mainloop()
