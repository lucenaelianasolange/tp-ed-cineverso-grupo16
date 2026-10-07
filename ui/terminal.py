from estructuras.arbol_general import ArbolGeneral
from modelos.peliculas import Pelicula
import json

from estructuras.avl import AVL

def cargar_datos():
    with open("datos/peliculas.json", "r", encoding="utf-8") as f:
        datos = json.load(f)
        peliculas= []
        for d in datos:
            peliculas.append(Pelicula(d["titulo"], d["director"], d["anio"], d["genero"]))
        return peliculas

def mostrar_menu():
    print("#"*40)
    print("Bienvenido al Universo del Cine")
    print("=== Menú de Cineverso ===")
    print("1. Mostrar todas las películas")
    print("2. Buscar película por título")
    print("3. Buscar pelicula por filtro")
    print("4.Ver recomendaciones de películas")
    print("5. Ver historial de búsquedas")
    print("6.Borrar historial de búsquedas")
    print("7. Salir")
    print("#"*40)

def mostrar_generos(arbol_general):
    aux = 0
    if arbol_general.raiz is None:
        print("El árbol general está vacío.")
        return
    else:
        print("Géneros disponibles:")
        for hijo in arbol_general.raiz.hijos:
            print(f"-{aux + 1} {hijo.dato}")
    

def buscar(arbol):
    titulo = input("titulo a buscar: ")
    resultado = arbol.buscar(titulo.lower(), clave=lambda e: e.titulo.lower())
    if resultado:
        print("pelicula encontrada: ", resultado)
    else:
        print("No se encontró la película.")
    print("fin de resultados")


def listar(peliculas):
    for i, p in enumerate(peliculas, 1):
        print(f"{i}. {p}")

def filtrar(peliculas):
    genero = input("Ingrese el género a filtrar: ")
    for p in peliculas:
        if genero.lower() in p.genero.lower():
            print(p)

def main ():
    peliculas = cargar_datos()
    arbol = AVL()
    arbol_general = ArbolGeneral()

    arbol_general.insertar_raiz("Películas")
    accion = arbol_general.agregar_hijo(arbol_general.raiz, "Acción")
    ciencia = arbol_general.agregar_hijo(arbol_general.raiz, "Ciencia Ficción")
    amor = arbol_general.agregar_hijo(arbol_general.raiz, "Amor")
    comedia = arbol_general.agregar_hijo(arbol_general.raiz, "Comedia")
    animadas = arbol_general.agregar_hijo(arbol_general.raiz, "Animadas")
    suspenso = arbol_general.agregar_hijo(arbol_general.raiz, "Suspenso")


    for pelicula in peliculas:
        arbol.insertar(pelicula, clave=lambda e: e.titulo.lower())
        if pelicula.genero.lower() in ["acción", "acción y aventura", "acción","guerra"]:
            arbol_general.agregar_hijo(accion, pelicula.titulo)
        elif pelicula.genero.lower() in ["ciencia ficción", "ficción", "ciencia ficción y fantasía", "fantasia","espacio", "futuro"]:
            arbol_general.agregar_hijo(ciencia, pelicula.titulo)
        elif pelicula.genero.lower() in ["amor", "romántica", "romance"]:
            arbol_general.agregar_hijo(amor, pelicula.titulo)
        elif pelicula.genero.lower() in ["comedia", "comedia romántica"]:
            arbol_general.agregar_hijo(comedia, pelicula.titulo)
        elif pelicula.genero.lower() in ["animadas", "dibujos animados", "anime", "animación", "animación 3d"]:
            arbol_general.agregar_hijo(animadas, pelicula.titulo)
        elif pelicula.genero.lower() in ["suspenso", "thriller", "misterio", "suspense", "terror", "drama", "drama psicológico"]:
            arbol_general.agregar_hijo(suspenso, pelicula.titulo)


    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            listar(peliculas)
        elif opcion == "2":
            buscar(arbol)
        elif opcion == "3":
            filtrar(peliculas)
        elif opcion == "4":
            mostrar_generos(arbol_general)
            genero = input("Ingrese el género a filtrar: ")
            match genero:
                case "1":
                    for hijo in accion.hijos:
                        print(hijo.dato)
                case "2":
                    for hijo in ciencia.hijos:
                        print(hijo.dato)
                case "3":
                    for hijo in amor.hijos:
                        print(hijo.dato)
                case "4":
                    for hijo in comedia.hijos:
                        print(hijo.dato)
                case "5":
                    for hijo in animadas.hijos:
                        print(hijo.dato)
                case "6":
                    for hijo in suspenso.hijos:
                        print(hijo.dato)
                case _:
                    print("Género no válido.")

            # print aplitur
            rsult = arbol_general.amplitud()
            print(rsult)

        elif opcion == "5":
            print("Funcionalidad de historial aún no implementada.")
        elif opcion == "6":
            print("Funcionalidad de borrar historial aún no implementada.")
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")
