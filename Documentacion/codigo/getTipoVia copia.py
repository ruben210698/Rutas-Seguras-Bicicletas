import csv
import os
from re import findall

def getTipoVia(nombreViaIni = ""):
    if(nombreViaIni == ""):
        return ""
    arr = nombreViaIni.upper().split()
    # Para solo tener las primeras palabras y no por ejemplo Gran VIA
    nombreVia = arr[0]
    if (nombreVia.__contains__("CALLE")):
        return "Calle"
    elif (nombreVia.__contains__("PASEO")):
        return "Paseo"
    elif (nombreVia.__contains__("PLAZA")):
        return "Plaza"
    elif (nombreVia.__contains__("GLORIETA")):
        return "Glorieta"
    elif (nombreVia.__contains__("RONDA")):
        return "Ronda"
    elif (nombreVia.__contains__("CAMINO")):
        return "Camino"
    elif (nombreVia.__contains__("PISTA")):
        return "Pista"
    elif (nombreVia.__contains__("ANILLO")):
        return "Anillo"
    elif (nombreVia.__contains__("CRUCE")):
        return "Cruce"
    elif (nombreVia.__contains__("AUTOVIA")):
        return "Autovia"
    elif (nombreVia.__contains__("CARRETERA")):
        return "Carretera"
    elif (nombreVia.__contains__("PARQUE")):
        return "Parque"
    elif (nombreVia.__contains__("CUESTA")):
        return "Cuesta"
    elif (nombreVia.__contains__("CAÑADA")):
        return "Cañada"
    elif (nombreVia.__contains__("AVENIDA")):
        return "Avenida"
    elif (nombreVia.__contains__("BULEVAR")):
        return "Bulevar"
    elif (nombreVia.__contains__("JARDIN")):
        return "Jardin"
    elif (nombreVia.__contains__("PARTICULAR")):
        return "Particular"
    elif (nombreVia.__contains__("POLIGONO")):
        return "Poligono"
    elif (nombreVia.__contains__("GALERIA")):
        return "Galeria"
    elif (nombreVia.__contains__("ESCALINATA")):
        return "Escalinata"
    elif (nombreVia.__contains__("VIA")):
        return "Via"
    elif (nombreVia.__contains__("PASARELA")):
        return "Pasarela"
    elif (nombreVia.__contains__("PASAJE")):
        return "Pasaje"
    elif (nombreVia.__contains__("PUENTE")):
        return "Puente"
    elif (nombreVia.__contains__("COSTANILLA")):
        return "Costanilla"
    elif (nombreVia.__contains__("COLONIA")):
        return "Colonia"
    elif (nombreVia.__contains__("CARRERA")):
        return "Carrera"
    elif (nombreVia.__contains__("PLAZUELA")):
        return "Plazuela"
    elif (nombreVia.__contains__("ACCESO")):
        return "Acceso"
    elif (nombreVia.__contains__("POBLADO")):
        return "Poblado"
    elif (nombreVia.__contains__("PASADIZO")):
        return "Pasadizo"
    elif (nombreVia.__contains__("TRASERA")):
        return "Trasera"
    elif (nombreVia.__contains__("SENDA")):
        return "Senda"
    elif (nombreVia.__contains__("ARROYO")):
        return "Arroyo"
    elif (nombreVia.__contains__("VALLE")):
        return "Valle"
    elif (nombreVia.__contains__("AEROPUERTO")):
        return "Aeropuerto"
    elif (nombreVia.__contains__("PASO_ELEVADO")):
        return "Paso Elevado"
    elif (nombreVia.__contains__("SENDA_CICLABLE")):
        return "Senda Ciclable"
    elif (nombreVia.__contains__("PASAJE")):
        return "Pasaje"
    else:
        return ""
