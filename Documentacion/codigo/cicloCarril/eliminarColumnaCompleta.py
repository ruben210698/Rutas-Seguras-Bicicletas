import csv
import os
from re import findall

def eliminarColumnaCompleta(nombreCarpeta="", nombreSinCsv="", nFileIni = "-1", nFileFin = "-1", nombreColumna = ""):
    with open(nombreCarpeta + "/" + nombreSinCsv + nFileIni + ".csv") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")
        file = open(nombreCarpeta + "/" + nombreSinCsv + nFileFin + ".csv", "w")
        primeraLinea = True
        nRowColumna = -1
        for row in csvreader:
            if (primeraLinea):
                nRowColumna = row.index(nombreColumna)
                del row[nRowColumna]
                fila = ";".join(row)
                primeraLinea = False
            else:
                del row[nRowColumna]
                fila = ";".join(row)
            file.write(fila + os.linesep)
        file.close()
