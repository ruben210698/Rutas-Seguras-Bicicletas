package rubenTfg.RutasBiciSeguras;

import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;

import org.apache.jena.query.Query;
import org.apache.jena.query.QueryExecution;
import org.apache.jena.query.QueryExecutionFactory;
import org.apache.jena.query.QueryFactory;
import org.apache.jena.query.QuerySolution;
import org.apache.jena.query.ResultSet;
import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.ModelFactory;
import org.apache.jena.util.FileManager;

public class JenaRequest {
	
	public static boolean esCicloCarril(int idVia) {
		String fileCiclo = "/Users/ruben210698/Documents/Universidad/TFG/Rutas-Seguras-Bicicletas/ProyectoJava/RutasBiciSeguras/src/main/java/rubenTfg/RutasBiciSeguras/datasets/ciclocarriles.ttl";
        Model modelCiclo = ModelFactory.createDefaultModel();
        InputStream inCiclo = FileManager.get().open(fileCiclo);
		
        if (inCiclo == null)
        	throw new IllegalArgumentException("File: " + fileCiclo + " not found");
		
        modelCiclo.read("/Users/ruben210698/Documents/Universidad/TFG/Rutas-Seguras-Bicicletas/ProyectoJava/RutasBiciSeguras/src/main/java/rubenTfg/RutasBiciSeguras/datasets/ciclocarriles.ttl");

        String idSearch = idVia + "";
        
        String queryTxt = 
        		" PREFIX cl-ciclo: <http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/callejero/ciclo-carril/> " + 
        		" PREFIX escjr: <http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/callejero/> " +
        		" SELECT ?name ?longitud ?carrilExclusBici" +
                " WHERE { " +
                " <http://vocab.ciudadesabiertas.es/recurso/callejero/madrid/Via/" + idSearch + "> a escjr:Via;" + 
                " <http://www.geonames.org/ontology#officialName> ?name ; " +
                " escjr:longitud ?longitud ; " +
                " }";
        
        Query query = QueryFactory.create(queryTxt);
        QueryExecution qexec = QueryExecutionFactory.create(query, modelCiclo);
        ResultSet results = qexec.execSelect();
        
        boolean encontrado = false;
        while (results.hasNext()) {
            QuerySolution binding = results.nextSolution();
            String name = binding.getLiteral("name").getString();
            double longitud = Double.parseDouble(binding.getLiteral("longitud").getString());
            
            System.out.println("---- " + name);
            System.out.println("---- " + longitud);
     
            encontrado = true;
        }
        
		return encontrado;
	}
	
	
	
	
	
	
	
	
	
	public static boolean esCalleTranquila(int idVia) {
		String fileCiclo = "/Users/ruben210698/Documents/Universidad/TFG/Rutas-Seguras-Bicicletas/ProyectoJava/RutasBiciSeguras/src/main/java/rubenTfg/RutasBiciSeguras/datasets/callesTranquilas.ttl";
        Model modelCiclo = ModelFactory.createDefaultModel();
        InputStream inCiclo = FileManager.get().open(fileCiclo);
		
        if (inCiclo == null)
        	throw new IllegalArgumentException("File: " + fileCiclo + " not found");
		
        modelCiclo.read("/Users/ruben210698/Documents/Universidad/TFG/Rutas-Seguras-Bicicletas/ProyectoJava/RutasBiciSeguras/src/main/java/rubenTfg/RutasBiciSeguras/datasets/callesTranquilas.ttl");

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
        
        boolean encontrado = false;
        while (results.hasNext()) {
            QuerySolution binding = results.nextSolution();
            String name = binding.getLiteral("name").getString();
            double longitud = Double.parseDouble(binding.getLiteral("longitud").getString());
            
            System.out.println("---- " + name);
            System.out.println("---- " + longitud);
            encontrado = true;
        }
        
		return encontrado;
	}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	public static boolean haHabidoAccidente(int idVia) {
		String fileCiclo = "/Users/ruben210698/Documents/Universidad/TFG/Rutas-Seguras-Bicicletas/ProyectoJava/RutasBiciSeguras/src/main/java/rubenTfg/RutasBiciSeguras/datasets/AccidentesBicicletas.ttl";
        Model modelCiclo = ModelFactory.createDefaultModel();
        InputStream inCiclo = FileManager.get().open(fileCiclo);
		
        if (inCiclo == null)
        	throw new IllegalArgumentException("File: " + fileCiclo + " not found");
		
        modelCiclo.read("/Users/ruben210698/Documents/Universidad/TFG/Rutas-Seguras-Bicicletas/ProyectoJava/RutasBiciSeguras/src/main/java/rubenTfg/RutasBiciSeguras/datasets/AccidentesBicicletas.ttl");

        String idSearch = idVia + "";
        
        String queryTxt = 
        		" PREFIX accid: <http://vocab.ciudadesabiertas.es/def/transporte/accidente/> " +
        		" PREFIX geo: <http://www.geonames.org/ontology> " +
        		" SELECT ?Accidente ?nombreCalle" +
                " WHERE { " +
                " <http://vocab.ciudadesabiertas.es/recurso/callejero/madrid/Via/" + idSearch + "> a "+
                	 "<http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/callejero#Via>;"+
                " accid:ocurrioAccidente ?Accidente ;" +
                " <http://www.geonames.org/ontology/officialName> ?nombreCalle ; " +
                " }";
        
        
        
        Query query = QueryFactory.create(queryTxt);
        QueryExecution qexec = QueryExecutionFactory.create(query, modelCiclo);
        ResultSet results = qexec.execSelect();
        
        ArrayList<String> listUrisAccidentes = new ArrayList<String>();
        boolean encontrado = false;
        while (results.hasNext()) {
            QuerySolution binding = results.nextSolution();
            String uriAccid = binding.getResource("Accidente").getURI();
            if(!listUrisAccidentes.isEmpty() && listUrisAccidentes.contains(uriAccid) ) //Evitar duplicados de accidentes
            	continue;
        	listUrisAccidentes.add(uriAccid);
        	
            String name = binding.getLiteral("nombreCalle").getString();
            System.out.println("---- " + name);
            System.out.println("---- " + uriAccid);
            String queryTxt2 = 
            		" PREFIX accid: <http://vocab.ciudadesabiertas.es/def/transporte/accidente/> " +
            		" PREFIX geo: <http://www.geonames.org/ontology> " +
            		" PREFIX geosparql: <http://www.opengis.net/ont/geosparql#> " +
            		" SELECT ?Accidente ?hour ?lesividad ?persona_afectada" +
                    " WHERE { " +
                	" <" + uriAccid + "> a accid:Accidente;" +
                	" accid:lesividad ?lesividad ;"+
                	" accid:hour ?hour; "+
                	" accid:hasPersAfectAccid ?persona_afectada; "+
                    " }";
            Query query2 = QueryFactory.create(queryTxt2);
            QueryExecution qexec2 = QueryExecutionFactory.create(query2, modelCiclo);
            ResultSet results2 = qexec2.execSelect();
            
            
            while (results2.hasNext()) {
            
                QuerySolution binding2 = results2.nextSolution();
                String lesividad = binding2.getResource("lesividad").getURI();
                String uriPersAfect = binding2.getResource("persona_afectada").getURI();
                String hour = binding2.getLiteral("hour").getString();

                System.out.println("---- " + lesividad);
                System.out.println("---- " + uriPersAfect);
                System.out.println("---- " + hour);
                
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
                	 System.out.println("---- " + tipoPersAfect);
                }
                
            }
            encontrado = true;
        }
        
		return encontrado;
	}
	
	
	

	
	
	
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int idVia = 263300;//266300;
	//	System.out.println(esCicloCarril(idVia));
	//	System.out.println(esCalleTranquila(idVia));
		System.out.println(haHabidoAccidente(idVia));

	}

}
