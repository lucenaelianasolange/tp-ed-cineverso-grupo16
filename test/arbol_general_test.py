from estructuras.arbol_general import ArbolGeneral 

arbol = ArbolGeneral()
arbol.insertar_raiz("Películas")

ciencia = arbol.agregar_hijo(arbol.raiz, "Ciencia Ficción")
accion = arbol.agregar_hijo(arbol.raiz, "Acción")
comedia = arbol.agregar_hijo(arbol.raiz, "Comedia")

arbol.agregar_hijo(ciencia, "Cyberpunk")
arbol.agregar_hijo(ciencia, "Viajes temporales")
arbol.agregar_hijo(ciencia, "Inteligencia artificial")

arbol.agregar_hijo(accion, "Superhéroes")
arbol.agregar_hijo(accion, "Guerra")

arbol.agregar_hijo(comedia, "Comedia romántica")
arbol.agregar_hijo(comedia, "Comedia negra")

print("=== Árbol General de Categorías ===")
print("Raíz:", arbol.raiz.dato)
print("Altura:", arbol.altura())
print("Cantidad de nodos:", arbol.cantidad_nodos())
print()

print("--- Recorrido en amplitud ---")
print(arbol.amplitud())
print()

print("--- Recorrido en profundidad (preorder) ---")
print(arbol.profundidad_preorder())
print()

print("--- Recorrido en profundidad (postorder) ---")
print(arbol.profundidad_postorder())
print()

print("--- Niveles ---")
for i, nivel in enumerate(arbol.obtener_niveles()):
    print(f"  Nivel {i}: {nivel}")
print()

print("--- Hijos de 'Ciencia Ficción' ---")
nodo_ciencia = arbol.buscar("Ciencia Ficción")
if nodo_ciencia:
    print(arbol.listar_hijos(nodo_ciencia))

print()
print("--- Buscar 'Cyberpunk' ---")
resultado = arbol.buscar("Cyberpunk")
print("Encontrado:", resultado)
