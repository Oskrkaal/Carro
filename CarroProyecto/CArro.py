from Tkinter import *
# ~ import time, os

 
def Avanzar():
    print('Avanzar')
     
def Retroceder():
    print('Retroceder')
     
def Izquierda():
    print('Izquierda')
     
def Derecha():
    print('Derecha')
    
def ActivarAutomatico():
    print('Activar Automatico')
    
def DesactivarAutomatico():
    print('Desactivar Automatico')
    
def Detener():
    print('Detener')

def Apagado():
    print('Apagado')

def Encender():
    print('Encender')
    
		
    

ventana = Tk()
ventana.title("Carro Controlado Via Computadora")
ventana.geometry("600x400")
ventana.resizable(width=False, height=False)
ventana.configure(background="#333334")



BotonEncender = Button(ventana, text='Encender', command=Encender, bg="#EBEDEE",fg="#288BEE").place(x=20,y=20)
# ~ BotonApagar.pack(side=BOTTOM)
BotonApagar = Button(ventana, text='Apagar', command=ventana.quit, bg="#EBEDEE",fg="red").place(x=110,y=20)
# ~ BotonApagar.pack(side=BOTTOM)
BotonAvanzar = Button(ventana, text='Avanzar', command=Avanzar, padx=25,pady=25, bg="#EBEDEE",fg="#288BEE").place(x=240,y=20)
# ~ BotonAvanzar.pack(side=TOP)
BotonIzquierda = Button(ventana, text='Izquierda', command=Izquierda,padx=25,pady=25, bg="#EBEDEE",fg="#288BEE").place(x=20,y=165)
# ~ BotonIzquierda.pack(side=LEFT)
BotonDerecha = Button(ventana, text='Derecha', command=Derecha,padx=25,pady=25, bg="#EBEDEE",fg="#288BEE").place(x=420,y=165)
# ~ BotonDerecha.pack(side=RIGHT)
BotonRetroceder = Button(ventana, text='Retroceder', command=Retroceder,padx=25,pady=25, bg="#EBEDEE",fg="#288BEE").place(x=240,y=310)
# ~ BotonRetroceder.pack(side=BOTTOM)
BotonDetener = Button(ventana, text='Detener', command=Detener,padx=25,pady=25, bg="#EBEDEE",fg="red").place(x=245,y=165)
# ~ BotonDetener.pack(side=BOTTOM)
BotonActivarAutomatico = Button(ventana, text='Activar Automatico', command=ActivarAutomatico, padx=5,pady=5, bg="#EBEDEE",fg="#288BEE").place(x=420,y=280)
# ~ BotonActivarAutomatico.pack(side=BOTTOM)
BotonDesactivarAutomatico = Button(ventana, text='Desactivar Automatico', command=DesactivarAutomatico, padx=5,pady=5, bg="#EBEDEE",fg="#288BEE").place(x=420,y=320)
# ~ BotonDesactivarAutomatico.pack(side=BOTTOM)
ventana.mainloop()
