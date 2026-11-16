## Analisis tp6, tp7 y tp8 - Heap - Grafos - DFS y BFS

# Algoritmos incorporado

Se incorporo la implementacion de estructuras Heap, Grafos, ubicadas en la carpeta de estructuras, DFS y BFS, ubicadas en la carpeta de algoritmos, aunque en sus estados actuales, NO SE ENCUENTRAN INTEGRADAS CON LAS FUNCIONALIDADES DEL SISTEMA.

# Heap
## ¿Que es un Heap?
Es una estructura de datos que nos organiza los elementos segun su prioridad, permitiendo acceder rapidamente al elemento mas importante.
La estructura permite insertar elementos, consultar el elemento prioritario y extraerlo respetando las propiedades del Heap.

## Grafo
## ¿Que es un grafo?
Es una estructura de datos formada por nodos y aristas que representan relaciones entre elementos.


· En nuestro proyecto, buscamos que Cineverso pueda recomendar peliculas relacionadas con los gustos y preferencias del usuario, en donde; cada nodo represente una pelicula y las aristas las relaciones que existen entre ellas, como por ejemplo genero, director, etc.
Actualmente, incluimos la estructura basica del Grafo, pero todavia no esta conectada con el sistema de recomendaciones.


# BFS
## ¿Que es un BFS?
(busqueda en anchura) Es un algoritmo que recorre un grafo por niveles, visitando primero los nodos mas cercanos al punto de partida. 

# DFS
## ¿que es un DFS?
(Busqueda en profundidad) Es un algoritmo que recorre un grafo explorando un camino hasta el final antes de regresar y buscar otras conexiones.


## Futuras integraciones al proyecto
Nuestra idea es mantener el arbol binario de busqueda para que el usuario realice busquedas de peliculas por titulo, aprovechando su organizacion para facilitar la localizacion de elementos.
Por otro lado, queremos utilizar grafos como base para desarrollar el sistema de recomendaciones que permita relacionar peliculas segun sus caracteristicas.
En esta etapa, las cuatro implementaciones se  encuentran desarrolladas independientemente, sin conexion con la interfaz.
