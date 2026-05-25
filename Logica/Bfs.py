from collections import deque

def bfs(grafo, inicio, objetivo):

    cola = deque()
    cola.append((inicio, [inicio]))

    visitados = []

    print("\n================ INICIO BFS ================")
    print("Inicio:", inicio.get_clave())
    print("Objetivo:", objetivo.get_clave())
    print("===========================================\n")

    while cola:

        print("\n-------------------------------------------")

        actual, camino = cola.popleft()

        # verificar si es el objetivo
        if actual.get_clave() == objetivo.get_clave():

            ruta = []
            for nodo in camino:
                ruta.append(nodo.get_clave())

            print("\nOBJETIVO ENCONTRADO")
            print("Ruta final:", ruta)
            print("===========================================\n")

            return ruta

        # si no ha sido visitado
        if actual.get_clave() not in visitados:

            visitados.append(actual.get_clave())

            print("Marcado como visitado:", actual.get_clave())
            print("Visitados:", visitados)

            # obtener vecinos del grafo
            nodo_actual = grafo.grafo_diccionario[actual.get_clave()]

            vecinos = [v.get_clave() for v in nodo_actual.vecinos]
            print("Vecinos de", actual.get_clave(), ":", vecinos)

            for vecino in nodo_actual.vecinos:

                nuevo_camino = camino + [vecino]
                cola.append((vecino, nuevo_camino))

                print(f"{actual.get_clave()} -> {vecino.get_clave()}")

        else:

            print("Nodo ya visitado:", actual.get_clave())

    print("\nNO SE ENCONTRÓ EL OBJETIVO")
    print("===========================================\n")

    return []