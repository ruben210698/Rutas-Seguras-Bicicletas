package com.example.androidrutasbicimadrid;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.content.ContextCompat;

import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;
import android.widget.LinearLayout;
import android.widget.TextView;

public class Main2Activity extends AppCompatActivity {

    String txtIncidencias = "";
    double notaRuta = -1;




    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

        try {
            Intent intent = getIntent();
            txtIncidencias = intent.getStringExtra("INCIDENCIAS");
            notaRuta = Double.parseDouble(intent.getStringExtra("NOTARUTA"));
        } catch (Exception e) {

        }

        TextView tv_NotaNum = (TextView) findViewById(R.id.tv_NotaNum);
        TextView tv_NotaTxt = (TextView) findViewById(R.id.tv_NotaTxt);
        TextView tv_Incidencias = (TextView) findViewById(R.id.tv_Incidencias);


        if (notaRuta < 0.0) {
            notaRuta = 0.0;
        }
        if (notaRuta > 10.0) {
            notaRuta = 10.0;
        }
        String notaTexto = "";
        if (notaRuta < 5) {
            notaTexto = "Suspenso";
            tv_NotaNum.setBackgroundColor(Color.RED);
        //    tv_NotaTxt.setBackgroundColor(Color.RED);
        } else if (notaRuta < 7){
            notaTexto = "Bien";
            tv_NotaNum.setBackgroundColor(Color.YELLOW);
      //      tv_NotaTxt.setBackgroundColor(Color.YELLOW);
        }
        else if(notaRuta<9) {
            notaTexto = "Notable";
            tv_NotaNum.setBackgroundColor(Color.rgb(255, 165, 0));
         //   tv_NotaTxt.setBackgroundColor(Color.rgb(255, 165, 0));
        }
        else {
            notaTexto = "Sobresaliente";
            tv_NotaNum.setBackgroundColor(Color.GREEN);
         //   tv_NotaTxt.setBackgroundColor(Color.GREEN);
        }
        tv_NotaNum.setText(notaRuta + "");
        tv_NotaTxt.setText(notaTexto);
        tv_Incidencias.setText(txtIncidencias + "");

    }













}
