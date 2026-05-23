## Clase Nodo
class Nodo:
    ##El constructor del nodo esta diseñado de tal manera que tiene la clave y el valor asociada a esa clave.
    ##En este caso self funciona como intermediario en la llamada de la clase. Ej: n1 = Nodo('D', ['E', 'F'] ) 
    # pero la llamada interna es: Nodo.__init__(n1, 'D', ['E', 'F'] )  
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor