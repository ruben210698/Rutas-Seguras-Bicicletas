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
	
	public static boolean esCicloCarril(int idVia, Context context) {
        AssetManager am = context.getAssets();

		String fileCiclo = "ciclocarriles.ttl";

        Model modelCiclo = ModelFactory.createDefaultModel();
        InputStream inCiclo = null;

        try {
            inCiclo = am.open(fileCiclo);
        } catch (IOException e) {
            System.out.println("+-+-+-+-+-+-+-+-+-+-+-+-+- Error ciclocarril");
            return false;
        }

        if (inCiclo == null)
        	throw new IllegalArgumentException("File: " + fileCiclo + " not found");


   //     System.out.println("+-+-+-+-+-+-+-+-+-+-+-+-+- 1");

        modelCiclo.read(inCiclo, "", "TURTLE");

   //     System.out.println("+-+-+-+-+-+-+-+-+-+-+-+-+- 2");
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
            
            System.out.println("\n\n------CicloCarril------ " + name);
            encontrado = true;
        }
        
		return encontrado;
	}
	
	public static boolean esCalleTranquila(int idVia, Context context) {
        AssetManager am = context.getAssets();

		String fileCiclo = "callesTranquilas.ttl";
        Model modelCiclo = ModelFactory.createDefaultModel();
        InputStream inCiclo = null;
        try {
            inCiclo = am.open(fileCiclo);
        } catch (IOException e) {
            System.out.println("+-+-+-+-+-+-+-+-+-+-+-+-+- Error calle tranquila");
            return false;
        }

        if (inCiclo == null)
        	throw new IllegalArgumentException("File: " + fileCiclo + " not found");

   //     System.out.println("+-+-+-+-+-+-+-+-+-+-+-+-+- 1");

        modelCiclo.read(inCiclo, "", "TURTLE");

       // System.out.println("+-+-+-+-+-+-+-+-+-+-+-+-+- 2");

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
            
            System.out.println("\n\n-----Call-Tranqu----- " + name);
            encontrado = true;
        }
        
		return encontrado;
	}
	
	
	
	
	public static void ejecucionPrueba(Context context){

        int idVia = 560600;//266300;
        System.out.println("\n\n+-+-+-+-+-Ciclo +-+-+-+-+-+-+-+-" + esCicloCarril(idVia, context));
        System.out.println("\n\n+-+-+-+-+-Cll-tranq +-+-+-+-+-+-+-+-" + esCalleTranquila(idVia, context));


    }
	
	

	
	
	
	/*

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int idVia = 266300;
		System.out.println(esCicloCarril(idVia));
		System.out.println(esCalleTranquila(idVia));

	}
*/
}
