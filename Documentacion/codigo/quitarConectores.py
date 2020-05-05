import csv
import os
from re import findall

def quitarConectores(nombreVia = ""):
    nombreVia = nombreVia.upper()
    listaPosibles = [' DEL ', ' DE ', ' Y ', ' LAS ', ' LA ', ' LOS ', ' A ', ' POR ', ' CON ',
                     ' EL ', ' EN ', ' O ', ' I ', ' AL ', ',', '-', 'S/N', ' JUNTO ', '_']
    for a in listaPosibles:
        if(nombreVia.__contains__(a)):
            nombreVia = nombreVia.replace(a, ' ')
    return nombreVia
