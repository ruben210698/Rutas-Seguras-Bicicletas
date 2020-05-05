import csv
import os
from re import findall

def annadirPalabrasClave(nombreCarpeta = "", nombreSinCsv = "", nRowNombre = -1, nFileIni = "-1", nFileFin = "-1"):
    with open(nombreCarpeta + "/" + nombreSinCsv + nFileIni + ".csv") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")
        file = open(nombreCarpeta + "/" + nombreSinCsv + nFileFin + ".csv", "w")
        primeraLinea = True
        for row in csvreader:
            if (primeraLinea):
                fila = ";".join(row)
                fila = fila + ";" + "PALABRAS_CLAVE"
                primeraLinea = False
            else:
                palabrasClave = quitarConectores(row[nRowNombre])
                palabrasClave = quitarPalabrasConflicto(palabrasClave)
                fila = ";".join(row)
                fila = fila + ";" + palabrasClave
            file.write(fila + os.linesep)
        file.close()
