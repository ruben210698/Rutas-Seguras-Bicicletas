import csv
import os
from re import findall

def variosCambiosEnCicloCarriles(nombreCarpeta="", nombreSinCsv="", nFileIni = "-1", nFileFin = "-1"):
    with open(nombreCarpeta + "/" + nombreSinCsv + nFileIni + ".csv") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")
        file = open(nombreCarpeta + "/" + nombreSinCsv + nFileFin + ".csv", "w")
        primeraLinea = True
        nColLong = -1
        nColDistMin = -1
        for row in csvreader:
            if (primeraLinea):
                fila = ";".join(row)
                nColLong = row.index("Longitud")
                nColDistMin = row.index("MinSimpTol")
                # Cambio nombres: tipoUso, nombreVia, distMaxExclusBici y longitud
                fila = fila.replace("Longitud", "longitud").replace("CAPA", "tipoUso")\
                            .replace("TX_NOMBRE", "nombreVia").replace("MaxSimpTol","distMaxExclusBici")
                #Añadir carrilExclusBici:
                fila = fila + ";" + "carrilExclusBici"
                # Añadir municipio:
                fila = fila + ";" + "municipio"
                primeraLinea = False
            else:
                # Cambiar la longitud de KM a metros
                row[nColLong] = (float(row[nColLong].replace(',', '.')) * 1000).__str__()
                fila = ";".join(row)

                #Añadir carrilExclusBici:
                if(float(row[nColDistMin].replace(',', '.')) == 0.0):
                    fila = fila + ";" + "0" # No tiene carril exclusivo para bicicletas
                else:
                    fila = fila + ";" + "1" # Si tiene

                # Añadir municipio:
                fila = fila + ";" + "Madrid"

            file.write(fila + os.linesep)
        file.close()
