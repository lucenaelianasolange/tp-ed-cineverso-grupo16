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
    titulo = input("titulo a buscar: ")
    for p in peliculas:
        if titulo.lower() in p.titulo.lower():
            print(p)
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
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            buscar(peliculas)
        elif opcion == "2":
            listar(peliculas)
        elif opcion == "3":
            filtrar(peliculas)
        elif opcion == "4":
            print("Funcionalidad de recomendaciones aún no implementada.")
        elif opcion == "5":
            print("Funcionalidad de historial aún no implementada.")
        elif opcion == "6":
            print("Funcionalidad de borrar historial aún no implementada.")
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")
if __name__ == "__main__":
    main()