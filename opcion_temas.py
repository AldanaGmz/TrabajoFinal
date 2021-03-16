import shelve


# ##################################################################
# Defino base de datos
# ##################################################################
"""Tuve que cambiar lo que estaba entre paréntesis porque no me funcionaba el módulo,
ya que cambié la ubicación en el directorio"""

with shelve.open("opcion_temas") as db:
    db["tema1"] = "#222"
    db["tema2"] = "blue"
    db["tema3"] = "OrangeRed"

# ##################################################################
# Defino comando para modificar propiedades de los temas
# ##################################################################

def eleccion_tema (variable):
    with shelve.open("opcion_temas") as db:
        print(variable)
        print(type(variable))
        if variable == 0:
            variable = "tema1"
            print(variable)
        elif variable == 1:
            variable = "tema2"
            print(variable)
        elif variable == 2:
            variable = "tema3"
            print(variable)
        TemaSeleccionado = db[variable]
        return TemaSeleccionado



