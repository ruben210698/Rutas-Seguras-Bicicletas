String queryTxt =
" PREFIX escjr: <http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/callejero/> " +
" PREFIX geo: <http://www.geonames.org/ontology/> " +
" SELECT ?name ?longitud" +
" WHERE { " +
" <http://datos.madrid.es/recurso/urbanismo-infraestructuras/callejero/via/" + idSearch + "> a escjr:Via;" +
" geo:officialName ?name ; " +
" escjr:longitud ?longitud ; " +
" }";
