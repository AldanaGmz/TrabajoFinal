from tkinter import Tk
from tkinter import Label
from tkinter import Radiobutton
from tkinter import ttk
from tkinter import messagebox
from tkinter import StringVar
from tkinter import Entry
from tkinter import Frame
from tkinter import IntVar
from tkinter import Button

import base_datos  
import opcion_temas
from observador import Tema

"""Objeto Observado"""

class Producto (Tema):
    """Hereda de la clase Tema del módulo observador.py"""
    def __init__(self, window):
    
        
        # Ventana principal 
        self.root = window
        self.root.title("Entrega Final")
        self.base = base_datos.Crud()
        """Obejeto para el alta, modificación y eliminación de datos"""
        self.observador = base_datos.ConcreteObserverA(self)
        
        
        self.titulo = Label(self.root, text="Ingrese sus datos", bg="DarkOrchid3", fg="thistle1", height=1, width=60)
        self.titulo.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky="W" + "E")

        self.a_val = StringVar()
        self.b_val = StringVar() 
        self.w_ancho = 20

        self.tree = ttk.Treeview(height = 10, columns = 4)
        self.tree["columns"]=("one", "two", "three", "four")
        self.tree.grid(row = 7, column = 0, columnspan = 3)
        self.tree.heading("#0",text="ID",anchor="center")
        self.tree.heading("one", text = 'Título', anchor = "center")
        self.tree.heading("two", text = 'Descripción', anchor = "center")
        self.tree.heading("three", text = "Fecha", anchor = "center")
        self.tree.heading("four", text = "Objeto", anchor = "center")
         

        # obteniendo los productos
        def mostrar():
            # limpieza de tabla 
            records = self.tree.get_children()
            for element in records:
                self.tree.delete(element)
            # Consiguiendo datos
            """Aquí implenté format para que pudieran mostrarse los datos en el Treeview con el ORM"""
            for prod in base_datos.Producto.select():
                variables = ("Título: {} - Descripción: {} - Fecha: {} ".format(prod.titulo, prod.descripcion, prod.fecha))
                print(variables)
                """Aquí también está integrado el ejercicio de la unidad 2"""
                self.tree.insert('', 0, text = prod.id, values = (prod.titulo, prod.descripcion, prod.fecha, prod))

        self.boton0 =Button(self.root, text = 'Mostrar registros existentes',  command = mostrar)
        self.boton0.grid( row = 5, columnspan = 3, sticky = "W" + "E")


        self.boton1 = Button(self.root, text="Crear bd", command=lambda:self.base.crearbd())
        self.boton1.grid(row=6, column=1)
        
        """Se aplica el objeto para las funciones de alta, modificación y eliminación de datos"""
        def pasar_objeto_guardar():
            self.observador.update("Alta Datos")
            mostrar()

        def pasar_objeto_eliminar():
            self.observador.update_c("Eliminación Datos")
            mostrar()

        def pasar_objeto_modificar():
            self.observador.update_b("Modificación Datos")
            mostrar()

        
        self.boton3 = Button(self.root, text="Guardar", command=pasar_objeto_guardar)
        self.boton3.grid(row=11, column=0)
        self.boton4 = Button(self.root, text= "Eliminar", command=pasar_objeto_eliminar)
        self.boton4.grid(row=11, column=1)
        self.boton5 = Button(self.root, text="Modificar", command=pasar_objeto_modificar)
        self.boton5.grid(row=11, column=2)

        
        # ################ TEMAS ##############################

        self.temas_opciones = Frame(self.root, bg="red",borderwidth=2, relief="raised")
        self.temas_opciones.grid(row=12, column=0, columnspan=4, padx=1, pady=1, sticky="W" + "E")
 
        self.ancho_boton = 10
        self.temas = StringVar()
        self.temas.set("tema1")
        self.tema_option = IntVar(value=0)

        def bg_fg_option():
            print(self.tema_option.get())
            print(opcion_temas.eleccion_tema(self.tema_option.get()))
            self.temas_opciones["bg"] = opcion_temas.eleccion_tema(self.tema_option.get())
            self.root["bg"] = opcion_temas.eleccion_tema(self.tema_option.get())

        self.label = Label(self.temas_opciones, borderwidth=4, relief="raised", text="Temas", bg="#222",fg="OrangeRed",)
        self.label.pack(fill= "x")
        temas = ["tema1", "tema2", "tema3"]
        for opcion in temas:
            boton = Radiobutton(self.temas_opciones,
            text=str(opcion), indicatoron=1, value=int(opcion[-1])-1, variable =self.tema_option,
            bg="#222",fg="OrangeRed", command=bg_fg_option)
            boton["width"] = self.ancho_boton
            boton.pack(side= "top")


        # ################ FIN DE TEMAS #######################
    


if __name__ == '__main__':
    window = Tk()
    application = Producto(window)
    window.mainloop()
