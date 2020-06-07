String queryTxt =
        " PREFIX accid: <http://vocab.ciudadesabiertas.es/def/transporte/accidente/> " +
        " PREFIX geo: <http://www.geonames.org/ontology> " +
        " SELECT ?nombreCalle" +
        " WHERE { " +
        " <http://datos.madrid.es/recurso/urbanismo-infraestructuras/callejero/via/" + idSearch + "> a "+
             "<http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/callejero#Via>;"+
        " <http://www.geonames.org/ontology/officialName> ?nombreCalle ; " +
        " }";

String queryTxt2 =
" PREFIX accid: <http://vocab.ciudadesabiertas.es/def/transporte/accidente/> " +
" PREFIX geo: <http://www.geonames.org/ontology> " +
" PREFIX geosparql: <http://www.opengis.net/ont/geosparql#> " +
" SELECT ?Accidente ?hour ?lesividad ?persona_afectada" +
" WHERE { " +
" ?Accidente a accid:Accidente;" +
" accid:ocurreEnVia <http://datos.madrid.es/recurso/urbanismo-infraestructuras/callejero/via/"+ idSearch +">;" +
" accid:lesividad ?lesividad ;"+
" accid:hour ?hour; "+
" accid:hasPersAfectAccid ?persona_afectada; "+
" }";

String queryTxt3 =
" PREFIX accid: <http://vocab.ciudadesabiertas.es/def/transporte/accidente/> " +
" PREFIX geosparql: <http://www.opengis.net/ont/geosparql#> " +
" SELECT ?PersonaAfectada ?tipoPersAfect " +
" WHERE { " +
" <" + uriPersAfect + "> a accid:PersonaAfectada;" +
" accid:tipoPersAfect ?tipoPersAfect ;"+
" }";
