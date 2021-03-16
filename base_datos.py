from peewee import SqliteDatabase
from peewee import CharField
from peewee import TextField
from peewee import DateTimeField
from peewee import Model

from tkinter import messagebox
from tkinter import Toplevel
from tkinter import Button

import datetime
import val
import  guardar 
import modificar
import eliminar
import datetime
from observador import Observador


db = SqliteDatabase("baseprueba3.db")

class BaseModel(Model):
    class Meta:
        database = db

class Producto(BaseModel):
    titulo = CharField(unique = True)
    descripcion = TextField()
    fecha = DateTimeField(default= datetime.datetime.now)

    def __str__ (self, ):
        return "El título es: " +  self.titulo 


class RegistroBD(BaseModel):
    """Tabla que notifica los movimientos de la tabla Producto"""
    titulo = CharField()
    descripcion = CharField()
    estado = CharField()
    fecha = DateTimeField(default = datetime.datetime.now)


class Crud:
    """Agregué esta función para que se active la base de datos a travé del boton Crear bd"""
    def crearbd(self, ):
        try:
            db.connect()
            db.create_tables([Producto, RegistroBD])
            messagebox.showinfo("Bases de datos", "Bases de datos creadas con éxito")

        except:
            messagebox.showerror("Bases de datos", "Bases de datos ya existentes")
    

class Registros:    
    """Función que registra los movimientos de la tabla Producto"""
    def registro (self, titulo, descripcion, estado):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado 

        try:
            dato = RegistroBD()
            dato.titulo = self.titulo
            dato.descripcion = self.descripcion
            dato.estado= self.estado
            dato.save()
        except:
            messagebox.showwarning("Datos", "No se ha podido cargar el registro")


class ConcreteObserverA(Observador, Registros):
    """Observador que hereda de las clases Observador del modulo observador.py y de la clase Registros"""
    def __init__ (self, obj):
        self.obj = obj
        self.obj.agregar(self)


    def guarda(self, variables, popup_guardar):
        popup_guardar.destroy()
        
        lista = []
        for variable in variables:
            lista.append(variable.get())
        
        
        if(val.validar(lista[1])==(True)):
            try:
                prod = Producto()
                prod.titulo = lista[1]
                prod.descripcion = lista[2]
                prod.save()
                self.registro(prod.titulo, prod.descripcion, "Alta Datos")
                messagebox.showinfo("Datos", "Datos guardados con éxito")
            except:
                messagebox.showwarning("Dato", "Dato existente, ingrese otro título")
        else:
            messagebox.showwarning("No Validado", "Campo título solo con datos alfabeticos")
        
    
    def update(self, dato):
        """Función de la clase Observador del módulo observador.py"""
        self.dato = dato
        print ("Estado =  ", self.dato)
        if self.dato == "Alta Datos":
            popup_guardar = Toplevel()
            vars_guardar = guardar.crear_form_guardar(popup_guardar, guardar.campos)
            boton_guardar = Button(popup_guardar, text='Guardar', command=(lambda:self.guarda(vars_guardar, popup_guardar)))
            boton_guardar.pack()

            popup_guardar.grab_set()
            popup_guardar.focus_set()
            popup_guardar.wait_window()
            print("Se ha guardado un nuevo registro")

    def modifica(self, variables, popup_modificar):
        popup_modificar.destroy()
        lista = []
        for variable in variables:
            lista.append(variable.get())
        
        prod = Producto()
        prod.titulo = lista[1]
        prod.descripcion = lista[2]
        
        if (val.validar(lista[1])==(True)):
            try:
                actualizar = Producto.update(titulo = lista[1], descripcion = lista[2]).where(Producto.id == lista[0])
                actualizar.execute()   
                self.registro("Registro: " + lista[0] + " = " + prod.titulo, prod.descripcion, "Modificación Datos")
                messagebox.showinfo("Datos", "Datos modificados con éxito")     
            except:
                messagebox.showwarning("Datos", "Campo título existente. Ingrese un título diferente")
        else:
            messagebox.showwarning("No Validado", "Campo título solo con datos alfabeticos") 


    def update_b(self, dato):
        """Función de la clase Observador del módulo observador.py"""
        self.dato = dato
        print ("Estado =  ", self.dato)
        if self.dato == "Modificación Datos":
            popup_modificar = Toplevel()
            vars_modificar = modificar.crear_form_modificar(popup_modificar, modificar.campos)
            boton_modificar = Button(popup_modificar, text='Modificar', command=(lambda:self.modifica(vars_modificar, popup_modificar)))
            boton_modificar.pack()

            popup_modificar.grab_set()
            popup_modificar.focus_set()
            popup_modificar.wait_window()
            print("Se ha modificado un registro")


    def elimina(self, variables, popup_eliminar):
        popup_eliminar.destroy()
        lista = []
        for variable in variables:
            lista.append(variable.get())
        try:
            borrar = Producto.get(Producto.id == lista[0])
            borrar.delete_instance()
            self.registro("Registro: " + lista[0] , "Eliminado", "Eliminación Datos")
            messagebox.showinfo("Datos", "Datos eliminados con éxito")
        except:
            messagebox.showwarning("Registro", "Registro inexistente")
    
    def update_c(self, dato):
        """Función de la clase Observador del módulo observador.py"""
        self.dato = dato
        print ("Estado =  ", self.dato)
        if self.dato == "Eliminación Datos":
            popup_eliminar = Toplevel()
            vars_eliminar = eliminar.crear_form_eliminar(popup_eliminar, eliminar.campos)
            boton_eliminar = Button(popup_eliminar, text='Eliminar', command=(lambda:self.elimina(vars_eliminar, popup_eliminar)))
            boton_eliminar.pack()

            popup_eliminar.grab_set()
            popup_eliminar.focus_set()
            popup_eliminar.wait_window()
            print("Se ha eliminado un registro")





    

    
    


    

        


        

        
        


    
