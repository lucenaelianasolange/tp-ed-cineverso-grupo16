import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from estructuras.grafo import Grafo

grafo=Grafo()

grafo.agregar_vertice("Interestelar")
grafo.agregar_vertice("Matrix")
grafo.agregar_vertice("Avatar")
grafo.agregar_vertice("Inception")

grafo.agregar_arista("Interestelar", "Matrix", 5)
grafo.agregar_arista("Interestelar", "Avatar", 3)
grafo.agregar_arista("Matrix", "Avatar", 4)
grafo.agregar_arista("Inception", "Matrix", 2)

grafo.mostrar_grafo()

print("Recomendaciones para Interestelar: ")
print(grafo.obtener_recomendaciones("Interestelar"))
print("/nAristas del grafo: ")
print(grafo.obtener_aristas())

print("/nRecomendaciones para Matrix: ")
print(grafo.obtener_recomendaciones("Matrix"))