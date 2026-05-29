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

    # Mostrar grafo
    def mostrar(self):

        print("\n---GRAFO---\n")

        # Recorrer cada nodo del diccionario
        for clave in self.grafo_diccionario:

            nodo = self.grafo_diccionario[clave]

            # Lista para guardar claves de vecinos
            vecinos = []

            # Recorrer vecinos del nodo
            for vecino in nodo.vecinos:

                vecinos.append(vecino.get_clave())

            # Mostrar nodo y vecinos
            print(f"{clave} -> {vecinos}")
