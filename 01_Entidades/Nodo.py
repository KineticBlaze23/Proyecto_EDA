## Clase Nodo
class Nodo:
    ##El constructor del nodo esta diseñado de tal manera que tiene la clave y el valor asociada a esa clave.
    ##En este caso self funciona como intermediario en la llamada de la clase. Ej: n1 = Nodo('D', ['E', 'F'] ) 
    # pero la llamada interna es: Nodo.__init__(n1, 'D', ['E', 'F'] )  
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor

  # GETTERS
    def get_clave(self):
        return self.__clave

    def get_dato(self):
        return self.__dato

    # SETTERS
    def set_clave(self, nueva_clave):
        self.__clave = nueva_clave

    def set_dato(self, nuevo_dato):
        self.__dato = nuevo_dato        