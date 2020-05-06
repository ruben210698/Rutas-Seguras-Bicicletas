# Rutas-Seguras-Bicicletas

Poyecto cuyo fin último es la creación de una aplicación para obtener una valoración sobre la seguridad de una ruta en bicicleta. Se están tratando datos proporcionados por el ayuntamiento de Madrid, por lo tanto tendrá ese ámbito de utilización, sin embargo podrá ser aplicable a cualquier lugar que disponga de esos datos y puedan ser refinados con los vocabularios aqui definidos.
Siguiendo los principios de Web Semantica y Linked Data se definirán los vocabularios para Accidentes de Bicicletas, Ciclocarriles y Calles Tranquilas para Ciclistas. Se tratarán los datasets proporcionados por el portal datos.madrid transformandolos y adaptándolos a nuestras necesidades y se generarán datos a partir de ellos acorde con los voabularios descritos. En la aplicación final, creada en Android, se harán búsquedas a estos ficheros mediante consultas SPARQL y a partir de una ruta se mostrarán los detalles de la misma con los datos existentes.

## Distribución del repositorio
El proyecto se ha dividido en carpetas para diferenciar claramente sus componentes. Se dispondrá de un directorio para la documentación, otro para los ficheros directamente relacionados con los vocabularios (dir/ OWL), otro para el código escrito en Python (que se corresponde principalmente con el utilizado para hacer las transformaciones a los datasets) y otro para el código en Android (aplicación final y código java para consultas SPARQL a los datos).

#### Documentación
En este directorio se podrá consultar el PDF con la documentación relativa al proyecto y el código en LATEX utilizado para generarlo. Dispone de varias subcarpetas, "secciones" contiene el texto de los distintos capítulos, "include" corresponde a la carpeta proporcionada que contiene tanto imagenes como código de portada y preámbulo, "images" incluye las imagenes utilizadas para el documento y "codigo" corresponde a las secciones de programación que se han añadido al documento.

#### OWL
En este directorio se incluyen los ficheros OWL, generados por el programa Protegée, para los vocabularios aquí definidos. Compone las imágenes relativas a los vocabularios antes mencionados y un fichero xml que permite modificarlas con el programa Draw.io.


