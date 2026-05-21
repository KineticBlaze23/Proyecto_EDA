class Arista:
    #Constructor de la clase Arista, recibe el nodo origen y el nodo destino
    def __init__(self, origen, destino):
        self.origen = origen
        self.destino = destino
    
    #Setters para asignar el nodo origen y el nodo destino
    def set_origen(self, origen):
        self.origen = origen
        
    def set_destino(self, destino):
        self.destino = destino
    
    #Getters para obtener el nodo origen y el nodo destino  
    def get_origen(self):
        return self.origen
    
    def get_destino(self):
        return self.destino
    
    #Impresion de los nodos conectados
    #def __str__(self):
        #return self.origen.get_valor() + "---->" + self.destino.get_valor()