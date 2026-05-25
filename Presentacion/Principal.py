from Datos.leer_archivo import cargar_grafo
from Logica.Bfs import bfs


# cargar datos desde JSON
grafo, nodos = cargar_grafo()


# mostrar grafo
print("GRAFO:")

for clave, nodo in nodos.items():

    vecinos = []

    for v in nodo.vecinos:
        vecinos.append(v.get_clave())

    print(clave, "->", vecinos)


# ejecutar BFS
resultado = bfs(grafo, nodos["A"], nodos["G"])

print()
print("BFS A → G:")
print(resultado)