package com.example.androidrutasbicimadrid;

import android.content.Context;
import android.content.res.AssetManager;


import java.io.IOException;
import java.io.InputStream;
import java.io.StringWriter;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;



import com.hp.hpl.jena.query.Query;
import com.hp.hpl.jena.query.QueryExecution;
import com.hp.hpl.jena.query.QueryExecutionFactory;
import com.hp.hpl.jena.query.QueryFactory;
import com.hp.hpl.jena.query.QuerySolution;
import com.hp.hpl.jena.query.ResultSet;
import com.hp.hpl.jena.rdf.model.Model;
import com.hp.hpl.jena.rdf.model.ModelFactory;

import org.apache.commons.io.IOUtils;

public class JenaRequest {
	
	public static CicloCarril getCicloCarril(int idVia, Context context) {
        AssetManager am = context.getAssets();
		String fileCiclo = "ciclocarriles.ttl";
        Model modelCiclo = ModelFactory.createDefaultModel();
        InputStream inCiclo = null;


        try {
            inCiclo = am.open(fileCiclo);
        } catch (IOException e) {
            System.out.println("+-+-+-+-+-+-+-+-+-+-+-+-+- Error ciclocarril");
            return null;
        }
        if (inCiclo == null)
        	throw new IllegalArgumentException("File: " + fileCiclo + " not found");
        modelCiclo.read(inCiclo, "", "TURTLE");
        String idSearch = idVia + "";


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

        Query query = QueryFactory.create(queryTxt);
        QueryExecution qexec = QueryExecutionFactory.create(query, modelCiclo);
        ResultSet results = qexec.execSelect();

        Query query2 = QueryFactory.create(queryTxt2);
        QueryExecution qexec2 = QueryExecutionFactory.create(query2, modelCiclo);
        ResultSet results2 = qexec2.execSelect();

        CicloCarril ciclo = null;
        if (results.hasNext()) {
            QuerySolution binding = results.nextSolution();
            String nombreCalle = binding.getLiteral("name").getString();
            double longitud = Double.parseDouble(binding.getLiteral("longitud").getString());

            ciclo = new CicloCarril();
            ciclo.setNombreCalle(nombreCalle);
            ciclo.setLongitud(longitud);
        }
        if (results2.hasNext() && ciclo != null) {
            QuerySolution binding2 = results2.nextSolution();
            boolean carrilExclusBici = binding2.getLiteral("carrilExclusBici").getBoolean();

            ciclo.setCarrilExclusBici(carrilExclusBici);
        }

		return ciclo;
	}





	public static CalleTranquila getCalleTranquila(int idVia, Context context) {
        AssetManager am = context.getAssets();

		String fileCiclo = "callesTranquilas.ttl";
        Model modelCiclo = ModelFactory.createDefaultModel();
        InputStream inCiclo = null;

        try {
            inCiclo = am.open(fileCiclo);
        } catch (IOException e) {
            System.out.println("+-+-+-+-+-+-+-+-+-+-+-+-+- Error calle tranquila");
            return null;
        }
        if (inCiclo == null)
        	throw new IllegalArgumentException("File: " + fileCiclo + " not found");
        modelCiclo.read(inCiclo, "", "TURTLE");
        String idSearch = idVia + "";

        String queryTxt =
                " PREFIX escjr: <http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/callejero/> " +
                        " PREFIX geo: <http://www.geonames.org/ontology/> " +
                        " SELECT ?name ?longitud" +
                        " WHERE { " +
                        " <http://vocab.ciudadesabiertas.es/recurso/callejero/madrid/Via/" + idSearch + "> a escjr:Via;" +
                        " geo:officialName ?name ; " +
                        " escjr:longitud ?longitud ; " +
                        " }";
        
        Query query = QueryFactory.create(queryTxt);
        QueryExecution qexec = QueryExecutionFactory.create(query, modelCiclo);
        ResultSet results = qexec.execSelect();


        CalleTranquila callTranq = null;
        if (results.hasNext()) {
            QuerySolution binding = results.nextSolution();
            String nombreCalle = binding.getLiteral("name").getString();
            double longitud = Double.parseDouble(binding.getLiteral("longitud").getString());

            callTranq = new CalleTranquila(nombreCalle, longitud);
        }
        
		return callTranq;
	}















    public static ArrayList<Accidente> getAccidentes(int idVia, Context context) {
        AssetManager am = context.getAssets();

        String fileCiclo = "AccidentesBicicletas.ttl";
        Model modelCiclo = ModelFactory.createDefaultModel();
        InputStream inCiclo = null;

        try {
            inCiclo = am.open(fileCiclo);
        } catch (IOException e) {
            System.out.println("+-+-+-+-+-+-+-+-+-+-+-+-+- Error Accidentes");
            return null;
        }
        if (inCiclo == null)
            throw new IllegalArgumentException("File: " + fileCiclo + " not found");
        modelCiclo.read(inCiclo, "", "TURTLE");
        String idSearch = idVia + "";

        String queryTxt =
                " PREFIX accid: <http://vocab.ciudadesabiertas.es/def/transporte/accidente/> " +
                        " PREFIX geo: <http://www.geonames.org/ontology> " +
                        " SELECT ?nombreCalle" +
                        " WHERE { " +
                        " <http://vocab.ciudadesabiertas.es/recurso/callejero/madrid/Via/" + idSearch + "> a "+
                        "<http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/callejero#Via>;"+
                        " <http://www.geonames.org/ontology/officialName> ?nombreCalle ; " +
                        " }";


        Query query = QueryFactory.create(queryTxt);
        QueryExecution qexec = QueryExecutionFactory.create(query, modelCiclo);
        ResultSet results = qexec.execSelect();

        ArrayList<String> listUrisAccidentes = new ArrayList<String>();
        ArrayList<Accidente> listAccidentes = new ArrayList<Accidente>();


        while (results.hasNext()) {
            QuerySolution binding = results.nextSolution();

            String nombreCalle = binding.getLiteral("nombreCalle").getString();


    //        System.out.println("---- " + nombreCalle);
            String queryTxt2 =
                    " PREFIX accid: <http://vocab.ciudadesabiertas.es/def/transporte/accidente/> " +
                            " PREFIX geo: <http://www.geonames.org/ontology> " +
                            " PREFIX geosparql: <http://www.opengis.net/ont/geosparql#> " +
                            " SELECT ?Accidente ?hour ?lesividad ?persona_afectada" +
                            " WHERE { " +
                            " ?Accidente a accid:Accidente;" +
                            " accid:ocurreEnVia <http://vocab.ciudadesabiertas.es/recurso/callejero/madrid/Via/"+ idSearch +">;" +
                            " accid:lesividad ?lesividad ;"+
                            " accid:hour ?hour; "+
                            " accid:hasPersAfectAccid ?persona_afectada; "+
                            " }";
            Query query2 = QueryFactory.create(queryTxt2);
            QueryExecution qexec2 = QueryExecutionFactory.create(query2, modelCiclo);
            ResultSet results2 = qexec2.execSelect();


            while (results2.hasNext()) {
                Accidente accidente = new Accidente();
                listAccidentes.add(accidente);
                accidente.setNombreCalle(nombreCalle);

                QuerySolution binding2 = results2.nextSolution();

                String uriAccid = binding2.getResource("Accidente").getURI();
                if(!listUrisAccidentes.isEmpty() && listUrisAccidentes.contains(uriAccid) ) //Evitar duplicados de accidentes
                    continue;
                listUrisAccidentes.add(uriAccid);


                String lesividad = binding2.getResource("lesividad").getURI();
                String uriPersAfect = binding2.getResource("persona_afectada").getURI();
                String hour = binding2.getLiteral("hour").getString();

                accidente.setUriLesividad(lesividad);
                accidente.setHora(hour);

          //      System.out.println("---- " + lesividad);
         //       System.out.println("---- " + uriPersAfect);
          //      System.out.println("---- " + hour);

                String queryTxt3 =
                        " PREFIX accid: <http://vocab.ciudadesabiertas.es/def/transporte/accidente/> " +
                                " PREFIX geosparql: <http://www.opengis.net/ont/geosparql#> " +
                                " SELECT ?PersonaAfectada ?tipoPersAfect " +
                                " WHERE { " +
                                " <" + uriPersAfect + "> a accid:PersonaAfectada;" +
                                " accid:tipoPersAfect ?tipoPersAfect ;"+
                                " }";
                Query query3 = QueryFactory.create(queryTxt3);
                QueryExecution qexec3 = QueryExecutionFactory.create(query3, modelCiclo);
                ResultSet results3 = qexec3.execSelect();
                if(results3.hasNext()) {
                    QuerySolution binding3 = results3.nextSolution();
                    String tipoPersAfect = binding3.getResource("tipoPersAfect").getURI();
                    accidente.setUriTipoPersAfect(tipoPersAfect);
         //           System.out.println("---- " + tipoPersAfect);
                }

            }
        }

        return listAccidentes;
    }







	


}
