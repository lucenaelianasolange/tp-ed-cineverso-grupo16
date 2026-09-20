# Análisis TP3 — Árbol Binario de Búsqueda

## 1. ¿Qué resolvimos?
Se implemento la integracion de la funcionalidad de "Busqueda por titulo" del menu con un arbol Binario de Busqueda, en donde las Peliculas se almacenan en el Arbol utilizando el titulo como criterio de ordenamiento.

## 2. Clave de ordenamiento
La clave de ordenamiento utilizada es el Titulo dela Pelicula, debido a que este es el criterio mediante el cual el usuario realiza la busqueda.

## 3. Prueba del árbol
Altura del arbol: 4

---inorder (ordenado alfabeticamente)---
    Arribal (rating 8.4)
    Blade Runner (rating 8.5)
    Inception (rating8.8)
    Matrix (rating 9.0)
    Titanic(rating 7.8)

---preorder---
    Matrix
    Inception
    Blade Runner
    Arrival
    Titanic

---postorder---
    Arrival
    Blade Runner
    Inception
    Titanic
    Matrix

---busquedas---
Buscar "matrix : Matrix(rating 9.0)
Buscar "zzz": None
## 4. Comparación de tiempos
En la tabla siguiente, los tiempos son **reales**, sacados con nuestro
script `algoritmos/medir_tiempos.py`
| N elementos | Secuencial (ms) | Binaria (ms) | Árbol BST (ms) |
|---|---:|---:|---:|
| 100 | [0.00010840] | [0.00001030] | [x] |
| 1.000 | [0.00037710] | [0.00001200] | [x] |
| 10.000 | [0.00051390] | [0.00000990] | [x] |
| 100.000 | [0.01456880] | [0.00001490] | [x] |

## 5. Análisis de complejidad
- **Búsqueda secuencial:** O(n). Recorre toda la lista en el peor caso.
- **Búsqueda binaria:** O(log n) pero exige lista ordenada (ordenar cuesta O(n log n) una s
- **Búsqueda en árbol:** O(log n) promedio si el árbol está balanceado;
O(n) en el peor caso si está degenerado (como una lista).
- **Inserción en árbol:** O(log n) promedio, O(n) peor caso.
- **Recorridos (inorder, preorder, postorder):** O(n), porque visitan cada nodo 1 vez.

## 6. Conclusión
En conclusión, podemos ver que el método secuencial y el árbol tienen diferentes tiempos de búsqueda. A medida que aumenta la cantidad de elementos, el árbol resulta más rápido para encontrar información.Aunque crear el árbol lleva un tiempo al principio, este costo se compensa cuando se realizan muchas búsquedas.

## 7. Errores o dudas que tuvimos
Tuvimos dificultades para realizar las pruebas de medicion de tiempos.