package com.example.androidrutasbicimadrid;

public class CicloCarril {
    private String nombreCalle;
    private double longitud;
    private boolean carrilExclusBici;

    public CicloCarril() {
        this.nombreCalle = "";
        this.longitud = 0;
        this.carrilExclusBici = false;
    }

    public CicloCarril(String nombreCalle, double longitud, boolean carrilExclusBici) {
        this.nombreCalle = nombreCalle;
        this.longitud = longitud;
        this.carrilExclusBici = carrilExclusBici;
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

    public boolean isCarrilExclusBici() {
        return carrilExclusBici;
    }

    public void setCarrilExclusBici(boolean carrilExclusBici) {
        this.carrilExclusBici = carrilExclusBici;
    }
}
