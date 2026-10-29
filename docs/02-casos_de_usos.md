# Casos de uso - Cinebot

## Casos de uso: Listar
- **Actor**: Usuario 
- **Precondición**: el catálogo está cargado. 
- **Flujo principal**:
    1. El usuario selecciona "Ver listado". 
    2. el sistema muestra todas las peliculas


## Casos de uso: Buscar por titulo
- **Actor**: Usuario
- **Precondición**: El catalogo debe estar cargado en arbol AVL
- **Flujo principal**:
    1. El usuario selecciona "Buscar película por titulo"
    2. El sistema pide el titulo
    3. El usuario ingresa el titulo a elegir
    4. El sistema lo busca sin (distinguir enter mayusculas)
- **Flujo alternativo**: si no lo encuentra el sistema informa que la pelicula no se encontro

## Casos de uso: Buscar pelicula por Categoria
- **Actor**: Usuario
- **Precondición**: 
    1. Las categorías deben estar declaradas en arbol general (AG)
    2. Cada pelicula este asociada a una categorías
- **Flujo principal**:
    1. El usuario elije la opcion de buscar por categorías
    2. El sistema muestra las categorías disponibles
    3. El usuario selecciona una categoria
    4. El sistema busca y muestra las peliculas asociadas
- **Flujo alternativo**: En caso de elegir una categoria inexistente el sistema informa que no existe 

-  **Aclaraciones**: si peliculas tiene subcategorias tembien apareceran en ellas

    


