from cgitb import text
from contextlib import nullcontext
from tkinter import font
import numpy as np
from tkinter import*
from tkinter import messagebox

#Yulissa Restrepo (8-961-1900)     Jorge Benthancourth ()
# Proyecto 2 -- M.Cerrado y M.Abierto

class Main:

    def __init__(self):
        self.root=Tk()
        self.root.config(width=380, height=280)
        self.root.title('PROYECTO 2')
        self.title=Label(self.root,text="Busqueda de raices \ncon Metodos Numericos", font=("consolas",15, "bold"), anchor=CENTER)
        self.title.place(x=75, y=0)
        self.title2=Label(self.root, text="Yulissa Restrepo y Jorge Benthancourth \n1SF131", font=("consolas",12, ), anchor=CENTER)
        self.title2.place(x=20, y=50)
        self.enter1=Button(self.root, text="Metodo Cerrado", command=self.metodoCerrado)
        self.enter1.place(x=150, y=150)
        self.enter2=Button(self.root, text="Metodo Abierto", command=self.metodoAbierto)
        self.enter2.place(x=150, y=200)
        self.root.mainloop()

    def metodoCerrado(self):
        self.root2=Tk()
        self.root2.config(width=600, height=800)
        self.root2.title('PROYECTO 2 - METODO CERRADO')
        self.title=Label(self.root2,text="METODO REGULA FALSI", font=("consolas",20, "bold"), anchor=CENTER)
        self.title.place(x=150, y=10)
        self.mc1=Label(self.root2,text="Introducir la funcion :", font=("consolas",10), anchor=CENTER)
        self.mc1.place(x=15, y=100)
        self.mc2=Label(self.root2,text="Introducir limite inferior :", font=("consolas",10), anchor=CENTER)
        self.mc2.place(x=15, y=150)
        self.mc3=Label(self.root2,text="Introducir limite superior :", font=("consolas",10), anchor=CENTER)
        self.mc3.place(x=15, y=200)
        self.mc4=Label(self.root2,text="")
        self.mc4.place(x=20, y=300)
        self.mc5=Label(self.root2,text="")
        self.mc5.place(x=20, y=600)
        self.campmc=Entry(self.root2,bg="white")
        self.campmc.place(x=250, y=100)
        self.campmc2=Entry(self.root2,bg="white")
        self.campmc2.place(x=250, y=150)
        self.campmc3=Entry(self.root2,bg="white")
        self.campmc3.place(x=250, y=200)
        self.calcularmc=Button(self.root2, text="CALCULAR")#, command=self.regulaFalsi(self.campmc.get(),self.campmc2.get(),self.campmc3.get()))
        self.calcularmc.place(x=300, y=250)

          
    def metodoAbierto(self):
        self.root3=Tk()
        self.root3.config(width=600, height=800)
        self.root3.title('PROYECTO 2 - METODO ABIERTO')
        self.title=Label(self.root3,text="METODO DE LA SECANTE", font=("consolas",20, "bold"), anchor=CENTER)
        self.title.place(x=150, y=10)
        self.ma1=Label(self.root3,text="Introducir la funcion :", font=("consolas",10), anchor=CENTER)
        self.ma1.place(x=15, y=100)
        self.ma2=Label(self.root3,text=" el valor de X:", font=("consolas",10), anchor=CENTER)
        self.ma2.place(x=15, y=150)
        self.ma3=Label(self.root3,text=" el valor de X-1:", font=("consolas",10), anchor=CENTER)
        self.ma3.place(x=15, y=200)
        self.ma4=Label(self.root3,text="")
        self.ma4.place(x=20, y=300)
        self.ma5=Label(self.root3,text="")
        self.ma5.place(x=20, y=600)
        self.campma=Entry(self.root3,bg="white")
        self.campma.place(x=250, y=100)
        self.campma2=Entry(self.root3,bg="white")
        self.campma2.place(x=250, y=150)
        self.campma3=Entry(self.root3,bg="white")
        self.campma3.place(x=250, y=200)
        self.calcularma=Button(self.root3, text="CALCULAR")#, command=self.secante(self.campma.get(),self.campma2.get(),self.campma3.get()))
        self.calcularma.place(x=300, y=250)

    #def regulaFalsi(self):


    #def secante(self):



#Inicio del programa
Inicio=Main()