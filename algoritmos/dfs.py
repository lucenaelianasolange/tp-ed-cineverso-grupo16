def dfs(grafo, inicio):
    if not grafo.existe_vertice(inicio):
        raise ValueError(f"El vértice {inicio} no existe en el grafo.")
    visitados = set()
    pila = [inicio]
    recorrido = []

    while pila:
        vertice = pila.pop()
        if vertice not in visitados:
            visitados.add(vertice)
            recorrido.append(vertice)
            for adyacente in grafo.aristas.get(vertice, []):
                if adyacente not in visitados:
                    pila.append(adyacente)

    return recorrido