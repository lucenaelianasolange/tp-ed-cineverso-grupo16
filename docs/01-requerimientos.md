# Requerimientos - Cineverso

## Alcance

Cineverso es una aplicación de consola que permite explorar un catálogo de películas para facilitar su búsqueda y elección

## Requerimientos funcionales (RF)

| ID | Requerimiento | Estado |
|---|---|---|
| RF-01 | El sistema debe cargar el catálogo de películas desde el archivo de datos del proyecto. | Implementado |
| RF-02 | El sistema debe mostrar todas las películas del catálogo, incluyendo su información disponible. | Implementado |
| RF-03 | El sistema debe permitir buscar una película por su título y mostrarla si existe. La búsqueda no debe distinguir entre mayúsculas y minúsculas. | Implementado |
| RF-04 | El sistema debe permitir explorar las películas agrupadas por categoría y mostrar las películas correspondientes a la categoría seleccionada. | Implementado |
| RF-05 | El sistema debe permitir filtrar películas por género. | Implementado |
| RF-06 | El sistema debe ofrecer recomendaciones de películas basadas en las preferencias o selecciones del usuario. | Pendiente |
| RF-07 | El sistema debe permitir consultar el historial de películas vistas | Pendiente |
| RF-08 | El sistema debe permitir borrar el historial del usuario. | Pendiente |
| RF-09 | El sistema debe permitir salir de la aplicación desde el menú principal. | Implementado |

## Requerimientos no funcionales (RNF)

| ID | Requerimiento |
|---|---|
| RNF-01 | La aplicación debe ejecutarse en una terminal y presentar las opciones mediante un menú de texto. |
| RNF-02 | El catálogo debe almacenarse en un archivo JSON legible por el programa. |
| RNF-03 | Las búsquedas y consultas deben informar claramente si se encontraron resultados o si la opción ingresada no es válida. |
| RNF-04 | La aplicación debe poder iniciarse desde el punto de entrada `main.py` en los entornos Windows y Linux|



## Decisiones 
$1.a$ se decidio utilizar un arbol general como estructura principal para mostrar el catalogo de pelicula, ya que permite reprecentar relaciones jerarquicas entre generos y subgeneros

## Observaciones 
$1.a$ La estructura elegida favorece la exploracion de categoria relacionada y evitar tener que mantener multiples estructuras de clasificación independites para cada criterio de busqueda.
$1.b$ Los filtros de director y año qudaron fuera del alcace de esta vercion, debido a su incorporacion precentaba replantear o complejisar el esquema de la jerarquia elegida.

