from tkinter import messagebox


def decorador_g(funcion_parametro):
    def funcion_interior(*args):
        try:
            funcion_parametro(*args)
            print("Se ha registrado un nuevo ingreso")
        except:
            pass
            
            
    return funcion_interior

def decorador_m(funcion_parametro):
    def funcion_interior(*args):
        try:
            funcion_parametro(*args)
            print("Se ha modificado un registro")
        except:
            pass
            
            
    return funcion_interior

def decorador_e(funcion_parametro):
    def funcion_interior(*args):
        try:
            funcion_parametro(*args)
            print("Se ha eliminado un registro")
        except:
            pass
            
            
    return funcion_interior
