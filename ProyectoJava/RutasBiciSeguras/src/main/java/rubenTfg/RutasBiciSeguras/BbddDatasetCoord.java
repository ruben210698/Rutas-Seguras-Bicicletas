package rubenTfg.RutasBiciSeguras;

import javafx.util.Pair; 

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Properties;
import java.util.TimeZone;

public class BbddDatasetCoord {
	//OJOOO: añadir al pom.xml las lines de mysql
	final static String url = "jdbc:mysql://localhost:3306/"; //Nuestra cadena de conexcion
	final static String dbName = "coordenadasMadrid";
	final static String driver = "com.mysql.cj.jdbc.Driver";
	final static String userName = "root";
	final static String password = "password"; //"ruben210698password";
	
	final static double MARGENV1 = 0.00015;
	final static double MARGENV2 = 0.0003;
	final static double MARGENV3 = 0.0006;
	final static double MARGENV4 = 0.001;
	final static double MARGENV5 = 0.0015;
	// Cuando haya varias calles posibles, el margen que se le puede dar con respecto a la más proxima
	final static double MARGEN_ENTRE_CALLES_FINAL = 0.0003; // 30m
	
	final static double[] ARRLATITUD = 
			{ 40.31, 40.32, 40.33, 40.34, 40.35, 40.36, 40.37, 40.38, 40.39, 40.4, 
			40.41, 40.42, 40.43, 40.44, 40.45, 40.46, 40.47, 40.48, 40.49, 40.5, 
			40.51, 40.52, 40.53, 40.54, 40.55, 40.56, 40.57, 40.58, 40.6, 40.61 };
	
	final static double[] ARRLONGITUD = 
			{ -3.84, -3.83, -3.82, -3.81, -3.8, -3.79, -3.78, -3.77, -3.76, -3.75,
			-3.74, -3.73, -3.72, -3.71, -3.7, -3.69, -3.68, -3.67, -3.66, -3.65, 
			-3.64, -3.63, -3.62, -3.61, -3.6, -3.59, -3.58, -3.57, -3.56, -3.55, 
			-3.54, -3.53, -3.52 };
	
	
	public static ArrayList<Integer> getPosArray(double[] arr, double num){
		ArrayList<Integer> arrPosFinales = new ArrayList<Integer>();
		ArrayList<Double> arrNums = new ArrayList<Double>();
		//System.out.println(num+0.001);
		double num2Dec = (double)(Math.round(num*100d) / 100d);
		
		//Posiciones cercanas:
		double numNew = 0;
		if ((numNew = (double)(Math.round((num+0.001)*100d) / 100d)) != num2Dec)
			arrNums.add((double)(Math.round((num+0.001)*100d) / 100d));
		if ((numNew = (double)(Math.round((num-0.001)*100d) / 100d)) != num2Dec)
			arrNums.add((double)(Math.round((num-0.001)*100d) / 100d));
		if (arrNums.isEmpty()) {
			// Si solo esta el numero inicial:
			for(int pos = 0; pos < arr.length; pos++) {
				if(num2Dec == arr[pos]) {
					arrPosFinales.add(pos);
					break;
				}
			}
		} else {
			arrNums.add(numNew);
			for(int i = 0; i<arrNums.size(); i++) {
				for(int pos = 0; pos < arr.length; pos++) {
					if(arrNums.get(i) == arr[pos]) {
						arrPosFinales.add(pos);
						break;
					}
				}
			}
			
		}
		return arrPosFinales;
	}
	
	
	public static ArrayList<Integer> getCuadrantes(double latitud, double longitud) {
		ArrayList<Integer> arrCuadrantes = new ArrayList<Integer>();
		
		// Misma fórmula que en el proceso de Python para el detaset de coordenadas
		ArrayList<Integer> arrLat = getPosArray(ARRLATITUD, latitud);
		ArrayList<Integer> arrLon = getPosArray(ARRLONGITUD, longitud);
		
		for(int i = 0; i<arrLat.size(); i++) {
			int cuadrante = 0;
			for(int j = 0; j<arrLon.size(); j++) {
				cuadrante = arrLat.get(i)*100;
				cuadrante = cuadrante+arrLon.get(j);
				if(!arrCuadrantes.contains(cuadrante)) {
					// Si esta en las ultimas o primeras posiciones se añadirian duplicados
					arrCuadrantes.add(cuadrante);
					//System.out.println("-- "+cuadrante);
				}
			}
		}
		return arrCuadrantes;
	}
	

	public static Connection startBBDD() throws ClassNotFoundException {
		Connection conn = null;
		
		try {
			Class.forName(driver);//.newInstance();
		//	System.out.println("OK Driver");
			
			conn = DriverManager.getConnection(url + dbName + 
					"?useSSL=false&autoReconnect=false&serverTimezone="+ TimeZone.getDefault().getID()
					, userName, password);
		//	System.out.println("OK Connection");
			if(conn.isClosed())
			//	System.out.println("Database connection working using TCP/IP...");	
				System.out.println("Error al conectar la BBDD");
			
		} catch(Exception e) {
			System.err.println("Exception: " + e.getMessage());
			
		}
		return conn;
		
	}	
	
	/*
	 La funcion getListaCallesPosibles(double latitud, double longitud)  lo que hace es buscar la latitud y longitud
	 con cierto margen de error. Para ello va por fases, cada fase permite un poco más de margen, obligando a
	 que encuentre la calle con el menor posible.
	 En caso de encontrar varios, calcula la diferencia total (De las 2 ejes con las coordenadas originales) y elige
	 el menor o varios más próximos
	 
	 
	 */
	
	public static ArrayList<Integer> getListaCallesPosibles(double latitud, double longitud) throws ClassNotFoundException {
		ArrayList<Integer> listaCalles = new ArrayList<Integer>();
		ArrayList<Double> listaDifs = new ArrayList<Double>();
		ArrayList<Integer> listaCallesDist = new ArrayList<Integer>();
		ArrayList<Double> listaDifsDist = new ArrayList<Double>();
		
		
		Connection con = null;
		try {
			
			con = startBBDD();
			double margenError = 0;
			
			long startTime = System.currentTimeMillis();
			for(int nVuelta = 1; nVuelta<=5; nVuelta++) {
				switch(nVuelta) {
					case 1: margenError = MARGENV1; break;
					case 2: margenError = MARGENV2; break;
					case 3: margenError = MARGENV3; break;
					case 4: margenError = MARGENV4; break;
					case 5: margenError = MARGENV5; break;
					default: margenError = MARGENV1; break;
				}
				// Primero se intentará con un margen de error mínimo. 
				// En la segunda vuelta se probatá con algo más y en la tercera más
				/* Vamos a aceptar una diferencia entre coordenadas de 15 metros.
				 * Si 15 metros son 0.00014 en coordenadas aproximadamente, se le aceptará 0.00007 por arriba y abajo.
				 */
				
				String consulta = "SELECT COD_VIA, LATITUD, LONGITUD "
								+ " FROM callCoordMadrid WHERE "
								+ " LATITUD < ? AND LATITUD > ? AND"
								+ " LONGITUD < ? AND LONGITUD > ?" ;
				
				
				PreparedStatement sentencia= con.prepareStatement(consulta);
				sentencia.setDouble(1, latitud + margenError);
				sentencia.setDouble(2, latitud - margenError);
				sentencia.setDouble(3, longitud + margenError);
				sentencia.setDouble(4, longitud - margenError);
				ResultSet rs = sentencia.executeQuery();
				
	
				while(rs.next())
				{
					double latDB = rs.getFloat("LATITUD");
					double lonDB = rs.getFloat("LONGITUD");
					double dif = Math.abs(latitud - latDB) + Math.abs(longitud - lonDB);
					listaDifs.add(dif);
					listaCalles.add(rs.getInt("COD_VIA"));
					
				}
				if(!listaCalles.isEmpty()) {
					// Sacar las diferentes calles(con ids) y la diferencia menor con las coordenadas introducidas.
					for(int i = 0; i<listaCalles.size(); i++) {
						
						if(!listaCallesDist.contains(listaCalles.get(i))) {
							//Si no existe se añade
							listaCallesDist.add(listaCalles.get(i));
							listaDifsDist.add(listaDifs.get(i));
						} else {
							// Si existe se comprueba que la diferencia sea la menor posible
							if(listaDifsDist.get(listaCallesDist.indexOf(listaCalles.get(i))) > listaDifs.get(i)) {
								listaDifsDist.set(listaCallesDist.indexOf(listaCalles.get(i)), listaDifs.get(i));
							}
							
						}
					}
					break;
				}
			}
			System.out.println("---- Tiempo consulta BBDD: " + (System.currentTimeMillis()-startTime));
			
			
		} catch (SQLException sqle) { 
			System.out.println("--Error en la ejecución: " + sqle.getErrorCode() + " " + sqle.getMessage()); }
		try { if(con != null) { con.close(); } } catch(SQLException e) { }
		
		double numMenor = 1;
		int posMenor = -1;
		// Calculamos la menor diferencia de todas:
		for(int i = 0; i<listaCallesDist.size(); i++) {
			if(numMenor > listaDifsDist.get(i)) {
				numMenor = listaDifsDist.get(i);
				posMenor = i;
			}
		}
		
		ArrayList<Integer> listaCallesDistFinal = new ArrayList<Integer>();
		if(posMenor > -1)
			listaCallesDistFinal.add(listaCallesDist.get(posMenor));
		
		// Si alguna diferencia inferior a 30 metros con respecto a la menor diferencia, se considera también
		for(int i = 0; i<listaCallesDist.size(); i++) {
			if((numMenor+MARGEN_ENTRE_CALLES_FINAL) >= listaDifsDist.get(i) && i!=posMenor 
					&& !listaCallesDistFinal.contains(listaCallesDist.get(i))) {
				listaCallesDistFinal.add(listaCallesDist.get(i));
			}
		}
		return listaCallesDistFinal;
	}
	

	
	
	
	public static void queryPersonalizada() throws ClassNotFoundException {
		/*
		CREATE TABLE callCoorMadrid (
		COD_VIA INT NULL,
		LATITUD DOUBLE NULL,
		LONGITUD DOUBLE NULL,
		codCuadrante INT NULL
		);
	 */
	Connection con = null;

	try {
		con = startBBDD();
		Statement statement = con.createStatement();
		ResultSet rs = statement.executeQuery("select codCuadrante, count(*) as cuenta from callCoorMadrid group by 1 order by cuenta");
		while(rs.next())
		{
			System.out.println("Result = " + rs.getString("codCuadrante") + " --> " + rs.getString("cuenta") );
		}
		
	} catch (SQLException sqle) { 
		System.out.println("--Error en la ejecución: " + sqle.getErrorCode() + " " + sqle.getMessage());    
	}

	try {
		if(con != null)
			con.close();
	} catch(SQLException e) {

	}


	}
	
	
	
	
	

	public static void main( String[] args ) throws ClassNotFoundException, SQLException
	{
		long startTime = System.currentTimeMillis();
		
		//queryPersonalizada();
		double latitud = 40.40551;
	//	double latitud = 40.454093;
		double longitud = -3.67371;
		

		
		ArrayList<Integer> arr = getListaCallesPosibles(latitud, longitud);  //1012
		
		for(int i = 0; i<arr.size(); i++) {
			System.out.println("Select nombreOriginal from callejeroNombres Where COD_VIA = " + arr.get(i) + ";");
			
		}

		System.out.println("----Time: " + (System.currentTimeMillis()-startTime));
	}

	
	
	/*
	  	QUERIES UTILIZADAS:
	 
	 // Para sacar los distintos cuadrantes que hay para una coordenada
	 String consulta = "select DISTINCT codCuadrante from callCoorMadrid where "
							+ "LATITUD < ?+0.00015 and LATITUD > ?-0.00015 "
							+ "and LONGITUD < ?+0.00015 AND LONGITUD > ?-0.00015";
	String consulta = "select COD_VIA, LATITUD, LONGITUD from callCoorMadrid where "
								+ " LATITUD < ? and LATITUD > ?"
								+ " and LONGITUD < ? AND LONGITUD > ?";
	 
	 
	 
	 
	 
	 
	 
	 */

}














/*

	// Código copiado de:
	// https://stackoverflow.com/questions/343865/how-to-convert-from-utm-to-latlng-in-python-or-javascript/344083#344083
	// http://www.juntadeandalucia.es/economiainnovacioncienciayempleo/pam/ConvED50.action
	// La zona, obtenida de la web de la junta de Andalucia, es 30.
	// System.out.println(getLongLat(30, 437960.11, 4472790.13, true));
	public static Pair <Double,Double>  getLongLat(int zone, double easting, double northing, boolean northernHemisphere) {
	    if(! northernHemisphere)
	        northing = 10000000 - northing;
	    double latitude;
	    double longitude;

	    int a = 6378137;
	    double e = 0.081819191;
	    double e1sq = 0.006739497;
	    double k0 = 0.9996;

	    double arc = northing / k0;
	    double mu = arc / (a * (1 - Math.pow(e, 2) / 4.0 - 3 * Math.pow(e, 4) / 64.0 - 5 * Math.pow(e, 6) / 256.0));

	    double ei = (1 - Math.pow((1 - e * e), (1 / 2.0))) / (1 + Math.pow((1 - e * e), (1 / 2.0)));

	    double ca = 3 * ei / 2 - 27 * Math.pow(ei, 3) / 32.0;

	    double cb = 21 * Math.pow(ei, 2) / 16 - 55 * Math.pow(ei, 4) / 32;
	    double cc = 151 * Math.pow(ei, 3) / 96;
	    double cd = 1097 * Math.pow(ei, 4) / 512;
	    double phi1 = mu + ca * Math.sin(2 * mu) + cb * Math.sin(4 * mu) + cc * Math.sin(6 * mu) + cd * Math.sin(8 * mu);

	    double n0 = a / Math.pow((1 - Math.pow((e * Math.sin(phi1)), 2)), (1 / 2.0));

	    double r0 = a * (1 - e * e) / Math.pow((1 - Math.pow((e * Math.sin(phi1)), 2)), (3 / 2.0));
	    double fact1 = n0 * Math.tan(phi1) / r0;

	    double _a1 = 500000 - easting;
	    double dd0 = _a1 / (n0 * k0);
	    double fact2 = dd0 * dd0 / 2;

	    double t0 = Math.pow(Math.tan(phi1), 2);
	    double Q0 = e1sq * Math.pow(Math.cos(phi1), 2);
	    double fact3 = (5 + 3 * t0 + 10 * Q0 - 4 * Q0 * Q0 - 9 * e1sq) * Math.pow(dd0, 4) / 24;

	    double fact4 = (61 + 90 * t0 + 298 * Q0 + 45 * t0 * t0 - 252 * e1sq - 3 * Q0 * Q0) * Math.pow(dd0, 6) / 720;

	    double lof1 = _a1 / (n0 * k0);
	    double lof2 = (1 + 2 * t0 + Q0) * Math.pow(dd0, 3) / 6.0;
	    double lof3 = (5 - 2 * Q0 + 28 * t0 - 3 * Math.pow(Q0, 2) + 8 * e1sq + 24 * Math.pow(t0, 2)) * Math.pow(dd0, 5) / 120;
	    double _a2 = (lof1 - lof2 + lof3) / Math.cos(phi1);
	    double _a3 = _a2 * 180 / Math.PI;

	    latitude = 180 * (phi1 - fact1 * (fact2 + fact3 + fact4)) / Math.PI;

	    if (!northernHemisphere){
	        latitude = -latitude;
	    }
	    
	//    longitude = ((zone > 0) and (6 * zone - 183.0) or 3.0) - _a3
	    longitude = (3.0 + _a3) *-1;

	    return new Pair<Double,Double>(latitude, longitude);
	}
	
	


*/
