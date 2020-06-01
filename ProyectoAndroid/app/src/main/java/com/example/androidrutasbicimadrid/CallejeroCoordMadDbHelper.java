package com.example.androidrutasbicimadrid;

import android.content.ContentValues;
import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;


public class CallejeroCoordMadDbHelper extends SQLiteOpenHelper {

    // /data/data/<paquete>/databases/<nombre-de-la-bd>.db

    public static final int DATABASE_VERSION = 1;
    public static final String DATABASE_NAME = "CallejeroCoordMad.db";

    public CallejeroCoordMadDbHelper(Context context) {
        super(context, DATABASE_NAME, null, DATABASE_VERSION);
    }


    @Override
    public void onCreate(SQLiteDatabase sqLiteDatabase) {
        sqLiteDatabase.execSQL(
                "CREATE TABLE callCoordMadrid (\n" +
                        "COD_VIA INT NULL,\n" +
                        "COD_POSTAL INT NULL,\n" +
                        "LATITUD DOUBLE NULL,\n" +
                        "LONGITUD DOUBLE NULL,\n" +
                        "codCuadrante INT NULL\n" +
                        ");"
        );

        // Volcado de Datos:
        insertarTodasCoordernadas(sqLiteDatabase);


    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        // No hay operaciones
    }


    private void insertarTodasCoordernadas(SQLiteDatabase sqLiteDatabase) {

        DatosCoorden.insertarTodasCoordernadas(sqLiteDatabase);

    }
}
