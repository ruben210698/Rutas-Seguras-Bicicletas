import csv
import os
from re import findall


def quitarPalabrasConflicto(nombreVia = ""):
    nombreVia = nombreVia.upper()
    if(nombreVia == ""):
        return ""
    listaPalabrasQuitar = ["CRUCE. ", "CRUCE ", "CALL. ", "CALL ", "CALLE ", "C/", "C/ ", "PASEO. ", "PASEO ", "PLAZA.", "PLAZA ", "GTA. ",
    "GTA ", "GLORIETA ", "RONDA. ", "RONDA ",
    "CMNO. ", "CMNO ", "CAMINO ", "PISTA. ", "PISTA ", "AUTOVIA ", "CTRA. ",
    "CTRA ", "CARRETERA ", "PQUE. ", "PQUE ", "PARQUE ", "CUSTA. ", "CUSTA ", "CUESTA ", "CÑADA. ", "CÑADA ", "CAÑADA ", "AVDA. ",
    "AVDA ", "AV. ", "AV ", "AVENIDA ", "VIA ", "PASARELA ", "PASAJE ", "PUENTE ", "COSTANILLA ", "COLONIA ", "CARRERA ",
    "PLAZUELA ", "BULEVAR ", "BULEV. ", "ESCALINATA ", "JARDÍN ", "JARDIN ", "JARDINES ", "PARTICULAR ", "POLÍGONO ", "POLIGONO ", "ACCESO ",
    "POBLADO ", "PASADIZO ", "TRASERA ", "SENDA ", "GALERÍA ", "GALERIA ", "ARROYO ", "VALLE ", "AEROPUERTO ", "PASO_ELEVADO", "SENDA_CICLABLE"]

    for a in listaPalabrasQuitar:
        if(nombreVia.__contains__(a) and findall('[A-z]{1}' + a, nombreVia) == []): #Para evitar errores por ejemplo en SegoVIA
            arr = nombreVia.split()
            if (arr.index(a.replace(' ', '')) == 0):  # Para evitar suprimir Gran VIA p.ej.
                nombreVia = nombreVia.replace(a, ' ')
            if (nombreVia.__contains__('/') and findall('[A-z]{1}' + '/', nombreVia) == []):
                if (arr.index(a.replace(' ', '')) == arr.index('/') + 1):  # Para cuando es un cruce
                    nombreVia = nombreVia.replace(a, ' ')
      
        # Podria ser M11 por ejemplo
    if(nombreVia.strip()[0] == '/'):
        # Para eliminar descripciones al inicio y su / p.ej. SENDA_CICLABLE / AV.ROSALES / CARRET.VILLAV. A VALLECA
        nombreVia = nombreVia.replace('/', '', 1)
    return nombreVia
