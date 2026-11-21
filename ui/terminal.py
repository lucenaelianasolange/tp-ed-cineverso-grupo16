from estructuras.arbol_general import ArbolGeneral
from modelos.peliculas import Pelicula
import json

from estructuras.avl import AVL
from estructuras.grafo import Grafo
from algoritmos.bfs import bfs
from algoritmos.dfs import dfs


    
class Terminar():
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self):
        return f"Hola: {self.nombre}, Bienbenido a Cineverso \n {self.descripcion}"

    def mostrar_menu(self):
        print("#"*40)
        print("Bienvenido al Universo del Cine")
        print("=== Menú de Cineverso ===")
        print("1. Mostrar todas las películas")
        print("2. Buscar película por título")
        print("3. Buscar pelicula por categoria")
        print("4.Ver recomendaciones de películas")
        print("5. Ver historial ")
        print("6.Borrar historial de búsquedas")
        print("7. Salir")
        print("#"*40)

    def listar(self, peliculas):
        for i, p in enumerate(peliculas, 1):
            print(f"{i}. {p}")

    def buscar(self, arbol):
        titulo = input("titulo a buscar: ")
        resultado = arbol.buscar(titulo.lower(), clave=lambda e: e.titulo.lower())
        if resultado:
            print("pelicula encontrada: ", resultado)
        else:
            print("No se encontró la película.")
        print("fin de resultados")


    def mostrar_categorias(self, nodo, nivel=0):
        """Muestra las categorías del árbol general de manera jerárquica."""
        if nodo is None:
            return
        print("     " * nivel + f"- {nodo.dato}")
        for hijo in nodo.hijos:
            self.mostrar_categorias(hijo, nivel + 1)

    def explorar_categoria(self, arbol_general):
        # peticion al arbol_general para buscar las peliculas
        nombre = input("Ingrese el género a explorar: ")
        nodo = arbol_general.buscar(nombre.lower())
        if nodo is None:
            print(f"Género '{nombre}' no encontrado en el árbol.")
            return
        peliculas = arbol_general.peliculas_de_rama(nodo)
        for i in peliculas:
            print(i)
                
    def filtrar(self, peliculas):
        genero = input("Ingrese el género a filtrar: ")
        for p in peliculas:
            if genero.lower() in p.genero.lower():
                print(p)

    def repetir_accion(self, accion,texto):
        while True:
            accion()
            continuar = input(f"¿Desea {texto}? (s/n): ")
            if continuar.lower() == "s":
                continue
            elif continuar.lower() == "n":
                break
            else:
                print("Opción inválida. Por favor, ingrese 's' o 'n'.")



def cargar_datos():
    with open("datos/peliculas.json", "r", encoding="utf-8") as f:
        datos = json.load(f)
        peliculas= []
        for d in datos:
            peliculas.append(Pelicula(d["titulo"], d["director"], d["anio"], d["genero"]))
        return peliculas


def crear_grafo(peliculas):
    grafo=Grafo()
    for pelicula in peliculas:                    #agregar todas las peliculas como vertices
        grafo.agregar_vertice(pelicula.titulo) 
    for i, pelicula1 in enumerate (peliculas):     #conectar peliculas que tengan el mismo genero
        for pelicula2 in peliculas[i+1:]:
            if pelicula1.genero.strip().lower() == pelicula2.genero.strip().lower():
                grafo.agregar_arista(pelicula1.titulo, pelicula2.titulo, 10)  
    return grafo

def recomendar_peliculas(grafo):
    titulo=input("Ingrese el título de la película para obtener recomendaciones: ")
    pelicula=next ( (p for p in grafo.vertices if p.lower() == titulo.strip().lower()),
    None)
    if pelicula is None:
        print("La película no se encuentra en el grafo.")
        return
    
    recomendaciones = grafo.obtener_recomendaciones(pelicula)    

    if not recomendaciones:
        print("No hay recomendaciones disponibles para esta película.")
        return
    print(f"Recomendaciones para '{pelicula}':")
    for titulo,peso in recomendaciones:
        print(f"- {titulo} (peso: {peso})") 




def main ():
    terminar = Terminar("Usuario", "Cineverso es una aplicación para explorar películas y géneros cinematográficos.")
    print(terminar)

    # dataset
    peliculas = cargar_datos()

    # estructuras de datos
    arbol = AVL()
    arbol_general = ArbolGeneral()
    grafo=crear_grafo(peliculas)

    # categorias 
    arbol_general.insertar_raiz("Películas")

    generos = arbol_general.agregar_hijo(arbol_general.raiz, "generos")

    #generos
    accion = arbol_general.agregar_hijo(generos, "accion")
    ciencia_ficcion = arbol_general.agregar_hijo(generos, "ciencia ficción")
    arbol_general.agregar_hijo(generos, "aventura")
    amor = arbol_general.agregar_hijo(generos, "amor")
    arbol_general.agregar_hijo(generos, "comedia")
    animadas = arbol_general.agregar_hijo(generos, "animadas")
    suspenso = arbol_general.agregar_hijo(generos, "suspenso")

    # sub-genero
    arbol_general.agregar_hijo(accion, "superheroes")
    arbol_general.agregar_hijo(accion, "guerra")
    arbol_general.agregar_hijo(accion, "policías")
    arbol_general.agregar_hijo(ciencia_ficcion, "fantasía")
    arbol_general.agregar_hijo(ciencia_ficcion, "espacio")
    arbol_general.agregar_hijo(ciencia_ficcion, "futuro")
    arbol_general.agregar_hijo(amor, "romcom")
    arbol_general.agregar_hijo(animadas, "anime")
    arbol_general.agregar_hijo(suspenso, "misterio")
    arbol_general.agregar_hijo(suspenso, "terror")
    arbol_general.agregar_hijo(suspenso, "thriller")
    







    # insercion de las peliculas
    for pelicula in peliculas:
        # Insertar en el árbol AVL
        arbol.insertar(pelicula, clave=lambda e: e.titulo.lower())

        # Insertar en el árbol general según el género
        arbol_general.agregar_pelicula(pelicula.genero, pelicula)


    print("Acción:", len(arbol_general.peliculas_de_rama(accion)))
    print("Total en el árbol:", len(arbol_general.peliculas_de_rama(generos)), "de", len(peliculas))
        


    while True:
        terminar.mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            terminar.listar(peliculas)

        elif opcion == "2":
            terminar.buscar(arbol)
        
        elif opcion == "3":
            terminar.repetir_accion(lambda: terminar.explorar_categoria(arbol_general), "explorar otra categoría")

        elif opcion == "4":
            recomendar_peliculas(grafo)

        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
                print("Opción inválida. Por favor, intente nuevamente.")
