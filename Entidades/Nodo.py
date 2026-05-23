## Clase Nodo
class Nodo:
    #Le cambie el valor a vecinos y le hice con una lista.
    def __init__(self, clave):
        self.clave = clave
        self.vecinos = []
    
    def get_clave(self):
        return self.clave
    
    def agregar_vecino(self, vecino):
        if vecino not in self.vecinos:
            self.vecinos.append(vecino)
