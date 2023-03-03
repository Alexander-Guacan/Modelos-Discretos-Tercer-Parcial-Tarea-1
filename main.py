def es_grafo_no_dirigido(grafo: list[list[int]]) -> bool:
    """
    Retorna True si todas las aristas cumplen el criterio de bidireccionalidad y False en caso contrario

    Args:
        grafo (list[list[int]]): _description_ Lista de adyacencias

    Returns:
        bool: _description_ True: grafo nd dirigido, False: grafo dirigido
    """
    # El primer nodo de la lista no tiene vertices adyacentes
    if len(grafo[0]) <= 0:
        return False
    
    # Nodos que quedan en espera a que sus nodos adyacentes sean recorridos
    queue = list[int]()
    # Agregamos a la cola el primer nodo de la lista de adyacencias
    queue.append(0)
    # Nodos visitados al recorrer el grafo, marcamos al nodo 0 como visitado
    nodos_visitados = [0]

    # Mientras aun queden nodos por recorrer
    while len(queue) > 0:
        # Obtenemos cada nodo en el orden en que fueron agregados
        nodo_actual = queue.pop(0)
        
        # Recorrer cada nodo adyacente al nodo actual
        for vertice_adyacente in grafo[nodo_actual]:
            # La arista entre nodo actual y el nodo adyacente no tiene bidireccionalidad
            if nodo_actual not in grafo[vertice_adyacente]:
                return False
            
            # Agregamos cada nodo adyacente que no haya sido visitado
            if vertice_adyacente not in nodos_visitados:
                # Agregamos a la lista de nodos cuya lista de vertices adyacentes se debe recorrer
                queue.append(vertice_adyacente)
                # Indicamos que el nodo adyacente ha sido visitado
                nodos_visitados.append(vertice_adyacente)

    # Verficamos que se haya recorrido todos los nodos
    if len(nodos_visitados) < len(grafo):
        return False

    # No se encontro ninguna arista unidireccional. Es grafo no dirigido
    return True

def recorrido_en_profundidad(grafo: list[list[int]], vertice_inicial = 0) -> list[list[int]]:
    """
    Retorna todos los caminos posibles que permitan recorrer todo el grafo desde un vertice inicial pasando una sola vez por cada nodo

    Args:
        grafo (list[list[int]]): _description_ Lista de adyacencia
        vertice_inicial (int, optional): _description_. Defaults to 0. Nodo desde donde comenzara a hacer el recorrido por el grafo

    Returns:
        list[list[int]]: _description_ Rutas posibles desde el vertice inicial hasta recorrer todo el grafo con sus diferentes caminos
    """
    # Listado de caminos posibles. Su primer camino empieza desde el nodo inicio
    caminos = [[vertice_inicial]]
    # Camino que se recorre actualmente
    camino_actual = 0

    # Mientras no sea el ultimo camino por recorrer
    while camino_actual < len(caminos):
        # Ultimo nodo agregado al camino actual
        nodo_actual = caminos[camino_actual][-1]
        # No existe bifurcacion
        es_camino_alterno = False
        # Recorremos cada vertice adyacente al nodo actual
        for vertice_adyacente in range(len(grafo[nodo_actual])):
            # El nodo adyacente ya ha sido recorrido en el camino actual
            if grafo[nodo_actual][vertice_adyacente] in caminos[camino_actual]:
                continue

            # Es el primer nodo adyacente al nodo actual
            if not es_camino_alterno:
                # Agregamos el nodo adyacente al camino actual
                caminos[camino_actual].append(grafo[nodo_actual][vertice_adyacente])
                # Si hay otro nodo adyacente sera un camino alterno
                es_camino_alterno = True
            # Es un camino alterno
            else:
                # Creamos el camino alternativo con los siguientes nodos adyacentes
                caminos.append(caminos[camino_actual][:caminos[camino_actual].index(nodo_actual) + 1] + [grafo[nodo_actual][vertice_adyacente]])

        # No se ha agregado un nuevo nodo al camino
        if nodo_actual == caminos[camino_actual][-1]:
            # Continuamos al siguiente camino
            camino_actual += 1

    # Retornamos los caminos que hayan recorrido todo el grafo
    return [camino for camino in caminos if len(camino) == len(grafo)]

def main():
    # Grafo no dirigido
    grafo_A = [
        [1,2,3,4],
        [2,0],
        [1,0],
        [0,4],
        [3,0]
    ]

    print("El grafo A es" + (" no " if es_grafo_no_dirigido(grafo_A) else " ") + "dirigido")
    print(recorrido_en_profundidad(grafo_A, 2))
    
    # Grafo dirigido
    grafo_B = [
        [1],
        [0],
        [0,3,6],
        [],
        [1,7],
        [4],
        [7],
        [6]
    ]
    
    print("El grafo B es" + (" no " if es_grafo_no_dirigido(grafo_B) else " ") + "dirigido")
    print(recorrido_en_profundidad(grafo_B))
    
    # Grafo dirigido
    grafo_C = [
        [1],
        [0],
        [0,3],
        [2,4],
        [1]
    ]

    print("El grafo C es" + (" no " if es_grafo_no_dirigido(grafo_C) else " ") + "dirigido")
    print(recorrido_en_profundidad(grafo_C))
    
    # Grafo no dirigido
    grafo_D = [
        [1,2],
        [0,2,3],
        [0,1,3,4],
        [1,2,4],
        [2,3],
    ]

    print("El grafo D es" + (" no " if es_grafo_no_dirigido(grafo_D) else " ") + "dirigido")
    print(recorrido_en_profundidad(grafo_D))

if __name__ == "__main__":
    main()