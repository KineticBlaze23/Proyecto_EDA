from Datos.leer_archivo import cargar_grafo

#Llamada de las clases para poder implementar el menú
from Logica.Dfs import dfs  
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

        try:

            # Llamada al método que carga el json
            grafo, nodos = cargar_grafo()

            print("\nGrafo cargado correctamente")
            grafo.mostrar()

        except FileNotFoundError:

            print("\nEl archivo JSON no existe")

        except Exception as e:

            print("\nOcurrió un error:")
            print(e)

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

            print("\n---RECORRIDO DFS ---")

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

                dfs(
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

                

                print("\n---COMPARACIÓN---")

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
