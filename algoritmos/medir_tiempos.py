from modelos.peliculas import Pelicula

import random

from estructuras.arbol import ArbolBST

import timeit

import json

# dataset

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

        pelicula = Pelicula(

            titulo=f"Película {i}",

            director=random.choice(directores),

            anio=random.randint(1980, 2025),

            genero=random.choice(generos)

        )

        peliculas.append(pelicula)

    return peliculas

N_DATOS = 10000

list_peliculas = generar_peliculas(N_DATOS)

random.shuffle(list_peliculas)


N = 100

arbol = ArbolBST()


tiempo_secuencial = timeit.timeit(lambda:Pelicula.busqueda_secuencial(list_peliculas,'Película 1'),number=N)
tiempo_binario = timeit.timeit(lambda:arbol.busuqueda('Película 1', lambda p: p.titulo.lower()),number=N)


print(f"tiempor en busqueda secuencial {tiempo_secuencial}")
print(f"tiempor en busqueda en arbol binario {tiempo_binario} ")


print(f"Secuencial promedio: {tiempo_secuencial/N:.8f} s")
print(f"Árbol promedio:       {tiempo_binario/N:.8f} s")