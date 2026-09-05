from modelos.peliculas import Pelicula
import json

def cargar_datos():
    with open("datos/peliculas.json", "r", encoding="utf-8") as f:
        datos = json.load(f)
        peliculas= []
        for d in datos:
            peliculas.append(Pelicula(d["titulo"], d["director"], d["año"], d["genero"]))
        return peliculas

def mostrar_menu():
    print("Bienvenido al Universo del Cine")
    print("=== Menú de Cineverso ===")
    print("1. Mostrar todas las películas")
    print("2. Buscar película por título")
    print("3. Buscar pelicula por filtro")
    print("4.Ver recomendaciones de películas")
    print("5. Ver historial de búsquedas")
    print("6.Borrar historial de búsquedas")
    print("7. Salir")

def Buscar(peliculas):
    titulo = input("titulo a buscar:")
    for p in peliculas:
        if titulo.lower() in p.titulo.lower():
            print(p)

    # print("fin de resultado") 
