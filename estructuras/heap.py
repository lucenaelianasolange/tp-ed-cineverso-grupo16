class Heap:
    def __init__(self, max_heap=True):
        self.elementos = []
        self.max_heap = max_heap

    def _tiene_prioridad(self, i , j):
        if self.max_heap:
            return self.elementos[i] > self.elementos[j]
        else:
            return self.elementos[i] < self.elementos[j]

    def insertar(self, prioridad, elemento):
        self.elementos.append((prioridad, elemento))
        self._flotar(len(self.elementos) - 1)

    def _subir(self, indice):
        while indice > 0:
            padre = (indice - 1) // 2
            if self._tiene_prioridad(indice, padre):
                self.elementos[indice], self.elementos[padre] = self.elementos[padre], self.elementos[indice]
                indice = padre
            else:
                break

    def extraer(self):
        if self.es_vacio():
            raise IndexError("El heap está vacío.")
        if len(self.elementos) == 1:
            return self.elementos.pop()
        raiz = self.elementos[0]
        self.elementos[0] = self.elementos.pop()
        self._bajar(0)

    def _bajar(self, indice):
        while True:
            hijo_izquierdo = 2 * indice + 1
            hijo_derecho = 2 * indice + 2
            mayor = indice

            if hijo_izquierdo < len(self.elementos) and self._tiene_prioridad(hijo_izquierdo, mayor):
                mayor = hijo_izquierdo
            if hijo_derecho < len(self.elementos) and self._tiene_prioridad(hijo_derecho, mayor):
                mayor = hijo_derecho

            if mayor == indice:
                break

            self.elementos[indice], self.elementos[mayor] = self.elementos[mayor], self.elementos[indice]
            indice = mayor

    def consultar_maximo(self):
        if self.es_vacio():
            raise IndexError("El heap está vacío.")
        return self.elementos[0]

    def esta_vacio(self):
        return len(self.elementos) == 0

    def tamano(self):
        return len(self.elementos)
    