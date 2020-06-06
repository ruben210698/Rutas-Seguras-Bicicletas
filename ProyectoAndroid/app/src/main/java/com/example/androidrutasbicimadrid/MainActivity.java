package com.example.androidrutasbicimadrid;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.content.ContextCompat;

import android.content.Context;
import android.content.Intent;
import android.graphics.Color;
import android.os.Build;
import android.os.Bundle;
import android.os.StrictMode;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.AutoCompleteTextView;
import android.widget.Button;
import android.widget.TextView;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URL;
import java.net.URLConnection;
import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.Iterator;

import static com.example.androidrutasbicimadrid.JenaRequest.*;
import static com.example.androidrutasbicimadrid.PeticionesBBDD.getListaCallesPosibles;





public class MainActivity extends AppCompatActivity {
    public static final String DATABASE_NAME = "callCoordMadrid";
    private final static double VAR_CICLO = 3;
    private final static double VAR_CALLTRANQ = 2;
    private final static double VAR_ACCIDENTE = 5;

    private int distanciaRuta = 0;

    private String incidenciasCiclos = "";
    private String incidenciasCallTranq = "";
    private String incidencasAccidentes = "";

    private static String KEYGOOGLE = "AIzaSyDD-Kad1SKH6eboGHDKDZvr9MDFowKDL4M";
    private String[] callesArr = {"Calle Finisterre", "Calle Gimzo de limia", "Peñagrande"};

    Context thisActivity = this;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        if(Build.VERSION.SDK_INT>9){
            StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
            StrictMode.setThreadPolicy(policy);
        }

        incidenciasCiclos = "- - - - - CicloCarriles en ruta - - - - -\n";
        incidenciasCallTranq = "- - - - - Calles Tranquilas en ruta - - - - -\n";
        incidencasAccidentes = "- - - - - Accidentes en 2019 (Max 2 ptos por calle) - - - - -\n";


        final AutoCompleteTextView actv_origen = (AutoCompleteTextView) findViewById(R.id.actv_origen);
        final AutoCompleteTextView actv_destino = (AutoCompleteTextView) findViewById(R.id.actv_destino);
        final TextView tv_tiempoAprox = (TextView) findViewById(R.id.tv_tiempoAprox);

        Button btnBuscar = (Button) findViewById(R.id.btnBuscar);


        //    String[] callesArr = getResources().getStringArray(R.array.nombresCalles);
    /*    ArrayAdapter<String> adapterCalles = new ArrayAdapter<String>(this,
                android.R.layout.simple_list_item_1, callesArr);
        actv_origen.setAdapter(adapterCalles);
        actv_destino.setAdapter(adapterCalles);
*/

















        btnBuscar.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
     //           Toast.makeText(getApplicationContext(), "Realizando busqueda...", Toast.LENGTH_LONG).show();


                String txtOrigen = actv_origen.getText().toString() + "";
                String txtDestino = actv_destino.getText().toString() + "";
                ArrayList<Coordinate> arrCoordRuta = getArrayCoordenadas(txtOrigen, txtDestino);
                ArrayList<Integer> arrIdsViasRuta = getArrIdsViasBBDD(arrCoordRuta);

                double notaFinal = getNotaRuta(arrIdsViasRuta);
                String notaFinalTxt = String.format("%.2f", Float.parseFloat(notaFinal+""));
                String incidenciasTotal = incidencasAccidentes + "\n---------------------------------------------------\n"+
                        incidenciasCiclos + "\n---------------------------------------------------\n"+
                        incidenciasCallTranq;
//--------------------------------------------------Accion final boton -----------------

                Intent intent = new Intent(MainActivity.this, Main2Activity.class);
                intent.putExtra("NOTARUTA", notaFinalTxt);
                intent.putExtra("INCIDENCIAS", incidenciasTotal);

                startActivity(intent);


            }

        });



    }















    private double getNotaRuta(ArrayList<Integer> arrIdsViasRuta ) {
        if(arrIdsViasRuta == null){
            return 0;
        }
        int nCalles = arrIdsViasRuta.size();
        double notaFinal = 8;
        Iterator<Integer> it = arrIdsViasRuta.iterator();


        while (it.hasNext()) {
            int id = it.next();
            CicloCarril cicloCarril;
            if ((cicloCarril = getCicloCarril(id, getApplicationContext())) != null){
                notaFinal += VAR_CICLO / nCalles;
                incidenciasCiclos += cicloCarril.getNombreCalle() + " + " + String.format("%.2f", Float.parseFloat((VAR_CICLO / nCalles) +"")) + " puntos \n";
             //   System.out.println("+-+-+-+-+-+-+-+-+-+-+-+-+- notaFinal " + notaFinal);
            }

            CalleTranquila callTranq;
            if ((callTranq = getCalleTranquila(id, getApplicationContext())) != null) {
                notaFinal += VAR_CALLTRANQ / nCalles;
                incidenciasCallTranq += callTranq.getNombreCalle() + " + " + String.format("%.2f", Float.parseFloat((VAR_CALLTRANQ / nCalles) +"")) + " puntos \n";
            //    System.out.println("+-+-+-+-+-+-+-+-+-+-+-+-+- notaFinal " + notaFinal);
            }

            ArrayList<Accidente> listAccidentes = getAccidentes(id, getApplicationContext());
            if(!listAccidentes.isEmpty()){
                double disminucionCalle = 0;
                int nLeves = 0;
                int nGrave = 0;
                int nFallec = 0;
                String calle = listAccidentes.get(0).getNombreCalle();
                for(Accidente accidente : listAccidentes){
                    Pair<Double, String> pairAccid = getGravedadAccidente(accidente);
                    double disminucion = pairAccid.getElement0()*VAR_ACCIDENTE/nCalles;
                    disminucionCalle += disminucion;
                    if(pairAccid.getElement1() == "Leve"){
                        nLeves +=1;
                    } else if(pairAccid.getElement1() == "Grave"){
                        nGrave +=1;
                    } else if(pairAccid.getElement1() == "Fallecido"){
                        nFallec +=1;
                    }
                //    incidencasAccidentes += accidente.getNombreCalle() + " -- "  + pairAccid.getElement1() + ": - " + String.format("%.2f", Float.parseFloat(disminucion +"")) + " puntos \n";
                }
                if(disminucionCalle>2){ // No mas de 1 punto por calle
                    disminucionCalle = 2;
                }
                incidencasAccidentes += calle + "\n\t" + nFallec + " Fallecimientos; " + nGrave + " Graves; " + nLeves + " Leves" +
                        ": - " + String.format("%.2f", Float.parseFloat(disminucionCalle +"")) + " puntos \n";
                notaFinal -= disminucionCalle;
            //    System.out.println("+-+-+-+-+-+-+-+-+-+-+-+-+- AccidenteS: " + listAccidentes.get(0).getNombreCalle());
            }

        }
        return notaFinal;
    }



    private static Pair<Double, String> getGravedadAccidente(Accidente accidente){
        double gravedad = 0;
        String lesividad = "";
        switch(accidente.getUriLesividad()) {
            case "http://vocab.linkeddata.es/datosabiertos/kos/transporte/accidente/lesividad/01": //Leve
                gravedad = 1;
                lesividad="Leve";
                break;
            case "http://vocab.linkeddata.es/datosabiertos/kos/transporte/accidente/lesividad/02": //Leve
                gravedad = 1;
                lesividad="Leve";
                break;
            case "http://vocab.linkeddata.es/datosabiertos/kos/transporte/accidente/lesividad/03": //Grave
                gravedad = 5;
                lesividad="Grave";
                break;
            case "http://vocab.linkeddata.es/datosabiertos/kos/transporte/accidente/lesividad/04": //Fallecido
                gravedad = 10;
                lesividad="Fallecido";
                break;
            default: //Leve
                gravedad = 1;
                lesividad="Leve";
                break;
        }

        // En este caso se tiene en cuenta la lesividad anterior con respecto a la importancia que le da el conductor
        // de la bicicleta que usa la aplicacion
        switch(accidente.getUriTipoPersAfect()){
            case "http://vocab.linkeddata.es/datosabiertos/kos/transporte/accidente/tipo-pers-afect/Conductor":
                gravedad = gravedad*3;
                break;
            case "http://vocab.linkeddata.es/datosabiertos/kos/transporte/accidente/tipo-pers-afect/Peatón":
                gravedad = gravedad*2;
                break;
            case "http://vocab.linkeddata.es/datosabiertos/kos/transporte/accidente/tipo-pers-afect/Viajero":
                gravedad = gravedad*2;
                break;
            case "http://vocab.linkeddata.es/datosabiertos/kos/transporte/accidente/tipo-pers-afect/Testigo":
                gravedad = gravedad*1;
                break;
            default:
                gravedad = gravedad*1;
                break;
        }

        return new Pair<Double, String>(gravedad/5, lesividad);
    }


    public static String getURLText(String url) throws Exception{
        URL website = new URL(url);
        URLConnection connection = website.openConnection();
        BufferedReader in = new BufferedReader(
                new InputStreamReader(
                        connection.getInputStream()));
        StringBuilder response = new StringBuilder();
        String inputLine;

        while ((inputLine = in.readLine()) != null)
            response.append(inputLine);
        in.close();

        return response.toString();
    }



















    private ArrayList<Coordinate> getArrayCoordenadas(String txtOrigen, String txtDestino){
        ArrayList<Coordinate> arrCoordRuta = null;

         /*
        https://maps.googleapis.com/maps/api/directions/json?origin=calle+finisterre+8+,madrid&destination=calle+gimzo+de+limia+5+,madrid&key=AIzaSyDD-Kad1SKH6eboGHDKDZvr9MDFowKDL4M
        */
        String url = "https://maps.googleapis.com/maps/api/directions/json?origin=";
        url = url + txtOrigen.replace(" ", "+").replace("++", "+") + ",madrid"; //Por si hay 2 + juntos
        url = url + "&destination=";
        url = url + txtDestino.replace(" ", "+").replace("++", "+") + ",madrid";
        url = url + "&avoid=highway&mode=bicycling";
        url = url + "&key=" + KEYGOOGLE;
       //        System.out.println("----- " + url);

        //       url = "http://www.yournavigation.org/api/1.0/gosmore.php?flat=40.476894&flon=-3.701368&tlat=40.478664&tlon=-3.707398&format=geojson";
        String jsonFile = "";
        try {
                  StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
                  StrictMode.setThreadPolicy(policy);

                  jsonFile = getURLText(url);
            //         System.out.println(jsonFile);
        } catch (Exception e) {
            System.out.println("-------ERROR en el url al obtener el JSON------");
            e.printStackTrace();
        }

 /*       jsonFile =
                "{\n" +
                        "   \"geocoded_waypoints\" : [\n" +
                        "      {\n" +
                        "         \"geocoder_status\" : \"OK\",\n" +
                        "         \"place_id\" : \"ChIJZRVtlOEnQg0RP3REbYoaqCA\",\n" +
                        "         \"types\" : [ \"establishment\", \"point_of_interest\", \"transit_station\" ]\n" +
                        "      },\n" +
                        "      {\n" +
                        "         \"geocoder_status\" : \"OK\",\n" +
                        "         \"place_id\" : \"ChIJQ8bWojIuQg0RiAqTbTNutko\",\n" +
                        "         \"types\" : [ \"street_address\" ]\n" +
                        "      }\n" +
                        "   ],\n" +
                        "   \"routes\" : [\n" +
                        "      {\n" +
                        "         \"bounds\" : {\n" +
                        "            \"northeast\" : {\n" +
                        "               \"lat\" : 40.46054780000001,\n" +
                        "               \"lng\" : -3.5897912\n" +
                        "            },\n" +
                        "            \"southwest\" : {\n" +
                        "               \"lat\" : 40.3884228,\n" +
                        "               \"lng\" : -3.73031\n" +
                        "            }\n" +
                        "         },\n" +
                        "         \"copyrights\" : \"Map data ©2020 Inst. Geogr. Nacional\",\n" +
                        "         \"legs\" : [\n" +
                        "            {\n" +
                        "               \"distance\" : {\n" +
                        "                  \"text\" : \"19,9 km\",\n" +
                        "                  \"value\" : 19920\n" +
                        "               },\n" +
                        "               \"duration\" : {\n" +
                        "                  \"text\" : \"24 min\",\n" +
                        "                  \"value\" : 1446\n" +
                        "               },\n" +
                        "               \"end_address\" : \"Calle de Antonio Sancha, 3, 28042 Madrid, España\",\n" +
                        "               \"end_location\" : {\n" +
                        "                  \"lat\" : 40.4581053,\n" +
                        "                  \"lng\" : -3.5923929\n" +
                        "               },\n" +
                        "               \"start_address\" : \"Caramuel - Antillón, 28011 Madrid, España\",\n" +
                        "               \"start_location\" : {\n" +
                        "                  \"lat\" : 40.4104614,\n" +
                        "                  \"lng\" : -3.7271994\n" +
                        "               },\n" +
                        "               \"steps\" : [\n" +
                        "                  {\n" +
                        "                     \"distance\" : {\n" +
                        "                        \"text\" : \"1,0 km\",\n" +
                        "                        \"value\" : 1004\n" +
                        "                     },\n" +
                        "                     \"duration\" : {\n" +
                        "                        \"text\" : \"3 min\",\n" +
                        "                        \"value\" : 167\n" +
                        "                     },\n" +
                        "                     \"end_location\" : {\n" +
                        "                        \"lat\" : 40.40228889999999,\n" +
                        "                        \"lng\" : -3.729968399999999\n" +
                        "                     },\n" +
                        "                     \"html_instructions\" : \"Dirígete hacia el \\u003cb\\u003esuroeste\\u003c/b\\u003e en \\u003cb\\u003eCalle de Caramuel\\u003c/b\\u003e hacia \\u003cb\\u003eCalle de Antillón\\u003c/b\\u003e/\\u003cwbr/\\u003e\\u003cb\\u003eCalle Pozoblanco\\u003c/b\\u003e\",\n" +
                        "                     \"polyline\" : {\n" +
                        "                        \"points\" : \"ktsuF~}vUb@h@`@d@n@v@p@x@VX`@f@jAtATX^^VTh@b@`@TPJ@?^PRHVLd@RvAj@h@RNAFA`@GTETETCfB]b@GxBa@NCNC\\\\IXELCLCTAFA`@CT?R@J?L@P@rAVD@`@Jb@Hf@L`@HH@DADADC\"\n" +
                        "                     },\n" +
                        "                     \"start_location\" : {\n" +
                        "                        \"lat\" : 40.4104614,\n" +
                        "                        \"lng\" : -3.7271994\n" +
                        "                     },\n" +
                        "                     \"travel_mode\" : \"DRIVING\"\n" +
                        "                  },\n" +
                        "                  {\n" +
                        "                     \"distance\" : {\n" +
                        "                        \"text\" : \"0,6 km\",\n" +
                        "                        \"value\" : 610\n" +
                        "                     },\n" +
                        "                     \"duration\" : {\n" +
                        "                        \"text\" : \"1 min\",\n" +
                        "                        \"value\" : 72\n" +
                        "                     },\n" +
                        "                     \"end_location\" : {\n" +
                        "                        \"lat\" : 40.4055138,\n" +
                        "                        \"lng\" : -3.7246539\n" +
                        "                     },\n" +
                        "                     \"html_instructions\" : \"Gira a la \\u003cb\\u003eizquierda\\u003c/b\\u003e hacia \\u003cb\\u003eCalle Vía Carpetana\\u003c/b\\u003e\",\n" +
                        "                     \"maneuver\" : \"turn-left\",\n" +
                        "                     \"polyline\" : {\n" +
                        "                        \"points\" : \"iaruFhowUPUW]KSEKACEK?AGOEMCKCGKMGQEMIOCIEKEGCEEECEMOQSOQQQCEEEEECCIGCCECECGEGECCKGGGEECECCEECEEI?AGKKSAEGKIOYo@IQIQGIGIEIGGEGEEGGECCCEEEAGEECAAECECECECCCCCCCCEEECEEIGIIOKOS[IOIMGKCECECEAEACCGAECGAEAEAIAEAG?IAK?IAO?O?G@EBm@\"\n" +
                        "                     },\n" +
                        "                     \"start_location\" : {\n" +
                        "                        \"lat\" : 40.40228889999999,\n" +
                        "                        \"lng\" : -3.729968399999999\n" +
                        "                     },\n" +
                        "                     \"travel_mode\" : \"DRIVING\"\n" +
                        "                  },\n" +
                        "                  {\n" +
                        "                     \"distance\" : {\n" +
                        "                        \"text\" : \"0,1 km\",\n" +
                        "                        \"value\" : 109\n" +
                        "                     },\n" +
                        "                     \"duration\" : {\n" +
                        "                        \"text\" : \"1 min\",\n" +
                        "                        \"value\" : 22\n" +
                        "                     },\n" +
                        "                     \"end_location\" : {\n" +
                        "                        \"lat\" : 40.4045432,\n" +
                        "                        \"lng\" : -3.7248175\n" +
                        "                     },\n" +
                        "                     \"html_instructions\" : \"Gira a la \\u003cb\\u003ederecha\\u003c/b\\u003e hacia \\u003cb\\u003ePaseo de la Ermita del Santo\\u003c/b\\u003e\",\n" +
                        "                     \"maneuver\" : \"turn-right\",\n" +
                        "                     \"polyline\" : {\n" +
                        "                        \"points\" : \"muruF`nvULDLBNBJ@RBh@BV?L?FBD@D@B@L?\"\n" +
                        "                     },\n" +
                        "                     \"start_location\" : {\n" +
                        "                        \"lat\" : 40.4055138,\n" +
                        "                        \"lng\" : -3.7246539\n" +
                        "                     },\n" +
                        "                     \"travel_mode\" : \"DRIVING\"\n" +
                        "                  },\n" +
                        "                  {\n" +
                        "                     \"distance\" : {\n" +
                        "                        \"text\" : \"67 m\",\n" +
                        "                        \"value\" : 67\n" +
                        "                     },\n" +
                        "                     \"duration\" : {\n" +
                        "                        \"text\" : \"1 min\",\n" +
                        "                        \"value\" : 13\n" +
                        "                     },\n" +
                        "                     \"end_location\" : {\n" +
                        "                        \"lat\" : 40.40456289999999,\n" +
                        "                        \"lng\" : -3.7240238\n" +
                        "                     },\n" +
                        "                     \"html_instructions\" : \"Gira a la \\u003cb\\u003eizquierda\\u003c/b\\u003e hacia \\u003cb\\u003eCalle San Ambrosio\\u003c/b\\u003e\",\n" +
                        "                     \"maneuver\" : \"turn-left\",\n" +
                        "                     \"polyline\" : {\n" +
                        "                        \"points\" : \"koruFbovUAQ?M?s@AkA\"\n" +
                        "                     },\n" +
                        "                     \"start_location\" : {\n" +
                        "                        \"lat\" : 40.4045432,\n" +
                        "                        \"lng\" : -3.7248175\n" +
                        "                     },\n" +
                        "                     \"travel_mode\" : \"DRIVING\"\n" +
                        "                  },\n" +
                        "                  {\n" +
                        "                     \"distance\" : {\n" +
                        "                        \"text\" : \"0,2 km\",\n" +
                        "                        \"value\" : 223\n" +
                        "                     },\n" +
                        "                     \"duration\" : {\n" +
                        "                        \"text\" : \"1 min\",\n" +
                        "                        \"value\" : 29\n" +
                        "                     },\n" +
                        "                     \"end_location\" : {\n" +
                        "                        \"lat\" : 40.4030846,\n" +
                        "                        \"lng\" : -3.7229573\n" +
                        "                     },\n" +
                        "                     \"html_instructions\" : \"Incórporate a \\u003cb\\u003eCalle 30\\u003c/b\\u003e\",\n" +
                        "                     \"maneuver\" : \"ramp-right\",\n" +
                        "                     \"polyline\" : {\n" +
                        "                        \"points\" : \"ooruFbjvUBe@?E?G?U@G?G@GBE@EBC@ABABABA@?@?@AZAB?B?F?F@JBB@NFJBD@F@J?L?HAJEHEHEHIJKJOJOHMBC@CPM\"\n" +
                        "                     },\n" +
                        "                     \"start_location\" : {\n" +
                        "                        \"lat\" : 40.40456289999999,\n" +
                        "                        \"lng\" : -3.7240238\n" +
                        "                     },\n" +
                        "                     \"travel_mode\" : \"DRIVING\"\n" +
                        "                  },\n" +
                        "                  {\n" +
                        "                     \"distance\" : {\n" +
                        "                        \"text\" : \"0,7 km\",\n" +
                        "                        \"value\" : 731\n" +
                        "                     },\n" +
                        "                     \"duration\" : {\n" +
                        "                        \"text\" : \"1 min\",\n" +
                        "                        \"value\" : 43\n" +
                        "                     },\n" +
                        "                     \"end_location\" : {\n" +
                        "                        \"lat\" : 40.3996429,\n" +
                        "                        \"lng\" : -3.7171695\n" +
                        "                     },\n" +
                        "                     \"html_instructions\" : \"Incorpórate a \\u003cb\\u003eM-30\\u003c/b\\u003e\",\n" +
                        "                     \"maneuver\" : \"merge\",\n" +
                        "                     \"polyline\" : {\n" +
                        "                        \"points\" : \"gfruFncvUPERC`B[FAvAW`@I\\\\KB?TIJE`@ODAXOHCTOLKNMNO^]HKRUDITYBGTa@?ATe@JWDOPg@?ANi@DSFWBM@IFw@@Y@OBe@@iAE}ACkBE}@Aw@?w@\"\n" +
                        "                     },\n" +
                        "                     \"start_location\" : {\n" +
                        "                        \"lat\" : 40.4030846,\n" +
                        "                        \"lng\" : -3.7229573\n" +
                        "                     },\n" +
                        "                     \"travel_mode\" : \"DRIVING\"\n" +
                        "                  },\n" +
                        "                  {\n" +
                        "                     \"distance\" : {\n" +
                        "                        \"text\" : \"8,3 km\",\n" +
                        "                        \"value\" : 8279\n" +
                        "                     },\n" +
                        "                     \"duration\" : {\n" +
                        "                        \"text\" : \"7 min\",\n" +
                        "                        \"value\" : 444\n" +
                        "                     },\n" +
                        "                     \"end_location\" : {\n" +
                        "                        \"lat\" : 40.4272353,\n" +
                        "                        \"lng\" : -3.6601371\n" +
                        "                     },\n" +
                        "                     \"html_instructions\" : \"Mantente a la \\u003cb\\u003eizquierda\\u003c/b\\u003e en la bifurcación para permanecer en \\u003cb\\u003eM-30\\u003c/b\\u003e\",\n" +
                        "                     \"maneuver\" : \"fork-left\",\n" +
                        "                     \"polyline\" : {\n" +
                        "                        \"points\" : \"wpquFh_uUMcA?O@}@@KBc@Dm@@ADk@Fg@@EFm@BKF_@Jk@F_@Tu@JYDMJUb@o@V_@@AX_@X_@Xa@DGTWnA}APU^m@Va@Vc@Va@DIf@_A@CPa@Vk@Nc@b@qAVy@VcANi@Je@@EJk@Lk@Jk@Jk@Jk@Jm@F[P{@Jk@?EJe@DUP_ANm@Fc@Lw@@KDWDSH_@Hg@b@eBNi@`@_BJ[@CJc@@EXwAJm@Jk@Hk@Jm@VwAFe@He@Hm@Hk@Jm@Hk@T{ABOF[Jk@DUFURu@J]b@qADK`@aARg@N_@BGl@gATc@Tc@?AbBgCp@cAVa@Va@@?Vc@Ta@Ta@@AVc@NUBGp@yA^}@Vo@JYFMPg@Z}@FSPi@HUDSPi@Ni@`@aBBO?A@GDOb@sB@INo@LkAFm@Fm@N{AFm@?GRiBBgA@o@?G?E@Y?C?AD}AD}A?O?_@Cm@AuAAIAm@Ao@Cm@Ag@Eu@AOC]Gm@Eo@e@kFMu@Gc@Ia@Km@I]Oa@s@{BMa@AEOe@AEa@qAAC?Ae@{AKYAEGUGMSe@KUYq@AA}@wBQa@CCQg@mA_DO_@CGUe@}@sBSe@Wm@O_@i@mAGQaAwBIOUc@Ue@Uc@Wc@Ya@Wa@k@}@MSIMYa@Wa@CEKMOOMI]W}AeAa@]_@]_Ay@MKGE{@o@AAOGAA{@g@AACAME[OCCu@a@m@]OKKIKGSMyBuACCg@a@MK]Wg@a@CCSOCAWQ}AcA_@UIEUMuAs@KEa@QcA_@SKMESIEAQGKCa@Oa@MoBo@{@UOEe@K_@McA[cA[gBk@iBs@{@]GAe@SOIa@QKE}@_@e@S_@Qs@[QI_@MaAc@QIWKOIOGUW_A_@kAe@uBq@uBs@aBk@YKaBu@uDgBiAi@_@QqBgAeDiBKG_@S{@e@oAq@UO_@QeAk@_@UeAi@yC_Be@U_Ac@SIw@[}@[i@Oc@Mq@Mm@IsAMSCSAOAK?S?K?w@@g@BWBW@aAH{BTWB}BRG??@I?G@M@kE^iE^uBTq@JyB\\\\q@JyAVYF_AN_@Fw@JkBV\"\n" +
                        "                     },\n" +
                        "                     \"start_location\" : {\n" +
                        "                        \"lat\" : 40.3996429,\n" +
                        "                        \"lng\" : -3.7171695\n" +
                        "                     },\n" +
                        "                     \"travel_mode\" : \"DRIVING\"\n" +
                        "                  },\n" +
                        "                  {\n" +
                        "                     \"distance\" : {\n" +
                        "                        \"text\" : \"43 m\",\n" +
                        "                        \"value\" : 43\n" +
                        "                     },\n" +
                        "                     \"duration\" : {\n" +
                        "                        \"text\" : \"1 min\",\n" +
                        "                        \"value\" : 2\n" +
                        "                     },\n" +
                        "                     \"end_location\" : {\n" +
                        "                        \"lat\" : 40.4276049,\n" +
                        "                        \"lng\" : -3.660044\n" +
                        "                     },\n" +
                        "                     \"html_instructions\" : \"Toma la salida hacia \\u003cb\\u003eA-2\\u003c/b\\u003e/\\u003cwbr/\\u003e\\u003cb\\u003eZaragoza\\u003c/b\\u003e/\\u003cwbr/\\u003e\\u003cb\\u003eAeropuerto\\u003c/b\\u003e/\\u003cwbr/\\u003e\\u003cb\\u003eAvda. de Ramón y Cajal\\u003c/b\\u003e/\\u003cwbr/\\u003e\\u003cb\\u003eC/\\u003cwbr/\\u003e S. de Madariaga\\u003c/b\\u003e\",\n" +
                        "                     \"maneuver\" : \"ramp-right\",\n" +
                        "                     \"polyline\" : {\n" +
                        "                        \"points\" : \"g}vuFzziUSIEAO?I@C?AAMG\"\n" +
                        "                     },\n" +
                        "                     \"start_location\" : {\n" +
                        "                        \"lat\" : 40.4272353,\n" +
                        "                        \"lng\" : -3.6601371\n" +
                        "                     },\n" +
                        "                     \"travel_mode\" : \"DRIVING\"\n" +
                        "                  },\n" +
                        "                  {\n" +
                        "                     \"distance\" : {\n" +
                        "                        \"text\" : \"1,5 km\",\n" +
                        "                        \"value\" : 1457\n" +
                        "                     },\n" +
                        "                     \"duration\" : {\n" +
                        "                        \"text\" : \"1 min\",\n" +
                        "                        \"value\" : 72\n" +
                        "                     },\n" +
                        "                     \"end_location\" : {\n" +
                        "                        \"lat\" : 40.440575,\n" +
                        "                        \"lng\" : -3.6587551\n" +
                        "                     },\n" +
                        "                     \"html_instructions\" : \"Incorpórate a \\u003cb\\u003eM-30 Lateral\\u003c/b\\u003e\",\n" +
                        "                     \"maneuver\" : \"merge\",\n" +
                        "                     \"polyline\" : {\n" +
                        "                        \"points\" : \"o_wuFfziU_CToBN{BLM@iEZeAFa@@O?a@?I?_@?WAE?c@Am@EMAWCc@GqASmAUiASWEyB_@_@GQCG?IAuDe@yAWsBWg@KOEQAOCYEc@GICYCa@GyCa@_BOe@Cu@E[CWA[Ai@AmB?\"\n" +
                        "                     },\n" +
                        "                     \"start_location\" : {\n" +
                        "                        \"lat\" : 40.4276049,\n" +
                        "                        \"lng\" : -3.660044\n" +
                        "                     },\n" +
                        "                     \"travel_mode\" : \"DRIVING\"\n" +
                        "                  },\n" +
                        "                  {\n" +
                        "                     \"distance\" : {\n" +
                        "                        \"text\" : \"2,8 km\",\n" +
                        "                        \"value\" : 2838\n" +
                        "                     },\n" +
                        "                     \"duration\" : {\n" +
                        "                        \"text\" : \"2 min\",\n" +
                        "                        \"value\" : 130\n" +
                        "                     },\n" +
                        "                     \"end_location\" : {\n" +
                        "                        \"lat\" : 40.4490668,\n" +
                        "                        \"lng\" : -3.632721799999999\n" +
                        "                     },\n" +
                        "                     \"html_instructions\" : \"Toma la salida \\u003cb\\u003e5A\\u003c/b\\u003e para incorporarte a \\u003cb\\u003eA-2\\u003c/b\\u003e en dirección \\u003cb\\u003eZaragoza\\u003c/b\\u003e\",\n" +
                        "                     \"maneuver\" : \"ramp-right\",\n" +
                        "                     \"polyline\" : {\n" +
                        "                        \"points\" : \"qpyuFfriUMIAAC?CAC?AAuABg@BI?S@Y@U@YB_@D[B[Bg@D{@Hq@BUBU@U@I?E?C?G?G?GAE?CAC?OEGAICICEAOGMGUKKCGCGC[AOGUI[GSGQEQIECGEGGGGGIEKGKIUCGGSI[AC?AAA?AA?GEaAcEe@qB[mAAEc@gBMc@[kA[cASq@g@uAEOKYQg@K]AAOe@IYEOACQq@GMUy@KWq@yBs@_CEOM]Sm@yAuEc@qAu@_CGQOg@Ic@Ia@Iq@Gg@C[AUC_@Cs@?O?Q@c@@a@Ba@B]@GFm@?CL{ATkCb@{EXeDDg@H{@NeBFs@RwBD_@@O@KN_BB_@@KHaAHeA?ADu@Bc@DqA@m@?g@?_@?m@C{@Ao@GgACg@?GIaAEi@Ee@CYGs@MmAKmAAKK}AEc@IaA\"\n" +
                        "                     },\n" +
                        "                     \"start_location\" : {\n" +
                        "                        \"lat\" : 40.440575,\n" +
                        "                        \"lng\" : -3.6587551\n" +
                        "                     },\n" +
                        "                     \"travel_mode\" : \"DRIVING\"\n" +
                        "                  },\n" +
                        "                  {\n" +
                        "                     \"distance\" : {\n" +
                        "                        \"text\" : \"0,3 km\",\n" +
                        "                        \"value\" : 317\n" +
                        "                     },\n" +
                        "                     \"duration\" : {\n" +
                        "                        \"text\" : \"1 min\",\n" +
                        "                        \"value\" : 18\n" +
                        "                     },\n" +
                        "                     \"end_location\" : {\n" +
                        "                        \"lat\" : 40.44924,\n" +
                        "                        \"lng\" : -3.6290239\n" +
                        "                     },\n" +
                        "                     \"html_instructions\" : \"Toma la salida \\u003cb\\u003e7\\u003c/b\\u003e hacia \\u003cb\\u003eAv. 25 de Septiembre\\u003c/b\\u003e/\\u003cwbr/\\u003e\\u003cb\\u003eAv. Logroño\\u003c/b\\u003e\",\n" +
                        "                     \"maneuver\" : \"ramp-right\",\n" +
                        "                     \"polyline\" : {\n" +
                        "                        \"points\" : \"ue{uFnodUBC?A@C?A?C?G?EAI?EEo@Eg@Ee@G}AEuA?GEwAAI?]AQAo@AO?]?AA}@?e@?QBIDI\"\n" +
                        "                     },\n" +
                        "                     \"start_location\" : {\n" +
                        "                        \"lat\" : 40.4490668,\n" +
                        "                        \"lng\" : -3.632721799999999\n" +
                        "                     },\n" +
                        "                     \"travel_mode\" : \"DRIVING\"\n" +
                        "                  },\n" +
                        "                  {\n" +
                        "                     \"distance\" : {\n" +
                        "                        \"text\" : \"1,7 km\",\n" +
                        "                        \"value\" : 1681\n" +
                        "                     },\n" +
                        "                     \"duration\" : {\n" +
                        "                        \"text\" : \"2 min\",\n" +
                        "                        \"value\" : 117\n" +
                        "                     },\n" +
                        "                     \"end_location\" : {\n" +
                        "                        \"lat\" : 40.4494264,\n" +
                        "                        \"lng\" : -3.6091706\n" +
                        "                     },\n" +
                        "                     \"html_instructions\" : \"Incorpórate a \\u003cb\\u003eCalle de Josefa Valcárcel\\u003c/b\\u003e\",\n" +
                        "                     \"maneuver\" : \"merge\",\n" +
                        "                     \"polyline\" : {\n" +
                        "                        \"points\" : \"wf{uFjxcU?IAoAAq@AkAAcB?cB?{AEeBCaB?o@C}AGgHEoDC}ACcAAi@?a@AgAAo@A}A?{@AmC?_@CiF?A@O@kG?aB@{DAa@?Q?g@?s@?mA?gB@}B?}A?o@@}A?o@@m@?o@?m@?_@?eA@eA?s@Fo@?G\"\n" +
                        "                     },\n" +
                        "                     \"start_location\" : {\n" +
                        "                        \"lat\" : 40.44924,\n" +
                        "                        \"lng\" : -3.6290239\n" +
                        "                     },\n" +
                        "                     \"travel_mode\" : \"DRIVING\"\n" +
                        "                  },\n" +
                        "                  {\n" +
                        "                     \"distance\" : {\n" +
                        "                        \"text\" : \"0,3 km\",\n" +
                        "                        \"value\" : 299\n" +
                        "                     },\n" +
                        "                     \"duration\" : {\n" +
                        "                        \"text\" : \"1 min\",\n" +
                        "                        \"value\" : 53\n" +
                        "                     },\n" +
                        "                     \"end_location\" : {\n" +
                        "                        \"lat\" : 40.4510759,\n" +
                        "                        \"lng\" : -3.6077617\n" +
                        "                     },\n" +
                        "                     \"html_instructions\" : \"En la rotonda, toma la \\u003cb\\u003ecuarta\\u003c/b\\u003e salida en dirección \\u003cb\\u003eAv. de Logroño\\u003c/b\\u003e\",\n" +
                        "                     \"maneuver\" : \"roundabout-right\",\n" +
                        "                     \"polyline\" : {\n" +
                        "                        \"points\" : \"}g{uFh|_UBC@CBE@C@C@E@E@C@E?E@A?C?A?A@E?C?A?A?C?A?CAE?GAEAGAEAECEAECEACCCCCCCCACCCAECEAGACAC?E?E@E?E@EBE@EBEBCDEDCDABABA@?@A@?@A@?@ABUJE@E@E@IAC?CAA?ECEACCCCEC]k@Wc@[c@g@m@\"\n" +
                        "                     },\n" +
                        "                     \"start_location\" : {\n" +
                        "                        \"lat\" : 40.4494264,\n" +
                        "                        \"lng\" : -3.6091706\n" +
                        "                     },\n" +
                        "                     \"travel_mode\" : \"DRIVING\"\n" +
                        "                  },\n" +
                        "                  {\n" +
                        "                     \"distance\" : {\n" +
                        "                        \"text\" : \"0,2 km\",\n" +
                        "                        \"value\" : 250\n" +
                        "                     },\n" +
                        "                     \"duration\" : {\n" +
                        "                        \"text\" : \"1 min\",\n" +
                        "                        \"value\" : 30\n" +
                        "                     },\n" +
                        "                     \"end_location\" : {\n" +
                        "                        \"lat\" : 40.4525072,\n" +
                        "                        \"lng\" : -3.6055071\n" +
                        "                     },\n" +
                        "                     \"html_instructions\" : \"Mantente a la \\u003cb\\u003eizquierda\\u003c/b\\u003e para permanecer en \\u003cb\\u003eAv. de Logroño\\u003c/b\\u003e\",\n" +
                        "                     \"maneuver\" : \"keep-left\",\n" +
                        "                     \"polyline\" : {\n" +
                        "                        \"points\" : \"gr{uFns_Ui@w@{@wAa@s@cAcBO[AAWa@KQCGCGCEAGAGKa@\"\n" +
                        "                     },\n" +
                        "                     \"start_location\" : {\n" +
                        "                        \"lat\" : 40.4510759,\n" +
                        "                        \"lng\" : -3.6077617\n" +
                        "                     },\n" +
                        "                     \"travel_mode\" : \"DRIVING\"\n" +
                        "                  },\n" +
                        "                  {\n" +
                        "                     \"distance\" : {\n" +
                        "                        \"text\" : \"1,4 km\",\n" +
                        "                        \"value\" : 1402\n" +
                        "                     },\n" +
                        "                     \"duration\" : {\n" +
                        "                        \"text\" : \"2 min\",\n" +
                        "                        \"value\" : 137\n" +
                        "                     },\n" +
                        "                     \"end_location\" : {\n" +
                        "                        \"lat\" : 40.4604753,\n" +
                        "                        \"lng\" : -3.5931385\n" +
                        "                     },\n" +
                        "                     \"html_instructions\" : \"En la rotonda, toma la \\u003cb\\u003eprimera\\u003c/b\\u003e salida y continúa por \\u003cb\\u003eAv. de Logroño\\u003c/b\\u003e\",\n" +
                        "                     \"maneuver\" : \"roundabout-right\",\n" +
                        "                     \"polyline\" : {\n" +
                        "                        \"points\" : \"e{{uFle_U?K?IAKAICIEIEGEEEEECGCEAEAE?G?G@e@YIGGGIKGQQ]GIEGGESKGEEECCCEYWY_@sA}AyFyG_@c@WYo@u@KMSW]_@KMMOo@u@w@_AOQCEGIKQEEMUSe@Yq@e@wAc@qAQg@c@oAy@{BQe@iFsOCGUo@a@oAo@oBWu@\"\n" +
                        "                     },\n" +
                        "                     \"start_location\" : {\n" +
                        "                        \"lat\" : 40.4525072,\n" +
                        "                        \"lng\" : -3.6055071\n" +
                        "                     },\n" +
                        "                     \"travel_mode\" : \"DRIVING\"\n" +
                        "                  },\n" +
                        "                  {\n" +
                        "                     \"distance\" : {\n" +
                        "                        \"text\" : \"59 m\",\n" +
                        "                        \"value\" : 59\n" +
                        "                     },\n" +
                        "                     \"duration\" : {\n" +
                        "                        \"text\" : \"1 min\",\n" +
                        "                        \"value\" : 12\n" +
                        "                     },\n" +
                        "                     \"end_location\" : {\n" +
                        "                        \"lat\" : 40.4605133,\n" +
                        "                        \"lng\" : -3.5925357\n" +
                        "                     },\n" +
                        "                     \"html_instructions\" : \"Gira a la \\u003cb\\u003ederecha\\u003c/b\\u003e para continuar en \\u003cb\\u003eAv. de Logroño\\u003c/b\\u003e\",\n" +
                        "                     \"maneuver\" : \"turn-right\",\n" +
                        "                     \"polyline\" : {\n" +
                        "                        \"points\" : \"_m}uFbx|TLM@E?A@A?C@C?G?C?C?E?CACCMSk@\"\n" +
                        "                     },\n" +
                        "                     \"start_location\" : {\n" +
                        "                        \"lat\" : 40.4604753,\n" +
                        "                        \"lng\" : -3.5931385\n" +
                        "                     },\n" +
                        "                     \"travel_mode\" : \"DRIVING\"\n" +
                        "                  },\n" +
                        "                  {\n" +
                        "                     \"distance\" : {\n" +
                        "                        \"text\" : \"0,3 km\",\n" +
                        "                        \"value\" : 277\n" +
                        "                     },\n" +
                        "                     \"duration\" : {\n" +
                        "                        \"text\" : \"1 min\",\n" +
                        "                        \"value\" : 46\n" +
                        "                     },\n" +
                        "                     \"end_location\" : {\n" +
                        "                        \"lat\" : 40.4593771,\n" +
                        "                        \"lng\" : -3.5897912\n" +
                        "                     },\n" +
                        "                     \"html_instructions\" : \"Gira ligeramente a la \\u003cb\\u003ederecha\\u003c/b\\u003e hacia \\u003cb\\u003eCalle Manuel Aguilar Muñoz\\u003c/b\\u003e\",\n" +
                        "                     \"maneuver\" : \"turn-slight-right\",\n" +
                        "                     \"polyline\" : {\n" +
                        "                        \"points\" : \"em}uFjt|TGk@?A?U?S@K?G@EBKFWPi@@G@EHUBIX}@t@yB?APa@LSLOHKX_@HI@?@?DA\"\n" +
                        "                     },\n" +
                        "                     \"start_location\" : {\n" +
                        "                        \"lat\" : 40.4605133,\n" +
                        "                        \"lng\" : -3.5925357\n" +
                        "                     },\n" +
                        "                     \"travel_mode\" : \"DRIVING\"\n" +
                        "                  },\n" +
                        "                  {\n" +
                        "                     \"distance\" : {\n" +
                        "                        \"text\" : \"0,3 km\",\n" +
                        "                        \"value\" : 274\n" +
                        "                     },\n" +
                        "                     \"duration\" : {\n" +
                        "                        \"text\" : \"1 min\",\n" +
                        "                        \"value\" : 39\n" +
                        "                     },\n" +
                        "                     \"end_location\" : {\n" +
                        "                        \"lat\" : 40.4581053,\n" +
                        "                        \"lng\" : -3.5923929\n" +
                        "                     },\n" +
                        "                     \"html_instructions\" : \"Gira a la \\u003cb\\u003ederecha\\u003c/b\\u003e hacia \\u003cb\\u003eCalle de Antonio Sancha\\u003c/b\\u003e\",\n" +
                        "                     \"maneuver\" : \"turn-right\",\n" +
                        "                     \"polyline\" : {\n" +
                        "                        \"points\" : \"cf}uFdc|TTZ@BtAnBX^X`@?@^j@R^Pb@DPFVBRBJ?H@d@?^?ZAL\"\n" +
                        "                     },\n" +
                        "                     \"start_location\" : {\n" +
                        "                        \"lat\" : 40.4593771,\n" +
                        "                        \"lng\" : -3.5897912\n" +
                        "                     },\n" +
                        "                     \"travel_mode\" : \"DRIVING\"\n" +
                        "                  }\n" +
                        "               ],\n" +
                        "               \"traffic_speed_entry\" : [],\n" +
                        "               \"via_waypoint\" : []\n" +
                        "            }\n" +
                        "         ],\n" +
                        "         \"overview_polyline\" : {\n" +
                        "            \"points\" : \"ktsuF~}vUbIrJv@t@jAx@fAf@~D`BnAQvDo@vDs@jAOh@Eh@@X@dBXrBd@`@HN?JEPUW]Q_@GOQk@OUM_@Ym@sA_Bq@i@m@i@m@iAw@cB]e@YYWQg@]u@iA}@}ASu@Cg@?m@Bm@LD\\\\F^D`AB`@FP@A_@A_CBk@@m@DMDILGp@Cf@Nd@FVATKROV[Ze@PMPEtB_@~AY~@UfA_@~@e@l@i@h@i@X_@n@eAx@uB\\\\wADWHqADu@CgDIiDAoBMsABiAP_CTgBRkA\\\\uAPg@n@eAlAaBdC_Dp@cAn@eAfAoBh@mAr@uBn@}BZoAf@iCb@eCxAsH\\\\_CNs@l@mC~@iDr@oD~AcKn@eE`@sBhAqDhAqCxAqCdEoGrBkDtBaF|@gCr@}Bt@{Cj@mCPy@TyB^_ERiBBgA@w@@e@J{D?o@I{DM{DSkCe@kFMu@QeAUkAcA}Ca@sAwAsEc@iAeBaEuBmFgBaEeBaEiB}DcAmBkBuC_AwA[]k@a@}AeAa@]_BwAqAaAcB}@cCsA{@k@}ByAu@m@}AmAyCmBaCmAgCcAw@WcA]kDeAu@QcBi@kDgAeDqA_Bq@wHcDiAg@UW_A_@aEwAwE_B{BaA_GqCqCyAmGkDkE_CeHuDsAm@uBw@mA]_BWkCUcB@yCRkHp@yE`@iE^uBTkDh@kCb@qDj@kBVSIUAM@OIoFd@iCNoGb@q@@kA?aACwBSaGcAsDk@_Eg@mEo@yAWaBU{Di@eCSeCMwCAOKMC{CHo@By@H{CVsBJ[?YCe@K_Bm@[AOGq@Qe@MWM_@_@[u@Su@KIeCiKq@kCw@oCmAqDo@mB_CyHwGuSYkASsAQyBCcA@u@JiBxB_WhAmMTuCHyAF_CCqDMgD}@gKQaCEeA@KA]Y{ESoHAcCB[DI?ICaCCoD?_EIgEQeRImFKkTDyPAoCD}R?cE@yBFw@JQFSD_@Ca@IYKSOMWIS?WFURINCFAD[LY@QGk@w@s@gAqAeB}AkCsA_Ci@}@K]Km@AUQe@KKMGYCG@e@YQOc@{@MQ[QUUaKoL_EwE{BmCg@w@m@wAiAiDaCyGeH{SgAeDNSBK?UYaAGm@?i@Fe@\\\\oA|AwEPc@Zc@n@u@FAV^hCrDr@jAVt@N`A?nB\"\n" +
                        "         },\n" +
                        "         \"summary\" : \"M-30\",\n" +
                        "         \"warnings\" : [],\n" +
                        "         \"waypoint_order\" : []\n" +
                        "      }\n" +
                        "   ],\n" +
                        "   \"status\" : \"OK\"\n" +
                        "}";

*/

        try {
            JSONObject obj_JSONObject = new JSONObject(jsonFile);
            JSONArray jsonArrRoutes = obj_JSONObject.getJSONArray("routes");
            JSONObject jsonObjRoutes = (JSONObject) jsonArrRoutes.get(0);
            JSONObject jsonObjLegs = (JSONObject) ((JSONArray) jsonObjRoutes.get("legs")).get(0);
//-------------------------------------------------------------------------------------------------------------------------------------
            // Obtener la posicion inicial y final, distancia y tiempo:
            JSONObject jsonObjIni = (JSONObject) jsonObjLegs.get("start_location");
            Coordinate posIni = new Coordinate(jsonObjIni.getDouble("lat"), jsonObjIni.getDouble("lng"));
            JSONObject jsonObjFin = (JSONObject) jsonObjLegs.get("end_location");
            Coordinate posFin = new Coordinate(jsonObjFin.getDouble("lat"), jsonObjFin.getDouble("lng"));

            int distancia = ((JSONObject) jsonObjLegs.get("distance")).getInt("value"); // En metros
            distanciaRuta = distancia;
            int tiempo = ((JSONObject) jsonObjLegs.get("duration")).getInt("value"); // En segundos
//-------------------------------------------------------------------------------------------------------------------------------------
            JSONArray jsonArrSteps = (JSONArray) jsonObjLegs.get("steps");
            DecimalFormat formatoCoordenada = new DecimalFormat("#.######");

            arrCoordRuta = new ArrayList<Coordinate>();
            // Obtenermos la posicion final ya que la final y la inicial del siguiente son las mismas
            for (int i = 0; i < jsonArrSteps.length(); i++) {
                JSONObject step = (JSONObject) jsonArrSteps.get(i);
                JSONObject jsonObjPos = (JSONObject) step.get("end_location");

                double lat = Double.parseDouble(formatoCoordenada.format(jsonObjPos.getDouble("lat")));
                double lon = Double.parseDouble(formatoCoordenada.format(jsonObjPos.getDouble("lng")));
                Coordinate pos = new Coordinate(lat, lon);
                arrCoordRuta.add(pos);
            }

            System.out.println("----------2----" + arrCoordRuta.toString());


        } catch (JSONException e) {
            System.out.println("------ Error a la hora de parsear el JSON -------");
            e.printStackTrace();
        }
        return arrCoordRuta;
    }



//--------------------------- Busqueda en BBDD ----------------------------------------------------------------------------------------------------------

    private ArrayList<Integer> getArrIdsViasBBDD(ArrayList<Coordinate> arrCoordRuta){
        ArrayList<Integer> idsViasRuta = null;
        if (arrCoordRuta != null) {
            idsViasRuta = new ArrayList<Integer>();
            for (int i = 0; i < arrCoordRuta.size(); i++) {

                double latitud = arrCoordRuta.get(i).getLatitud();
                //	double latitud = 40.454093;
                double longitud = arrCoordRuta.get(i).getLongitud();
                try {
                    ArrayList<Integer> arrPosibles = getListaCallesPosibles(latitud, longitud, thisActivity);
                    for (int elem : arrPosibles)
                        if (!idsViasRuta.contains(elem))
                            idsViasRuta.add(elem);

                    // System.out.println("+++++++" + arrPosibles.toString());
                } catch (ClassNotFoundException e) {
                    e.printStackTrace();
                }
            }
            System.out.println("+++++++" + idsViasRuta.toString());
        }
        return idsViasRuta;
    }
















}



