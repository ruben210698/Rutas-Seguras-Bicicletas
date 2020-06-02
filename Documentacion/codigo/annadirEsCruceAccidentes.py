import csv
import os
from re import findall

def annadirEsCruceAccidentes(nombreCarpeta = "", nombreSinCsv = "", nRowNombre = -1, nFileIni = "-1", nFileFin = "-1"):
with open(nombreCarpeta + "/" + nombreSinCsv + nFileIni + ".csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=";")
    file = open(nombreCarpeta + "/" + nombreSinCsv + nFileFin + ".csv", "w")
    primeraLinea = True
    for row in csvreader:
        if (primeraLinea):
            fila = ";".join(row)
            fila = fila + ";" + "esCruce"
            primeraLinea = False
        else:
            fila = ";".join(row)
            if (row[nRowNombre].__contains__(" / ")):
                fila = fila + ";" + "1"
            else:
                fila = fila + ";" + "0"
        file.write(fila + os.linesep)
    file.close()
