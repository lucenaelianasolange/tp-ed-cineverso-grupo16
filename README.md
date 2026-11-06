# Cineverso
Permite al usuario buscar,consultar y filtrar las peliculas ayudandolos a encontrar la mejor optción que se adapten a sus preferencias

## Integrantes
- Nahuel Escobar
- Eliana Lucena
- Franco Mancilla


## Cómo ejecutar
clonar el repocitorio y ejecuta el comando necesario para su entorno

### Para Windows
```
py .\main.py

```

### Para Linux

```
python3 main.py

```

## Test
Ejecucion de test para probar las estructuras y comparar los algorimos implementados 

### test.algoritmos.medir_tiempos
Genera 1.000 películas de prueba y compara el tiempo de búsqueda secuencial en una lista con el tiempo de búsqueda en un árbol binario de búsqueda (BST); también muestra los resultados y la altura del árbol.
#### Para Windows
```
py -m test.algoritmos.medir_tiempos
```

#### Para Linux

```
python3 -m test.algoritmos.medir_tiempos
```

### test.algoritmos.probar_avl
Compara un árbol BST con un AVL usando 900 películas de prueba; muestra sus alturas y compara los tiempos de búsqueda.

#### Para Windows
```
py -m test.algoritmos.probar_avl
```

#### Para Linux

```
python3 -m test.algoritmos.probar_avl
```

### test.algoritmos.probar_bst
Prueba las operaciones del árbol BST, incluidos los recorridos, la altura y las búsquedas de elementos existentes y no existentes.

#### Para Windows
```
py -m test.algoritmos.probar_bst
```

#### Para Linux

```
python3 -m test.algoritmos.probar_bst
```

### test.algoritmos.arbol_general_test
Prueba la creación y consulta de un árbol general de categorías; muestra su altura, cantidad de nodos, recorridos, niveles, hijos y resultados de búsqueda.

#### Para Windows
```
py -m test.algoritmos.arbol_general_test
```

#### Para Linux

```
python3 -m test.algoritmos.arbol_general_test
```


## Estructura del proyecto
```text
tp-ed-cineverso-grupo16
├── .git
├── .gitignore
├── README.md
├── datos
│   └── peliculas.json
├── docs
│   ├── 00-propuesta.md
│   ├── 01-requerimientos.md
│   ├── 02-casos_de_usos.md
│   ├── 03-diagrama-clases.md
│   ├── 07-analisis.tp3.md
│   └── 08-analisis-tp4-tp5.md
├── estructuras
│   ├── arbol_binario.py
│   ├── arbol_general.py
│   └── avl.py
├── main.py
├── modelos
│   ├── clientes.py
│   └── peliculas.py
├── test
│   ├── algoritmos
│   │   ├── __pycache__
│   │   ├── medir_tiempos.py
│   │   ├── probar_avl.py
│   │   └── probar_bst.py
│   └── arbol_general_test.py
└── ui
    └── terminal.py
```

## estado 
- Tp0: Completado
- Tp1: Completado
- Tp3: Completado
- Tp4: Completado