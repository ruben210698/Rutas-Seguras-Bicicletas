
- ### Clases

> ### Accidente
> **IRI:**
> http://vocab.ciudadesabiertas.es/def/transporte/accidente#Accidente
> Siniestro ocurrido en la vía pública con implicación de algún vehículo. El recurso se construirá a partir de su número de expediente.
> **Definida por:**
> http://vocab.ciudadesabiertas.es/def/transporte/accidente


> ### PersonaAfectada
> **IRI:**
> http://vocab.ciudadesabiertas.es/def/transporte/accidente#PersonaAfectada
> La persona perjudicada por el accidente de tráfico.
> **Definida por:**
> http://vocab.ciudadesabiertas.es/def/transporte/accidente


> ### Portal
> **IRI:** http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/callejero#Portal
> Ha sido definido por la plataforma ciudadesabiertas.
> Subacceso independiente exterior (al aire libre) a una misma construcción. Para una misma construcción, con un mismo número de vía, pueden existir varias entradas que pueden estar numeradas con números o letras. [fuente: Modelo de Direcciones de la Administración General del Estado v.2]
> **Definida por:**
> http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/callejero


> ### Municipio
> **IRI:** http://vocab.linkeddata.es/datosabiertos/def/sector-publico/territorio#Municipio
> Se ha reutilizado la definición de Municipio proporcionada por vocab.linkeddata.es
> Un Municipio es el ente local definido en el artículo 140 de la Constitución española y la entidad básica de la organización territorial del Estado según el artículo 1 de la Ley 7/1985, de 2 de abril, Reguladora de las Bases del Régimen Local. Tiene personalidad jurídica y plena capacidad para el cumplimiento de sus fines. La delimitación territorial de Municipio está recogida del Registro Central de Cartografía del IGN. Su nombre, que se especifica con la propiedad dct:title, es el proporcionado por el Registro de Entidades Locales del Ministerio de Política Territorial, en http://www.ine.es/nomen2/index.do
> **Definida por:**
> http://purl.org/derecho/vocabulario
> http://vocab.linkeddata.es/datosabiertos/def/sector-publico/territorio
> http://www.ign.es/ign/resources/acercaDe/tablon/ModeloDireccionesAGE
> **Esta en rango de:** municipio



> ### Via
> **IRI:** http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/callejero#Via
> Se ha reutilizado la definición de Municipio proporcionada por vocab.linkeddata.es
> Vía de comunicación construida para la circulación. En su definición según el modelo de direcciones de la Administración General del Estado, Incluye calles, carreteras de todo tipo, caminos, vías de agua, pantanales, etc. Asimismo, incluye la pseudovía., es decir todo aquello que complementa o sustituye a la vía. En nuestro caso, este término se utiliza para hacer referencia a las vías urbanas. Representación numérica de la misma.
> **Definida por:**
> http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/callejero



> ### Gender
> **IRI:** https://schema.org/gender
> Género de la persona afectada.
> Seguirá el formato definido por Schema.org
> Se utilizarán las siguientes definidas en la clase:
> http://schema.org/Male
> http://schema.org/Female
> http://schema.org/Mixed
> **Definida por:**
> https://schema.org/gender



- ### Propiedades de datos


> ### fecha
> **IRI:** http://vocab.ciudadesabiertas.es/def/transporte/accidente#fecha
> Fecha en la que ocurre el siniestro. Día, mes y año, sin incluir la hora del accidente.
> **Definida por:**
> http://vocab.ciudadesabiertas.es/def/transporte/accidente
> **Dominio:** Accidente
> **Rango:** xsd:date


> ### hora
> **IRI:** http://vocab.ciudadesabiertas.es/def/transporte/accidente#hora
> Hora en la que ocurre el siniestro.
> **Definida por:**
> http://vocab.ciudadesabiertas.es/def/transporte/accidente
> **Dominio:** Accidente
> **Rango:** xsd:time




> ### officialName
> **IRI:** http://www.geonames.org/ontology#officialName
> Definición reutilizada del Callejero de DatosAbiertos.
> Un nombre en el idioma oficial local.
> **Definida por:**
> http://www.geonames.org/ontology
> **Dominio:** Via
> **Rango:** xsd:string



> ### typicalAgeRange
> **IRI:** https://schema.org/typicalAgeRange
> Rango de edad en el que se encuentra la persona afectada. Seguirá el siguiente formato definido por Schema.org:
> <span property="typicalAgeRange">10-12</span>
> **Definida por:**
> https://schema.org/typicalAgeRange
> **Dominio:** PersonaAfectada
> **Rango:** xsd:string


> ### enCruce
> **IRI:** http://vocab.ciudadesabiertas.es/def/transporte/accidente#enCruce
> Si el accidente ocurrió en un cruce entre 2 o más vías.
> Está representado como un integer ya que puede ser un cruce de múltiples calles. En caso de ser un valor booleano solo podría representarse la intersección entre calles. Esta propiedad representa el numero de calles asociadas. En caso de que no fuese cruce se le asignaría el valor 0, en los casos en los que si se asignaría 2, 3 o números sucesivos dependiendo del numero de calles de la intersección.
> **Definida por:**
> http://vocab.ciudadesabiertas.es/def/transporte/accidente
> **Dominio:** Accidente
> **Rango:** xsd:integer



> ### identifier
> **IRI:** http://purl.org/dc/terms/identifier
> An unambiguous reference to the resource within a given context.
> Recommended practice is to identify the resource by means of a string conforming to an identification system. Examples include International Standard Book Number (ISBN), Digital Object Identifier (DOI), and Uniform Resource Name (URN). Persistent identifiers should be provided as HTTP URIs.
> **Definida por:**
> http://purl.org/dc/elements
> **Dominio:** Accidente
> **Rango:**
> http://www.w3.org/2000/01/rdf-schema#Literal


> ### codigoINE
> **IRI:** http://vocab.linkeddata.es/datosabiertos/def/sector-publico/territorio#codigoINE
> Indicador de si las bicicletas disponen o no de un carril propio para su circulación.
> **Definida por:**
> http://vocab.linkeddata.es/datosabiertos/def/sector-publico/territorio
> **Dominio:** Municipio
> **Rango:** xsd:integer





- ### Propiedades de objeto

> ### hasPersonaAfectada
> **IRI:** http: //vocab.ciudadesabiertas.es/def/transporte/accidente#hasPersonaAfectada
> Persona que se asocia a un accidente. Esta a su vez puede tener más características como por ejemplo el rol que tuvo (peatón, conductor), edad y género.
> **Definida por:**
> http://vocab.ciudadesabiertas.es/def/transporte/accidente
> **Dominio:** Accidente
> **Rango:** PersonaAfectada

 


> ### tipoVehiculo
> **IRI:**
> http://vocab.ciudadesabiertas.es/def/transporte/accidente#tipoVehiculo
> Tipo de vehículo afectado, p.ej. Bicicleta, Bicicleta EPAC (pedaleo asistido). Se han definido los siguientes elementos:
http://vocab.linkeddata.es/datosabiertos/kos/transporte/accidente/tipo-vehiculo/BICICLETA
http://vocab.linkeddata.es/datosabiertos/kos/transporte/accidente/tipo-vehiculo/BICICLETA-EPAC
> **Definida por:**
> http://vocab.ciudadesabiertas.es/def/transporte/accidente
> **Dominio:** Accidente
> **Rango:** concept



> ### meteorologia
> **IRI:**
> http://vocab.ciudadesabiertas.es/def/transporte/accidente#meteorologia
> Condiciones ambientales que se dan en el momento del siniestro. Se han definido varios tipos posibles: http://vocab.linkeddata.es/datosabiertos/kos/transporte/accidente/meteorologia/DESPEJADO http://vocab.linkeddata.es/datosabiertos/kos/transporte/accidente/meteorologia/LLUVIA-DEBIL http://vocab.linkeddata.es/datosabiertos/kos/transporte/accidente/meteorologia/LLUVIA-INTENSA http://vocab.linkeddata.es/datosabiertos/kos/transporte/accidente/meteorologia/NUBLADO http://vocab.linkeddata.es/datosabiertos/kos/transporte/accidente/meteorologia/GRANIZANDO http://vocab.linkeddata.es/datosabiertos/kos/transporte/accidente/meteorologia/DESCONOCIDO
> **Definida por:**
> http://vocab.ciudadesabiertas.es/def/transporte/accidente
> **Dominio:** Accidente
> **Rango:** concept




> ### tipoAccidente
> **IRI:**
> http://vocab.ciudadesabiertas.es/def/transporte/accidente#tipoAccidente
> Tipo de accidente asociado. Se han definido para ello varios tipos posibles:
> http://vocab.linkeddata.es/datosabiertos/kos/transporte/accidente/tipo-accidente/COLISION http://vocab.linkeddata.es/datosabiertos/kos/transporte/accidente/tipo-accidente/COLISION-DOBLE http://vocab.linkeddata.es/datosabiertos/kos/transporte/accidente/tipo-accidente/COLISION-MULTIPLE http://vocab.linkeddata.es/datosabiertos/kos/transporte/accidente/tipo-accidente/ALCANCE http://vocab.linkeddata.es/datosabiertos/kos/transporte/accidente/tipo-accidente/CHOQUE-NO-VEHICULO http://vocab.linkeddata.es/datosabiertos/kos/transporte/accidente/tipo-accidente/ATROPELLO-PEATON http://vocab.linkeddata.es/datosabiertos/kos/transporte/accidente/tipo-accidente/VUELCO http://vocab.linkeddata.es/datosabiertos/kos/transporte/accidente/tipo-accidente/CAIDA http://vocab.linkeddata.es/datosabiertos/kos/transporte/accidente/tipo-accidente/OTROS
> **Definida por:**
> http://vocab.ciudadesabiertas.es/def/transporte/accidente
> **Dominio:** Accidente
> **Rango:** concept


> ### lesividad
> **IRI:** http://vocab.ciudadesabiertas.es/def/transporte/accidente#lesividad Código que indica la gravedad del siniestro para la persona afectada.
> Para su uso se han definido los siguientes elementos:
> 01 Atencion en urgencias sin posterior ingreso. - LEVE:
> http: //vocab.linkeddata.es/datosabiertos/kos/transporte/accidente/lesividad/01
> 02 Ingreso inferior o igual a 24 horas - LEVE:
> http: //vocab.linkeddata.es/datosabiertos/kos/transporte/accidente/lesividad/02
> 03 Ingreso superior a 24 horas. - GRAVE:
> http: //vocab.linkeddata.es/datosabiertos/kos/transporte/accidente/lesividad/03
> 04 Fallecido 24 horas - FALLECIDO:
> http: //vocab.linkeddata.es/datosabiertos/kos/transporte/accidente/lesividad/04
> 05 Asistencia sanitaria ambulatoria con posterioridad - LEVE:
> http: //vocab.linkeddata.es/datosabiertos/kos/transporte/accidente/lesividad/05
> 06 Asistencia sanitaria inmediata en centro de salud o mutua - LEVE:
> http: //vocab.linkeddata.es/datosabiertos/kos/transporte/accidente/lesividad/06
> 07 Asistencia sanitaria solo en el lugar del accidente - LEVE:
> http: //vocab.linkeddata.es/datosabiertos/kos/transporte/accidente/lesividad/07
> 14 Sin asistencia sanitaria:
> http: //vocab.linkeddata.es/datosabiertos/kos/transporte/accidente/lesividad/14
> 77 Se desconoce:
> http: //vocab.linkeddata.es/datosabiertos/kos/transporte/accidente/lesividad/77
> **Definida por:**
> http://vocab.ciudadesabiertas.es/def/transporte/accidente
> **Dominio:** Accidente
> **Rango:** concept


> ### gender
> **IRI:** https://schema.org/gender
> Género de la persona afectada.
> Seguirá el formato definido por Schema.org
> Se utilizarán las siguientes definidas en la clase:
> http://schema.org/Male
> http://schema.org/Female
> http://schema.org/Mixed
> **Definida por:**
> https://schema.org/gender
> **Dominio:** PersonaAfectada
> **Rango:** Gender



> ### tipoPersAfect
> **IRI:**
> http://vocab.ciudadesabiertas.es/def/transporte/accidente#tipoPersAfect
> Persona a la que afecta el accidente. Puede ser Conductor, peatón, testigo o viajero. Se han definido los siguientes elementos: http://vocab.linkeddata.es/datosabiertos/kos/transporte/accidente/tipo-pers-afect/CONDUCTOR http://vocab.linkeddata.es/datosabiertos/kos/transporte/accidente/tipo-pers-afect/PEATON http://vocab.linkeddata.es/datosabiertos/kos/transporte/accidente/tipo-pers-afect/TESTIGO http://vocab.linkeddata.es/datosabiertos/kos/transporte/accidente/tipo-pers-afect/VIAJERO
> **Definida por:**
> http://vocab.ciudadesabiertas.es/def/transporte/accidente
> **Dominio:** PersonaAfectada
> **Rango:** concept

> ### portal
> **IRI:** http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/callejero#portal
> Numero de la calle donde ha ocurrido el accidente, si procede.
> **Definida por:**
> http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/callejero
> **Dominio:** Accidente
> **Rango:** Portal


> ### ocurreEnVia
> **IRI:**
> http://vocab.ciudadesabiertas.es/def/transporte/accidente#ocurreEnVia
> Propiedad que permite conocer las vías asociadas a un accidente. Puede haber varias en el caso de que haya ocurrido en un cruce.
> **Definida por:**
> http://vocab.ciudadesabiertas.es/def/transporte/accidente
> **Dominio:** Accidente
> **Rango:** Via


> ### municipio
> **IRI:** http://vocab.linkeddata.es/datosabiertos/def/sector-publico/territorio#municipio
> Municipio al que pertenece un fenómeno geográfico o una entidad administrativa.
> **Definida por:**
> http://vocab.linkeddata.es/datosabiertos/def/sector-publico/territorio
> **Dominio:** Via
> **Rango:** Municipio


> ### portal
> **IRI:** http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/callejero#portal
> Portal asociado a un accidente.
> **Definida por:**
> http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/callejero
> **Dominio:** Accidente
> **Rango:** Via

