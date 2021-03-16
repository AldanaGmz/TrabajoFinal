"""Patrón Observador"""

class Tema:

    observadores = []

    def agregar(self, obj):
        self.observadores.append(obj)

    def notificar(self, dato):
        self.dato = dato
        for observador in self.observadores:
            observador.update(self.dato)

class Observador:

    def update(self, ):
        raise NotImplementedError("Delegación de actualización")


        