from tkinter import Tk
from tkinter import Toplevel
from tkinter import Button
from tkinter import Frame
from tkinter import StringVar
from tkinter import Label
from tkinter import Entry

archivo = 'persona'
campos = ("Id","Titulo","Descripcion")


def imprimir(variables):
    for variable in variables:
        print('Input => "%s"' % variable.get())


def crear_form_eliminar(root, campos):
    formulario = Frame(root)
    formulario.pack(fill="x")
    div1 = Frame(formulario, width=100)
    div1.pack(side="left")
    div2 = Frame(formulario, padx=7, pady=2)
    div2.pack(side="right", expand="YES", fill="x")
    variables = []
    lab = Label(div1, width=10, text="Id")
    lab.pack(side="top")
    ent = Entry(div2, width=30, relief="sunken")
    ent.pack(side="top", fill="x")
    var = StringVar()
    ent.config(textvariable=var)
    var.set("")
    variables.append(var)
    return variables
    

if __name__ == '__main__':
    root = Tk()
    vars_elimina = crear_form_eliminar(root, campos)
    boton_imprimir = Button(root, text='Imprimir', command=(lambda: imprimir(vars_elimina)))
    boton_imprimir.pack(side="bottom")
    root.bind('<Return>', (lambda event: imprimir(vars_elimina)))  
    root.mainloop()