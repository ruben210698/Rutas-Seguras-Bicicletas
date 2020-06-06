package com.example.androidrutasbicimadrid;

public class Accidente {
    private String nombreCalle;
    private String uriLesividad;
    private String uriTipoPersAfect;
    private String hora;

    public Accidente() {
        this.nombreCalle = "";
        this.uriLesividad = "";
        this.uriTipoPersAfect = "";
        this.hora = "";
    }

    public Accidente(String nombreCalle, String uriLesividad, String uriTipoPersAfect, String hora) {
        this.nombreCalle = nombreCalle;
        this.uriLesividad = uriLesividad;
        this.uriTipoPersAfect = uriTipoPersAfect;
        this.hora = hora;
    }

    public String getNombreCalle() {
        return nombreCalle;
    }

    public void setNombreCalle(String nombreCalle) {
        this.nombreCalle = nombreCalle;
    }

    public String getUriLesividad() {
        return uriLesividad;
    }

    public void setUriLesividad(String uriLesividad) {
        this.uriLesividad = uriLesividad;
    }

    public String getUriTipoPersAfect() {
        return uriTipoPersAfect;
    }

    public void setUriTipoPersAfect(String uriTipoPersAfect) {
        this.uriTipoPersAfect = uriTipoPersAfect;
    }

    public String getHora() {
        return hora;
    }

    public void setHora(String hora) {
        this.hora = hora;
    }
}
