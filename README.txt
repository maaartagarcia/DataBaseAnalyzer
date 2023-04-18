Problemática:
Dificultad para conocer las características de una base de datos en su totalidad, o comparar de forma tradicional (Hecha por humanos) el conjunto de imágenes de una base de datos, o la observación del tipo de manipulaciones que estas han sufrido
Puede servirnos para conocer ante qué clase de manipulaciones nos encontramos
Puede darnos una idea rápida sobre grandes cantidades de datos sin necesidad de pararnos a revisarnos
Es escalable, podemos añadir el análisis de otras características gracias a su implementación preparada para ser ampliada
En conclusión, es una herramienta que puede acelerar el proceso de búsqueda de bases de datos que nos sean de utilidad

Notas sobre la ejecución de la Herramienta:
Para probar el analizador, debemos comprender su funcionamiento:
Situarse en el directorio “ddbb_analysis/scripts”
Ejecutar en el cmd “py main.py” junto con las máscaras
El programa nos permitirá aquellas características que seleccionemos, es decir, marquemos como “1” en los argumentos
Podremos analizar
Primero: Porcentaje de Imágenes a Color en la Base de Datos
Segundo: Dimensiones Medias de las Imágenes en la Base de Datos
Tercero: Manipulaciones sufridas sobre una Imagen de la Base de Datos
Cuarto: Extracción de Imágenes a partir de un Fichero .pdf

Ejemplo de ejecución:
Como hemos comentado, ejecutando “py main.py 1 1 1 1” podremos realizar análisis sobre las 4 características posibles

