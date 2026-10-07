from estructuras.arbol_binario import ArbolBST
from estructuras.avl import AVL
from modelos.peliculas import Pelicula

def generar_peliculas(cantidad):
    peliculas = []
    aux = 0
    for i in range(cantidad):
        aux = i
        pelicula = Pelicula(

            titulo=f"Pelicula {i}",

            director="cristofer nolan",

            anio=aux,

            genero="accion"
        )
        peliculas.append(pelicula)
    return peliculas



def comparar_bst_vs_avl(lista_datos, clave):
    """Compara un BST común con un AVL insertando los mismos datos.

    Retorna un diccionario con las alturas de ambos árboles y
    tiempos de búsqueda para demostrar la diferencia de desbalance.
    """
    import time

    # --- BST común (usa arboles.py) ---
    try:
        from estructuras.arbol_binario import ArbolBST
        from estructuras.avl import AVL
    except ImportError:
        try:
            from estructuras.arbol_binario import ArbolBST
        except ImportError:
            return {"error": "No se encontró arboles.py para comparar"}

    bst = ArbolBST()
    for d in lista_datos:
        bst.insertar(d, clave=clave)

    # --- AVL ---
    avl = AVL()
    for d in lista_datos:
        avl.insertar(d, clave=clave)

    # Medir tiempo de búsqueda en ambos
    valor_test = clave(lista_datos[-1])

    inicio = time.time()
    for _ in range(1000):
        bst.buscar(valor_test, clave=clave)
    tiempo_bst = (time.time() - inicio) * 1000

    inicio = time.time()
    for _ in range(1000):
        avl.buscar(valor_test, clave=clave)
    tiempo_avl = (time.time() - inicio) * 1000

    return {
        "altura_bst": bst.altura(),
        "altura_avl": avl.altura(),
        "tiempo_bst_ms": tiempo_bst,
        "tiempo_avl_ms": tiempo_avl,
        "mejor_balance": avl.altura() < bst.altura(),
    }


lista_peliculas = generar_peliculas(900)

resultado = comparar_bst_vs_avl(lista_peliculas, clave=lambda x: x.anio)
if "error" in resultado:
    print("  ", resultado["error"])
else:
    print(f"  Altura BST: {resultado['altura_bst']}")
    print(f"  Altura AVL: {resultado['altura_avl']}")
    print(f"  BST es más alto que AVL: {resultado['mejor_balance']}")


print(f"  Tiempo búsqueda BST (ms): {resultado['tiempo_bst_ms']:.4f}")
print(f"  Tiempo búsqueda AVL (ms): {resultado['tiempo_avl_ms']:.4f}")