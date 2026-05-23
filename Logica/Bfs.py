from collections import deque

def bfs(grafo, inicio, objetivo):

    cola = deque()
    cola.append((inicio, [inicio]))

    visitados = []

    while cola:

        actual, camino = cola.popleft()

        # verificar si es el objetivo
        if actual.get_clave() == objetivo.get_clave():

            ruta = []

            for nodo in camino:
                ruta.append(nodo.get_clave())

            return ruta

        # si no ha sido visitado
        if actual.get_clave() not in visitados:

            visitados.append(actual.get_clave())

            # obtener vecinos del grafo
            nodo_actual = grafo.grafo_diccionario[actual.get_clave()]

            for vecino in nodo_actual.vecinos:

                # agregar a la cola con su camino
                nuevo_camino = camino + [vecino]
                cola.append((vecino, nuevo_camino))

    return []