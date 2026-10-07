from modelos.peliculas import Pelicula
import random
from estructuras.arbol_binario import ArbolBST
import timeit

#dataset
class PeliculaTest(Pelicula):
    def busqueda_secuencial(lista,anio):
        for p in lista:
            if anio == p.anio:

                print(p)
                return p

arbol = ArbolBST()


def generar_peliculas(cantidad):
    directores = [

        "Christopher Nolan",
        "Steven Spielberg",
        "James Cameron",
        "Martin Scorsese",
        "Quentin Tarantino"

    ]

    generos = [

        "Acción",
        "Comedia",
        "Drama",
        "Terror",
        "Ciencia ficción"
    ]

    peliculas = []

    for i in range(cantidad):
        aux = i
        pelicula = PeliculaTest(

            titulo=f"Pelicula {i}",

            director=random.choice(directores),

            anio=aux,

            genero=random.choice(generos)

        )

        peliculas.append(pelicula)

    return peliculas

#Cantidad de Peliculas
N_DATOS = 1000

list_peliculas = generar_peliculas(N_DATOS)

random.shuffle(list_peliculas)

for p in list_peliculas:
    arbol.insertar(p, lambda p: p.titulo.lower())


#Cantidad de veces que se repite
N = 1


tiempo_secuencial = timeit.timeit(lambda:PeliculaTest.busqueda_secuencial(list_peliculas,100),number=N)
tiempo_binario = timeit.timeit(lambda:arbol.buscar("pelicula 100", lambda p: p.titulo.lower()),number=N)


busqueda_secuencial = PeliculaTest.busqueda_secuencial(list_peliculas,100)
busqueda_arbol = arbol.buscar("pelicula 100", lambda p: p.titulo.lower())   

print(f"Resultado busqueda secuencial: {busqueda_secuencial}")
print(f"Resultado busqueda arbol: {busqueda_arbol}")


print(f"tiempo en busqueda secuencial {tiempo_secuencial:.8f}")
print(f"tiempo en busqueda en arbol binario {tiempo_binario:.8f} ")


print(f"Secuencial promedio: {tiempo_secuencial/N:.8f} s")
print(f"Árbol promedio:       {tiempo_binario/N:.8f} s")

print(f"Altura del árbol BST: {arbol.altura()}")

