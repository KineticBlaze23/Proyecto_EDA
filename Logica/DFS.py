#Llamada a la clase Grafo para poder usar sus métodos y atributos
from Entidades.Grafo import Grafo


#Definicion del método DFS 
#Mediante una adecuación el método ya no recibe el parámetro grafo dado que nodo es un objeto. Es decir, bajo la 
#estructura de la clase nodo este ya tiene los vecinos asociados
def DFS (nodo, destino, searched, componentR, orden_visita):
    searched.add(nodo.get_clave())
    #Me permite guardar el orden en el cual fueron pasando 
    orden_visita.append(nodo.get_clave())
    #Agrega el camino actual 
    componentR.append(nodo.get_clave())
    #Este if me permite validar si es el destino
    if nodo.get_clave() == destino.get_clave():
        return True
    

    #Se recorre la lista de vecinos contenida directamente por nodo
    for vecino in nodo.vecinos:
        if vecino.get_clave() not in searched:
            #Realiza la llamada recuriva 
            encontrado = DFS(vecino, destino, searched, componentR, orden_visita)
            #Se comprueba que se llego al destino
            if encontrado:
                return True
    #Este apartado de pop funciona en caso de que el nodo que trabaje no me lleva a destino
    componentR.pop()
    return False        