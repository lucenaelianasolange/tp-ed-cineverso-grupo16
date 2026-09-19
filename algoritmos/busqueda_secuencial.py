#BUSQUEDA SECUENCIAL

print("BUSQUEDA SECUENCIAL")


class Pelicula:
    def __init__(self,titulo):
        self.titulo = titulo

    def __repr__(self):
        return f"Pelicula({self.titulo})"



def busqueda_secuencial(lista,titulo_buscado):
    for pelicula in lista:
        if pelicula.titulo.lower() == titulo_buscado.lower():
            return pelicula
        else:
            return None

#main
if __name__ == "__main__":
    peliculas =  [
        Pelicula("Matrix"),
        Pelicula("Inception"),
        Pelicula("Interestelar"),
        Pelicula("Titanic"),
        Pelicula("Avatar")
    ]
    print("Lista de peliculas: ")
    for p in peliculas:
        print(" -", p.titulo)

    print ("------ Pruebas -----")

    resultado= busqueda_secuencial(peliculas, "Inception")
    print("Buscando Inception: ", resultado)

    resultado= busqueda_secuencial(peliculas,"Matrix")
    print("Buscando Matrix: ", resultado)

    resultado=busqueda_secuencial(peliculas, "El padrino")
    print("Buscando El padrino: ", resultado)


print("Busqueda Binaria")
#BUSQUEDA BINARIA
class Nodo:
    def __init__(self,pelicula):
        self.pelicula= pelicula
        self.izquierda= None
        self.derecha= None

class BT:
    def __init__(self):
        self.raiz= None

    def insertar(self, pelicula):
        if self.raiz is None:
            self.raiz= Nodo(pelicula)
        else:
            self._insertar_recursivo(self.raiz, pelicula)

    def _insertar_recursivo(self, nodo_actual, pelicula):
        if pelicula.titulo < nodo_actual.pelicula.titulo:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda= Nodo(pelicula)
            else:
                self._insertar_recursivo(nodo_actual.izquierda, pelicula)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha= Nodo(pelicula)
            else:
                self._insertar_recursivo(nodo_actual.derecha, pelicula)

    def buscar(self, titulo_buscado):
        return self._buscar_recursivo(self.raiz, titulo_buscado)

    def _buscar_recursivo(self, nodo_actual, titulo_buscado):
        if nodo_actual is None:
            return None
        if nodo_actual.pelicula.titulo.lower() == titulo_buscado.lower():
            return nodo_actual.pelicula
        elif titulo_buscado < nodo_actual.pelicula.titulo:
            return self._buscar_recursivo(nodo_actual.izquierda, titulo_buscado)
        else:
            return self._buscar_recursivo(nodo_actual.derecha, titulo_buscado)

#main
if __name__ == "__main__":
    peliculas = [
        Pelicula("Matrix"),
        Pelicula("Inception"),
        Pelicula("Interestelar"),
        Pelicula("Titanic"),
        Pelicula("Avatar")
    ]

    arbol = BT()
    for p in peliculas:
        arbol.insertar(p)

    print("Lista de peliculas: ")
    for p in peliculas:
        print(" -", p.titulo)

    print("\n------ Pruebas -----")

    resultado = arbol.buscar("Inception")
    print("Buscando Inception: ", resultado)

    resultado = arbol.buscar("Matrix")
    print("Buscando Matrix: ", resultado)

    resultado = arbol.buscar("El padrino")
    print("Buscando El padrino: ", resultado)