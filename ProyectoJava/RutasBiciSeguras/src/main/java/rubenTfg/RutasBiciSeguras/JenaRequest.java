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
                " escjr:" + idSearch + " a <http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/callejero#Via>,\n" + 
                "    cl-ciclo:Ciclocarril; " +
                " <http://www.geonames.org/ontology#officialName> ?name ; " +
           //     " escjr:longitud ?longitud ; " +
                " }";
        
        Query query = QueryFactory.create(queryTxt);
        QueryExecution qexec = QueryExecutionFactory.create(query, modelCiclo);
        ResultSet results = qexec.execSelect();
        
        boolean encontrado = false;
        while (results.hasNext()) {
            QuerySolution binding = results.nextSolution();
            String name = binding.getLiteral("name").getString();
            
            System.out.println("---- " + name);
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
        		" PREFIX cl-ciclo: <http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/callejero/ciclo-carril/> " + 
        		" PREFIX escjr: <http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/callejero/> " +
        		" PREFIX cl-tranquila: <http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/callejero/calle-tranquila/>" +
        		" PREFIX btn100: <https://datos.ign.es/def/btn100/>" +
        		" PREFIX geo: <http://www.geonames.org/ontology/>" +
        		
        		" SELECT ?name ?longitud ?calzada" +
                " WHERE { " +
                " escjr:" + idSearch + " a <http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/callejero#Via>;" +
                " geo:officialName ?name ; " +
                " btn100:calzada ?calzada" +
           //     " escjr:longitud ?longitud ; " +
                " }";
        
        Query query = QueryFactory.create(queryTxt);
        QueryExecution qexec = QueryExecutionFactory.create(query, modelCiclo);
        ResultSet results = qexec.execSelect();
        
        boolean encontrado = false;
        while (results.hasNext()) {
            QuerySolution binding = results.nextSolution();
            String name = binding.getLiteral("name").getString();
            
            System.out.println("---- " + name);
            encontrado = true;
        }
        
		return encontrado;
	}
	
	
	
	
	
	
	

	
	
	
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int idVia = 266300;
		System.out.println(esCicloCarril(idVia));
		System.out.println(esCalleTranquila(idVia));

	}

}
