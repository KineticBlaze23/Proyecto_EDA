
from Entidades.Arista import Arista
class Grafo:
    # Representación del grafo con diccionario: clave -> Nodo
    def __init__(self):
        self.grafo_diccionario = {}

    # Agregar nodo al grafo
    def agregar_nodo(self, nodo):
        if nodo.get_clave() in self.grafo_diccionario:
            return "El nodo ya se encuentra en el grafo"

        self.grafo_diccionario[nodo.get_clave()] = nodo

    # Agregar arista
    def agregar_arista(self, arista):
        origen = arista.get_origen()
        destino = arista.get_destino()

        if origen.get_clave() not in self.grafo_diccionario:
            return "El nodo origen no existe"

        if destino.get_clave() not in self.grafo_diccionario:
            return "El nodo destino no existe"

        
        nodo_origen = self.grafo_diccionario[origen.get_clave()]
        nodo_origen.agregar_vecino(destino)

    # Mostrar grafo en consola
    def mostrar(self):
        for clave in self.grafo_diccionario:
            nodo = self.grafo_diccionario[clave]
            vecinos = [v.get_clave() for v in nodo.vecinos]
            print(f"{clave} -> {vecinos}")