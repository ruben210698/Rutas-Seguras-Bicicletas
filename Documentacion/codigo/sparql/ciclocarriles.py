String queryTxt =
        " PREFIX escjr: <http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/callejero/> " +
        " SELECT ?name ?longitud" +
        " WHERE { " +
        " <http://vocab.ciudadesabiertas.es/recurso/callejero/madrid/Via/" + idSearch + "> a escjr:Via;" +
        " <http://www.geonames.org/ontology#officialName> ?name ; " +
        " escjr:longitud ?longitud ; " +
        " }";

String queryTxt2 =
        " PREFIX cl-ciclo: <http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/callejero/ciclo-carril/> " +
        " SELECT ?carrilExclusBici" +
        " WHERE { " +
        " <http://vocab.ciudadesabiertas.es/recurso/callejero/madrid/ciclo-carril/" + idSearch + "> a cl-ciclo:Ciclocarril;" +
        " cl-ciclo:carrilExclusBici ?carrilExclusBici ; " +
        " }";
