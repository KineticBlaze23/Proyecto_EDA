#Llamada de las clases para poder implementar el menú
from Logica.DFS import DFS
from Entidades.Grafo import Grafo
from Entidades.Nodo import Nodo
from Entidades.Arista import Arista
from Logica.Bfs import bfs

#Menú principal del programa
grafo = None
while True:

    print("\n--- MENU ---")
    print("1. Crear Grafo")
    print("2. Realizar Recorrido BFS")
    print("3. Realizar Recorrido DFS")
    print("4. Salir")

    opcion = input("Seleccione: ")

    #Este if me permite crear un grafo de los cuales estaran en el archivo estatico.
    #Dado ello, es necesario aplicar el manejo de excepciones para evitar que el programa se caiga en caso de que el archivo no exista. 
    if opcion == "1":
         
         numGrafo = input('Ingrese el grafo que desea crear: ')
         #Mediante esta manera como tentativa funcionara la creación desde el archivo. 
         #En este caso se lo plantea mediante txt
         nombre_archivo = "grafo" + numGrafo + ".txt"

         try:

             archivo = open(nombre_archivo, "r")

             grafo = Grafo()

             nodos_creados = {}

             for linea in archivo:

                 datos = linea.strip().split(",")

                 origen_clave = datos[0]
                 destino_clave = datos[1]

                 #Crear nodo origen si no existe
                 if origen_clave not in nodos_creados:

                     nodo_origen = Nodo(origen_clave)

                     nodos_creados[origen_clave] = nodo_origen

                     grafo.agregar_nodo(nodo_origen)

                 #Crear nodo destino si no existe
                 if destino_clave not in nodos_creados:

                     nodo_destino = Nodo(destino_clave)

                     nodos_creados[destino_clave] = nodo_destino

                     grafo.agregar_nodo(nodo_destino)

                 #Obtener objetos nodo
                 nodo_origen = nodos_creados[origen_clave]
                 nodo_destino = nodos_creados[destino_clave]

                 #Crear arista
                 arista = Arista(nodo_origen, nodo_destino)

                 #Agregar arista al grafo
                 grafo.agregar_arista(arista)

             archivo.close()

             print("Grafo cargado correctamente")

         except FileNotFoundError:

             print("El archivo no existe")
    elif opcion == '2':
        #Esta parte me permite verificar si fue creado un grafo antes 
        if grafo is None or len(grafo.grafo_diccionario) == 0:

            print("Debe cargar un grafo antes de ejecutar BFS")

        else:
            print("\n---RECORRIDO BFS---")

            inicio = input("Ingrese nodo inicio: ")
            fin = input("Ingrese nodo final: ")

            if inicio not in grafo.grafo_diccionario:

                print("El nodo inicio no existe")

            elif fin not in grafo.grafo_diccionario:

                print("El nodo final no existe")

            else:

                nodo_inicio = grafo.grafo_diccionario[inicio]
                nodo_fin = grafo.grafo_diccionario[fin]

                #Aplicación BFS
                ruta_bfs = bfs(
                    grafo,
                    nodo_inicio,
                    nodo_fin
                )

                #Calcular saltos
                saltos_bfs = len(ruta_bfs) - 1

                print("\nRuta encontrada:")
                print(ruta_bfs)

                print("\nCantidad de saltos:")
                print(saltos_bfs)

                print("\nBFS garantiza")
                print("el camino más corto.")

    elif opcion == '3':
        if grafo is None or len(grafo.grafo_diccionario) == 0:

            print("Debe cargar un grafo antes de ejecutar DFS")

        else:

            print("\n===== RECORRIDO DFS =====")

            inicio = input("Ingrese nodo inicio: ")
            fin = input("Ingrese nodo final: ")

            if inicio not in grafo.grafo_diccionario:

                print("El nodo inicio no existe")

            elif fin not in grafo.grafo_diccionario:

                print("El nodo final no existe")

            else:

                nodo_inicio = grafo.grafo_diccionario[inicio]
                nodo_fin = grafo.grafo_diccionario[fin]

                #Estas variables me ayudan a almacenar los resultados del recorrido DFS, como el orden de visita, la ruta encontrada y los nodos ya visitados.  
                searched = set()
                componentR = []
                orden_visita = []

                DFS(
                    nodo_inicio,
                    nodo_fin,
                    searched,
                    componentR,
                    orden_visita
                )
                #Aquí unicamente cuento los saltos que por facilidad solo mediante la cantidad -1
                saltos_dfs = len(componentR) - 1

           
               #Como se pide una comparación, se lo llama al bfs aquí 
                ruta_bfs = bfs(
                    grafo,
                    nodo_inicio,
                    nodo_fin
                )
                #Aplico la misma manera de contar los saltos para el bfs    
                saltos_bfs = len(ruta_bfs) - 1

                print("\nOrden de visita:")
                print(orden_visita)

                print("\nRuta encontrada:")
                print(componentR)

                print("\nCantidad de saltos:")
                print(saltos_dfs)

                print("\nDFS NO garantiza")
                print("el camino más corto.")

                

                print("\n===== COMPARACIÓN =====")

                print("Saltos BFS:", saltos_bfs)

                print("Saltos DFS:", saltos_dfs)

                if saltos_dfs > saltos_bfs:

                    print("\nDFS encontró una ruta más larga que BFS")

                elif saltos_dfs == saltos_bfs:

                    print("\nDFS encontró una ruta igual a BFS")

                else:

                    print("\nDFS encontró una ruta más corta")   

    elif opcion == "4":

        print("Saliendo del programa...")
        break

else:

        print("\nOpción inválida")