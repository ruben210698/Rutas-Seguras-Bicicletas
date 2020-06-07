
- ### Clases


> ### Ciclocarril
> **IRI:** http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/ciclo-carril#CicloCarril
> Vía con uno o más carriles destinados al tránsito de ciclistas. No necesariamente exclusivos para el tránsito de bicicletas, pero si con señalización y limitaciones adaptadas para ello.
> **Definida por:**
> http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/ciclo-carril
> **Pertenece A:** Via

 


> ### Via
>  **IRI:** http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/callejero#Via
> Se ha reutilizado la definición de Municipio proporcionada por vocab.linkeddata.es.
> Vía de comunicación construida para la circulación. En su definición según el modelo de direcciones de la Administración General del Estado, Incluye calles, carreteras de todo tipo, caminos, vías de agua, pantanales, etc. Asimismo, incluye la pseudovía., es decir todo aquello que complementa o sustituye a la vía. En nuestro caso, este término se utiliza para hacer referencia a las vías urbanas. Representación numérica de la misma.
>  **Definida por:**
>  http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/callejero



> ### Municipio
> **IRI:** http://vocab.linkeddata.es/datosabiertos/def/sector-publico/territorio#Municipio
> Se ha reutilizado la definición de Municipio proporcionada por vocab.linkeddata.es.
> Un Municipio es el ente local definido en el artículo 140 de la Constitución española y la entidad básica de la organización territorial del Estado según el artículo 1 de la Ley 7/1985, de 2 de abril, Reguladora de las Bases del Régimen Local. Tiene personalidad jurídica y plena capacidad para el cumplimiento de sus fines. La delimitación territorial de Municipio está recogida del Registro Central de Cartografía del IGN. Su nombre, que se especifica con la propiedad dct:title, es el proporcionado por el Registro de Entidades Locales del Ministerio de Política Territorial, en http://www.ine.es/nomen2/index.do
> **Definida por:**
> http://purl.org/derecho/vocabulario http://vocab.linkeddata.es/datosabiertos/def/sector-publico/territorio
> http://www.ign.es/ign/resources/acercaDe/tablon/ModeloDireccionesAGE
> **Esta en rango de:**
> municipio








- ### Propiedades de datos




> ### longitud
> **IRI:** http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/callejero#longitud
> Longitud de la calle descrita. Esta propiedad está referida a la vía que contiene un ciclocarril (calle completa).
> **Definida por:**
> http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/callejero
> **Dominio:** Via
> **Rango:** xsd:double



> ### distMaxExclusBici
> **IRI:** http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/ciclo-carril#distMaxExclusBici
> Longitud del carril exclusivo de bicicletas dentro de la calle. En caso de que no haya ciclocarril, el valor será 0.
> **Definida por:**
> http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/ciclo-carril
> **Dominio:** CicloCarril
> **Rango:** xsd:double


> ### officialName
> **IRI:** http://www.geonames.org/ontology#officialName
> Definido en el callejero de DatosAbiertos. Un nombre en el idioma oficial local.
> **Definida por:**
> http://www.geonames.org/ontology
> **Dominio:** Via
> **Rango:** xsd:string



> ### carrilExclusBici
> **IRI:** http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/ciclo-carril#carril-exclus-bici
> Indicador de si las bicicletas disponen o no de un carril propio para su circulación.
> **Definida por:**
> http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/ciclo-carril
> **Dominio:** CicloCarril
> **Rango:** xsd:boolean



> ### codigoINE
> **IRI:** http://vocab.linkeddata.es/datosabiertos/def/sector-publico/territorio#codigoINE
> Indicador de si las bicicletas disponen o no de un carril propio para su circulación.
> **Definida por:**
> http://vocab.linkeddata.es/datosabiertos/def/sector-publico/territorio
> **Dominio:** Municipio
> **Rango:** xsd:integer








- ### Propiedades de objeto

> ### municipio
> **IRI:** http://vocab.linkeddata.es/datosabiertos/def/sector-publico/territorio#municipio
> Municipio al que pertenece un fenómeno geográfico o una entidad administrativa.
> **Definida por:**
> http://vocab.linkeddata.es/datosabiertos/def/sector-publico/territorio
> **Dominio:** CicloCarril
> **Rango:** Municipio



> ### tipoUso
> **IRI:** http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/callejero#tipoUso
> Identificador del tipo de uso que puede tener la calle. Se han definido 2 clases para ello:
> - http://vocab.ciudadesabiertas.es/kos/urbanismo-infraestructuras/calle/ tipo-uso/CICLOCALLE
> - http://vocab.ciudadesabiertas.es/kos/urbanismo-infraestructuras/calle/ tipo-uso/PEATONAL

> **Definida por:**
> http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/callejero
> **Dominio:** Via
> **Rango:** concept

