from modelos.peliculas import Pelicula

import random

from estructuras.arbol_binario import ArbolBST

import timeit

#dataset
class PeliculaTest(Pelicula):
    def busqueda_secuencial(lista,pelicula):
        for p in lista:
            if pelicula == p.titulo.lower():
                print("ddssssss")
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

        pelicula = PeliculaTest(

            titulo=f"Pelicula {i}",

            director=random.choice(directores),

            anio=random.randint(1980, 2025),

            genero=random.choice(generos)

        )

        peliculas.append(pelicula)
        arbol.insertar(pelicula,lambda p:p.titulo.lower())

    return peliculas

#Cantidad de Peliculas
N_DATOS = 100

list_peliculas = generar_peliculas(N_DATOS)

random.shuffle(list_peliculas)



#Cantidad de veces que se repite
N = 1

result_secuencial = PeliculaTest.busqueda_secuencial(list_peliculas,"pelicula 1")
resul_binario = arbol.buscar('pelicula 1', lambda p: p.titulo.lower())

print(result_secuencial,"secuencial")

print(resul_binario,"binario")

tiempo_secuencial = timeit.timeit(lambda:PeliculaTest.busqueda_secuencial(list_peliculas,'pelicula 1'),number=N)
tiempo_binario = timeit.timeit(lambda:arbol.buscar('pelicula 1', lambda p: p.titulo.lower()),number=N)


print(f"tiempo en busqueda secuencial {tiempo_secuencial:.8f}")
print(f"tiempo en busqueda en arbol binario {tiempo_binario:.8f} ")


print(f"Secuencial promedio: {tiempo_secuencial/N:.8f} s")
print(f"Árbol promedio:       {tiempo_binario/N:.8f} s")

