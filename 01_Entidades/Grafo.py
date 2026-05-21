class Grafo:
    #Representación de un grafo como diccionario: nodo (clave) y sus aristas (nodos conectados)
    def __init__(self):
        self.grafo_diccionario = {}
        
    #Agregar un nodo al grafo, si el nodo ya existe, se muestra un mensaje indicando que el nodo ya se encuentra en el grafo
    def agregar_nodo(self, nodo):
        if nodo in self.grafo_diccionario:
            return "El nodo ya se encuentra en el grafo"
        self.grafo_diccionario[nodo.get_dato()] = []
        
    #Agregar una arista al grafo, se verifica que el nodo origen y el nodo destino existan en el grafo antes de agregar la arista.
    #Si alguno de los nodos no existe, se muestra un mensaje indicando que el nodo no existe.
    def agregar_aristas(self, arista):
        origen = arista.get_origen()
        destino = arista.get_destino()
        if origen not in self.grafo_diccionario:
            return "El nodo origen no existe "
        
        if destino not in self.grafo_diccionario:
            return "El nodo destino no existe "
        self.grafo_diccionario[origen].append(arista)