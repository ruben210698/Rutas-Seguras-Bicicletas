package com.example.androidrutasbicimadrid;

import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;

import java.util.ArrayList;


public class PeticionesBBDD {
	//OJOOO: añadir al pom.xml las lines de mysql
	public static final String DATABASE_NAME = "callCoordMadrid";


    final static double MARGENV1 = 0.00015;
	final static double MARGENV2 = 0.0003;
	final static double MARGENV3 = 0.0006;
	final static double MARGENV4 = 0.001;
	final static double MARGENV5 = 0.0015;
	// Cuando haya varias calles posibles, el margen que se le puede dar con respecto a la más proxima
	final static double MARGEN_ENTRE_CALLES_FINAL = 0.0003; // 30m


	/*
	 La funcion getListaCallesPosibles(double latitud, double longitud)  lo que hace es buscar la latitud y longitud
	 con cierto margen de error. Para ello va por fases, cada fase permite un poco más de margen, obligando a
	 que encuentre la calle con el menor posible.
	 En caso de encontrar varios, calcula la diferencia total (De las 2 ejes con las coordenadas originales) y elige
	 el menor o varios más próximos


	 */

	public static ArrayList<Integer> getListaCallesPosibles(double latitud, double longitud, Context contexto) throws ClassNotFoundException {
        ArrayList<Integer> listaCalles = new ArrayList<Integer>();
        ArrayList<Double> listaDifs = new ArrayList<Double>();
        ArrayList<Integer> listaCallesDist = new ArrayList<Integer>();
        ArrayList<Double> listaDifsDist = new ArrayList<Double>();

        CallejeroCoordMadDbHelper dbHelper = new CallejeroCoordMadDbHelper(contexto);
        SQLiteDatabase db = dbHelper.getWritableDatabase();


        if (db == null) {
            return null;
        }

        try {

            double margenError = 0;


            long startTime = System.currentTimeMillis();
            for (int nVuelta = 1; nVuelta <= 5; nVuelta++) {
                switch (nVuelta) {
                    case 1:
                        margenError = MARGENV1;
                        break;
                    case 2:
                        margenError = MARGENV2;
                        break;
                    case 3:
                        margenError = MARGENV3;
                        break;
                    case 4:
                        margenError = MARGENV4;
                        break;
                    case 5:
                        margenError = MARGENV5;
                        break;
                    default:
                        margenError = MARGENV1;
                        break;
                }
                // Primero se intentará con un margen de error mínimo.
                // En la segunda vuelta se probatá con algo más y en la tercera más
                /* Vamos a aceptar una diferencia entre coordenadas de 15 metros.
                 * Si 15 metros son 0.00014 en coordenadas aproximadamente, se le aceptará 0.00007 por arriba y abajo.
                 */
                double a1 = latitud + margenError;
                double a2 = latitud - margenError;
                double a3 = longitud + margenError;
                double a4 = longitud - margenError;
         //       System.out.println("+++1+++" + a1 + " "+ a2 + " "+ a3 + " "+ a4 + " ");

                String query = "SELECT COD_VIA, LATITUD, LONGITUD "
                        //			+ " FROM ( SELECT COD_VIA, LATITUD, LONGITUD "
                        + " FROM callCoordMadrid WHERE "
                        //					+ " codCuadrante IN ("+ cuadrantesSQL + "))A WHERE"
                        //	+ " codCuadrante IN (" + cuadrantesSQL + ") AND "
                        + " LATITUD < "+a1+" AND LATITUD > "+a2+" AND"
                        + " LONGITUD < "+a3+" AND LONGITUD > "+a4;


           //     Cursor c = db.rawQuery(query, new String[] {"COD_VIA", "LATITUD", "LONGITUD"});

                Cursor c = db.rawQuery(query, null);

                while(c.moveToNext()){
                    int idVia = c.getInt(c.getColumnIndex("COD_VIA"));
                    double latDB = c.getDouble(c.getColumnIndex("LATITUD"));
                    double lonDB = c.getDouble(c.getColumnIndex("LONGITUD"));
                    double dif = Math.abs(latitud - latDB) + Math.abs(longitud - lonDB);

                    listaDifs.add(dif);
                    listaCalles.add(idVia);

                    // Acciones...
                }
                if (!listaCalles.isEmpty()) {
                    // Sacar las diferentes calles(con ids) y la diferencia menor con las coordenadas introducidas.
                    for (int i = 0; i < listaCalles.size(); i++) {

                        if (!listaCallesDist.contains(listaCalles.get(i))) {
                            //Si no existe se añade
                            listaCallesDist.add(listaCalles.get(i));
                            listaDifsDist.add(listaDifs.get(i));
                        } else {
                            // Si existe se comprueba que la diferencia sea la menor posible
                            if (listaDifsDist.get(listaCallesDist.indexOf(listaCalles.get(i))) > listaDifs.get(i)) {
                                listaDifsDist.set(listaCallesDist.indexOf(listaCalles.get(i)), listaDifs.get(i));
                            }

                        }
                    }
                    break;
                }
            }
            System.out.println("---- Tiempo consulta BBDD: " + (System.currentTimeMillis() - startTime));


        } catch (Exception sqle) {
            System.err.println("--Error en la ejecución: " + sqle.getMessage());
        }

        double numMenor = 1;
        int posMenor = -1;
        // Calculamos la menor diferencia de todas:
        for (int i = 0; i < listaCallesDist.size(); i++) {
            if (numMenor > listaDifsDist.get(i)) {
                numMenor = listaDifsDist.get(i);
                posMenor = i;
            }
        }

        ArrayList<Integer> listaCallesDistFinal = new ArrayList<Integer>();
        if (posMenor > -1)
            listaCallesDistFinal.add(listaCallesDist.get(posMenor));

        // Si alguna diferencia inferior a 30 metros con respecto a la menor diferencia, se considera también
        for (int i = 0; i < listaCallesDist.size(); i++) {
            if ((numMenor + MARGEN_ENTRE_CALLES_FINAL) >= listaDifsDist.get(i) && i != posMenor
                    && !listaCallesDistFinal.contains(listaCallesDist.get(i))) {
                listaCallesDistFinal.add(listaCallesDist.get(i));
            }
        }
        return listaCallesDistFinal;
    }






	/*


		double latitud = 40.40551;
	//	double latitud = 40.454093;
		double longitud = -3.67371;



*/
}












