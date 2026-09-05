#Propuesta del proyecto


#Nombre del proyecto:
(Cineverso)


#Dominio elegido:
(Cine)
(Nuestro dominio elegido es el  cine, ya que es un Area en comun entre los integrantes del grupo, fue sometido a votacion.)


#Problematica que resuelve:
(Scroll infinito)
(Eleccion rapida y eficaz en un gran catalogo de peliculas.)
(El proyecto busca reducir el tiempo de busqueda y facilitar la eleccion de una pelicula, ofreciendo opciones de genero y actores basados en recomendaciones segun el historial del ususario.)


#Usuario Objetivo
(Personas de 15 a 60 años, con diversos gustos cinematograficos o aquellos que esten abiertos a descubrir nuevos generos de peliculas.)


#Funciones iniciales:
#1: Listar todos los elementos.
#2: Buscar Elementos por titulo.
#3: Listar por Filtro: 
(Genero)
(Actor)
(Director)
(Año)
#4: Historial depeliculas vistas.
#5: Peliculas recomendadas:
(Genero)
(Actor)
(Director)
(Año)
(Sal de tu zona de confort)
#6: Borrar historial.

#Ejemplo de interaccion:

###################################
#           CINEVERSO              #
#                                  #
# Bienvenido al Universo del Cine  #
#                                  #
#      Elija su opcion:            #
#                                  #
#     1-Ver listado                #
#     2-Buscar Pelicula            #
#     3-Buscar por Filtro          #
#     4-Ver Recomendaciones        #
#     5-Ver Historial              #
#     6-Borrar Historial           #
#     7-Salir                      #                
###################################


#Diagramadeclases 

┌─────────────────────────────┐
                    │          Interface          │
                    ├─────────────────────────────┤
                    │                             │
                    │ + mostrarInterfaz()         │
                    │ + cerrarInterfaz()          │
                    │                             │
                    └─────────────────────────────┘


┌─────────────────────────────┐              ┌─────────────────────────────┐
│          Películas          │              │           Cliente           │
├─────────────────────────────┤              ├─────────────────────────────┤
│ - id: number                │              │ - id: number                │
│ - title: string             │              │ - nombre: string            │
│ - director: string          │              │ - historial: []             │
│ - lanzamiento: number       │              │                             │
│ - genero: [string]          │              ├─────────────────────────────┤
│ - reparto: []               │              │                             │
├─────────────────────────────┤              │ watchMovie()                │
│                             │              │ removeMovie()               │
│ - searchMovie()             │              │ rateMovie()                 │
│ - filterMovie(atributo)     │              │ recommendMovie()            │
│ - createMovie()             │              │ recommendHistorial()        │
│ - deleteMovie()             │              │                             │
└─────────────────────────────┘              └─────────────────────────────┘
             │                                      │
             │                                      │
             └────────────── 0..* ──────────────────┘
                              1