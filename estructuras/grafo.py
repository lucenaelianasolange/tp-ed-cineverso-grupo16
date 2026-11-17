class Grafo:
    def __init__(self):
        self.vertices = {}
        self.aristas = {}

    def agregar_vertice(self, pelicula):
        if pelicula not in self.vertices:
            self.vertices[pelicula] = True
            self.aristas[pelicula] = {}

    def agregar_arista(self, pelicula1, pelicula2, peso):
        if pelicula1 in self.vertices and pelicula2 in self.vertices:
            self.aristas[pelicula1] [pelicula2]=peso
            self.aristas[pelicula2] [pelicula1]=peso 

    def obtener_recomendaciones(self, pelicula):
        if pelicula not in self.vertices:
            return []
        recomendaciones= []

        for otra_pelicula, peso in self.aristas [pelicula].items():
            recomendaciones.append((otra_pelicula, peso))

        recomendaciones.sort(key=lambda x:x[1], reverse=True)
        return recomendaciones

    def mostrar_grafo(self):
        for pelicula, conexiones in self.aristas.items():
            print (f"{pelicula}: {conexiones}")

    def obtener_aristas(self):
        aristas = []
        for vertice, adyacentes in self.aristas.items():
            for adyacente, peso in adyacentes.items():
                if (adyacente, vertice) not in [(a[0], a[1]) for a in aristas]:  # Evitar duplicados
                    aristas.append((vertice, adyacente, peso))
        return aristas
  
    def buscar_camino(self, inicio, fin, camino=None):
        if camino is None:
            camino = []
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