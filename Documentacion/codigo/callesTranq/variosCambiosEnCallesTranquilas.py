import csv
import os
from re import findall

def variosCambiosEnCallesTranquilas(nombreCarpeta="", nombreSinCsv="", nFileIni = "-1", nFileFin = "-1"):
    with open(nombreCarpeta + "/" + nombreSinCsv + nFileIni + ".csv") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")
        file = open(nombreCarpeta + "/" + nombreSinCsv + nFileFin + ".csv", "w")
        primeraLinea = True
        for row in csvreader:
            if (primeraLinea):
                fila = ";".join(row)
                # Cambio nombres: OBJECTID, ID_EJE, ID_GRUPO, TX_CAPA, NU_DIRECCI, NU_DOBLE_S,
                #                 TX_NOMBRE, TX_NOMBRE_ y Shape_Leng
                fila = fila.replace("OBJECTID", "idObject").replace("ID_EJE", "idEje")\
                            .replace("ID_GRUPO", "idGrupo").replace("TX_CAPA","tipoUso").replace("NU_DIRECCI","nuDireccion")\
                            .replace("NU_DOBLE_S", "nuDobleS").replace("TX_NOMBRE_","nombreViaReduc")\
                            .replace("TX_NOMBRE","nombreVia").replace("Shape_Leng","longitud")
                # Añadir municipio:
                fila = fila + ";" + "municipio"
                primeraLinea = False
            else:
                fila = ";".join(row)
                # Añadir municipio:
                fila = fila + ";" + "Madrid"
            file.write(fila + os.linesep)
        file.close()
