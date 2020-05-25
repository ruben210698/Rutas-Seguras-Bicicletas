package com.example.androidrutasbicimadrid;

public class Coordinate {
    double latitud;
    double longitud;

    public Coordinate(double latitud, double longitud) {
        this.latitud = latitud;
        this.longitud = longitud;
    }

    public double getLatitud() {
        return latitud;
    }

    public void setLatitud(double latitud) {
        this.latitud = latitud;
    }

    public double getLongitud() {
        return longitud;
    }

    public void setLongitud(double longitud) {
        this.longitud = longitud;
    }

    @Override
    public String toString() {
        return "Coordinate (lat, long) {" +
                + latitud +
                ", " + longitud +
                '}';
    }

    // Si hago el metodo equals que tenga un pelin de margen de error
}

