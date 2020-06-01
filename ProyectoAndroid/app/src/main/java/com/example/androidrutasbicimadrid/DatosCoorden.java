package com.example.androidrutasbicimadrid;

import android.content.ContentValues;
import android.database.sqlite.SQLiteDatabase;

import com.example.androidrutasbicimadrid.sqlData.*;

public class DatosCoorden {

    public static void insertarTodasCoordernadas(SQLiteDatabase sqLiteDatabase) {

        ContentValues values = null;
        int[][] matrizIds = {ArrayDatosCoordIds1.arrIds1, ArrayDatosCoordIds2.arrIds2, ArrayDatosCoordIds3.arrIds3, ArrayDatosCoordIds4.arrIds4, ArrayDatosCoordIds5.arrIds5, ArrayDatosCoordIds6.arrIds6, ArrayDatosCoordIds7.arrIds7, ArrayDatosCoordIds8.arrIds8, ArrayDatosCoordIds9.arrIds9, ArrayDatosCoordIds10.arrIds10, ArrayDatosCoordIds11.arrIds11, ArrayDatosCoordIds12.arrIds12, ArrayDatosCoordIds13.arrIds13, ArrayDatosCoordIds14.arrIds14, ArrayDatosCoordIds15.arrIds15, ArrayDatosCoordIds16.arrIds16, ArrayDatosCoordIds17.arrIds17, ArrayDatosCoordIds18.arrIds18, ArrayDatosCoordIds19.arrIds19, ArrayDatosCoordIds20.arrIds20, ArrayDatosCoordIds21.arrIds21, ArrayDatosCoordIds22.arrIds22, ArrayDatosCoordIds23.arrIds23, ArrayDatosCoordIds24.arrIds24, ArrayDatosCoordIds25.arrIds25, ArrayDatosCoordIds26.arrIds26};
        double[][] matrizLat = {ArrayDatosCoordLat1.arrLat1, ArrayDatosCoordLat2.arrLat2, ArrayDatosCoordLat3.arrLat3, ArrayDatosCoordLat4.arrLat4, ArrayDatosCoordLat5.arrLat5, ArrayDatosCoordLat6.arrLat6, ArrayDatosCoordLat7.arrLat7, ArrayDatosCoordLat8.arrLat8, ArrayDatosCoordLat9.arrLat9, ArrayDatosCoordLat10.arrLat10, ArrayDatosCoordLat11.arrLat11, ArrayDatosCoordLat12.arrLat12, ArrayDatosCoordLat13.arrLat13, ArrayDatosCoordLat14.arrLat14, ArrayDatosCoordLat15.arrLat15, ArrayDatosCoordLat16.arrLat16, ArrayDatosCoordLat17.arrLat17, ArrayDatosCoordLat18.arrLat18, ArrayDatosCoordLat19.arrLat19, ArrayDatosCoordLat20.arrLat20, ArrayDatosCoordLat21.arrLat21, ArrayDatosCoordLat22.arrLat22, ArrayDatosCoordLat23.arrLat23, ArrayDatosCoordLat24.arrLat24, ArrayDatosCoordLat25.arrLat25, ArrayDatosCoordLat26.arrLat26};
        double[][] matrizLon = {ArrayDatosCoordLon1.arrLon1, ArrayDatosCoordLon2.arrLon2, ArrayDatosCoordLon3.arrLon3, ArrayDatosCoordLon4.arrLon4, ArrayDatosCoordLon5.arrLon5, ArrayDatosCoordLon6.arrLon6, ArrayDatosCoordLon7.arrLon7, ArrayDatosCoordLon8.arrLon8, ArrayDatosCoordLon9.arrLon9, ArrayDatosCoordLon10.arrLon10, ArrayDatosCoordLon11.arrLon11, ArrayDatosCoordLon12.arrLon12, ArrayDatosCoordLon13.arrLon13, ArrayDatosCoordLon14.arrLon14, ArrayDatosCoordLon15.arrLon15, ArrayDatosCoordLon16.arrLon16, ArrayDatosCoordLon17.arrLon17, ArrayDatosCoordLon18.arrLon18, ArrayDatosCoordLon19.arrLon19, ArrayDatosCoordLon20.arrLon20, ArrayDatosCoordLon21.arrLon21, ArrayDatosCoordLon22.arrLon22, ArrayDatosCoordLon23.arrLon23, ArrayDatosCoordLon24.arrLon24, ArrayDatosCoordLon25.arrLon25, ArrayDatosCoordLon26.arrLon26};

        long startTime = System.currentTimeMillis();
        for(int j = 0; j<matrizIds.length; j++) {
            for (int i = 0; i < matrizIds[j].length; i++) {
                values = new ContentValues();
                values.put("COD_VIA", matrizIds[j][i]);
                values.put("COD_POSTAL", 0);
                values.put("LATITUD", matrizLat[j][i]);
                values.put("LONGITUD", matrizLon[j][i]);
                //   values.put("LATITUD", ArrayDatosCoordLat.arrLat[i]);
                //   values.put("LONGITUD", ArrayDatosCoordLon.arrLon[i]);
                values.put("codCuadrante", 0);
                sqLiteDatabase.insert("callCoordMadrid", null, values);
            }
            System.out.println("---- Arrays Numero... " + j);
        }
        System.out.println("---- Tiempo consulta BBDD: " + (System.currentTimeMillis()-startTime));


    }

}
