package com.example.androidrutasbicimadrid;

public class CalleTranquila {
    private String nombreCalle;
    private double longitud;

    public CalleTranquila() {
        this.nombreCalle = "";
        this.longitud = 0;
    }

    public CalleTranquila(String nombreCalle, double longitud) {
        this.nombreCalle = nombreCalle;
        this.longitud = longitud;
    }

    public String getNombreCalle() {
        return nombreCalle;
    }

    public void setNombreCalle(String nombreCalle) {
        this.nombreCalle = nombreCalle;
    }

    public double getLongitud() {
        return longitud;
    }

    public void setLongitud(double longitud) {
        this.longitud = longitud;
    }
}
