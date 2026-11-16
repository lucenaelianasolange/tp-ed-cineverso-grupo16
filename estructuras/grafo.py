class Grafo:
    def __init__(self):
        self.vertices = {}
        self.aristas = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []
            self.aristas[vertice] = []

    def agregar_arista(self, vertice1, vertice2):
        if vertice1 in self.vertices and vertice2 in self.vertices:
            self.aristas[vertice1].append(vertice2)
            self.aristas[vertice2].append(vertice1)  # Para grafos no dirigidos

    def obtener_vertices(self):
        return list(self.vertices.keys())

    def obtener_aristas(self):
        aristas = []
        for vertice, adyacentes in self.aristas.items():
            for adyacente in adyacentes:
                if (adyacente, vertice) not in aristas:  # Evitar duplicados
                    aristas.append((vertice, adyacente))
        return aristas
    def mostrar_grafo(self):
        for vertice, adyacentes in self.aristas.items():
            print(f"{vertice}: {adyacentes}")

    def buscar_camino(self, inicio, fin, camino=[]):
        camino = camino + [inicio]
        if inicio == fin:
            return camino
        if inicio not in self.aristas:
            return None
        for vertice in self.aristas[inicio]:
            if vertice not in camino:
                nuevo_camino = self.buscar_camino(vertice, fin, camino)
                if nuevo_camino:
                    return nuevo_camino
        return None
    
    def existe_camino(self, inicio, fin):
        return self.buscar_camino(inicio, fin) is not None
    
    def existe_vertice(self, vertice):
        return vertice in self.vertices