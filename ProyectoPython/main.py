import analizCalles
import generadorIdsCalles
import os
import csv

import time

import fase2EdicionDataSets
from tratamientoDataCoordenadas import ejecutarTransformacionDatasetCoordenadas


def cicloCarrilesCompleto():
    callejeroCompleto_BASE()
    analizCalles.ejecutarCicloCarriles()
    generadorIdsCalles.ejecutarCicloCarrilesIDs()


def accidentesCompleto():
    callejeroCompleto_BASE()
    analizCalles.ejecutarAccidentes()
    generadorIdsCalles.ejecutarAccidentesIDs()
    fase2EdicionDataSets.ejecutarAccidentesBiciFase2()

def callesTranquilasCompleto():
    callejeroCompleto_BASE()
    analizCalles.ejecutarCallesTranquilas()
    generadorIdsCalles.ejecutarCallesTranqIDs()
    fase2EdicionDataSets.ejecutarCallesTranquilasFase2()

def cicloCarrilesCompleto():
    callejeroCompleto_BASE()
    analizCalles.ejecutarCicloCarriles()
    generadorIdsCalles.ejecutarCicloCarrilesIDs()
    fase2EdicionDataSets.ejecutarCicloCarrilesFase2()




def callejeroCompleto_BASE():
    analizCalles.ejecutarCallejero()
    nombreCarpeta = "callejeroCSV"
    nombreSinCsv = "callejeroMadrid"
    fase2EdicionDataSets.ponerColIdAlPrincipio(nombreCarpeta, nombreSinCsv, "4", "5", "COD_VIA")

    with open(nombreCarpeta + "/" + nombreSinCsv + "5" + ".csv") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")
        file = open(nombreCarpeta + "/" + "nombres_IDs" + ".csv", "w")
        for row in csvreader:
            fila = ";".join(row)
            file.write(fila + os.linesep)
    file.close()
    print("-----------callejero OK-------")

# ---------------------------------------------------------------------------------------------------------------
start = time.time()
print("------------------------------------")
# ---------------------------------------------------------------------------------------------------------------


cicloCarrilesCompleto()

#ejecutarTransformacionDatasetCoordenadas()



#fase2EdicionDataSets.ejecutarCallesTranquilasFase2()







# ---------------------------------------------------------------------------------------------------------------
print("------------------------------------")
end = time.time()
print("Tiempo Transcurrido: ", end - start)
# ---------------------------------------------------------------------------------------------------------------
