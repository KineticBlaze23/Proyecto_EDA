import json
from Entidades.Nodo import Nodo
from Entidades.Arista import Arista
from Entidades.Grafo import Grafo


def cargar_grafo():

    with open("Datos/datos.json", "r") as archivo:
        data = json.load(archivo)

    grafo = Grafo()

    nodos = {}

    for clave in data:

        nodo = Nodo(clave)

        grafo.agregar_nodo(nodo)

        nodos[clave] = nodo

    for clave, vecinos in data.items():

        for v in vecinos:

            arista = Arista(nodos[clave], nodos[v])

            grafo.agregar_arista(arista)

    return grafo, nodos