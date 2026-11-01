from collections import deque

def bfs(grafo, inicio):
    if not grafo.existe_vertice(inicio):
        raise ValueError(f"El vértice {inicio} no existe en el grafo.")
    visitados = set()
    cola = deque([inicio])
    recorrido = []
    
    visitados.add(inicio)

    while cola:
        vertice = cola.popleft()
        if vertice not in visitados:
            visitados.add(vertice)
            recorrido.append(vertice)
            for adyacente in grafo.aristas.get(vertice, []):
                if adyacente not in visitados:
                    cola.append(adyacente)

    return recorrido