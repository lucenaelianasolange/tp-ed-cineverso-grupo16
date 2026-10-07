# Análisis TP4 + TP5 — AVL y Árbol General

## ¿Qué resolvimos?

En esta etapa incorporamos dos estructuras de datos que resuelven problemas distintos dentro del
sistema:

|Estructura|Problema que resuelve |Donde se usa|
|-----------|-----------|-----------|
|AVL|Que las búsquedas por título/clave sean siempre rápidas (O(log n)) incluso cuando los datos se insertan en orden| Opcion "Buscar" del menú
|Arbol General | Representar la ferarquía de categoría del dominio| Opción "Explorar categorías" del menu

## Árbol AVL
### ¿Por qué AVL y no un BST común?

Un BST común se desbalancea cuando se insertan datos ordenados (ej: títulos en orden alfabético). Esto lo
convierte en una lista enlazada con complejidad O(n) por búsqueda. El AVL resuelve esto con rotaciones
automáticas que mantienen la altura en O(log n) sin importar el orden de inserción.

### Rotaciones implementadas    
| tipo | casos | cuando se aplica|
|-----------|-----------|-----------|
|Rotación simple derecha|Izquierda- Izquierda| Factor de balance > 1 y el nuevo dato va a la izquierda del hijo izquierdo
|Rotación simple izquierda|Derecha- Derecha|Factor de balance < -1 y el nuevo dato va a la derecha del hijo derecho
|Rotación doble izquierda-derecha|Izquierda-Derecha|Factor de balance > 1 pero el hijo izquierdo está desbalanceado a la derecha
|Rotación doble derecha-izquierda|Derecha-Izquierda|Derecha-Izquierda

### Casos de desbalances generado
se insertaron datos en orden numerioco desmostrando el peor caso para un BST comun y demostramos que el AVL mantiene la atura controlada
datos de prueva 
$$1,2,3,4,5,6,7,8,9, ...900$$

## Comparacion bst vs avl

|metricas|BST comun|AVL|
|Altura con arvol Ordenado|||
|Busqueda con 900 datos Ordenados|||
|complejidad peor caso de busqueda|||
|complejidad promedio de insercion|||


se utilizaron 900 elementos ordenados para mostrar la diferencia entre un tiempo de ejecucion y otro, no se usaron cadena de texto porque tenian que ser exactamente de la misma longitud ya que python al comparar usa caracter por caracter teniendo bug a la hora de usar letras y numeros juntos 

## Errores que tuvimos 

a la hora de importar el arbol avl tivimos errores de importacion de la cual tivimos que modificar las importaciones de pruevas,
errores de implementacion, en probar_avl.py y medir_tiempo , las estructuras son capaces de comprovar si "matrix y jumanjy" y ordenarlas pero a la hora de comparar "10" "2" y "1" los ordena "1" "10"  "2"

  Altura BST: 900
  Altura AVL: 10
  BST es más alto que AVL: True
  Tiempo búsqueda BST (ms): 165.3621
  Tiempo búsqueda AVL (ms): 0.9971

## Datos de prueba
##script de prueba:

Géneros
├── Acción
│   ├── acción
│   ├── acción y aventura
│   └── guerra
│
├── Ciencia ficción
│   ├── ciencia ficción
│   ├── ficción
│   ├── ciencia ficción y fantasía
│   ├── fantasía
│   ├── espacio
│   └── futuro
│
├── Amor
│   ├── amor
│   ├── romántica
│   └── romance
│
├── Comedia
│   ├── comedia
│   └── comedia romántica
│
├── Animadas
│   ├── animadas
│   ├── dibujos animados
│   ├── anime
│   ├── animación
│   └── animación 3d
│
└── Suspenso
    ├── suspenso
    ├── thriller
    ├── misterio
    ├── suspense
    ├── terror
    ├── drama
    └── drama psicológico
