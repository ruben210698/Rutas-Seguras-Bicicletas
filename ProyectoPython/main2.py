import analizCalles
import generadorIdsCalles
import os
import csv

import time
from re import findall

import fase2EdicionDataSets


def cicloCarrilesCompleto():
    analizCalles.ejecutarCicloCarriles()
    generadorIdsCalles.ejecutarCicloCarrilesIDs()


def accidentesCompleto():
    analizCalles.ejecutarAccidentes()
    generadorIdsCalles.ejecutarAccidentesIDs()

def callesTranquilasCompleto():
    analizCalles.ejecutarCallesTranquilas()
    generadorIdsCalles.ejecutarCallesTranqIDs()

def cicloCarrilesCompleto():
    analizCalles.ejecutarCicloCarriles()
    generadorIdsCalles.ejecutarCicloCarrilesIDs()


def callejeroCompleto_BASE():
    analizCalles.ejecutarCallejero()
    #generadorIdsCalles.ejecutarCallejeroIDs_Fuente()
    nombreCarpeta = "callejeroCSV"
    nombreSinCsv = "callejeroMadrid"
    #"callejeroCSV" + "/" + "nombres_IDs" + ".csv")
    with open(nombreCarpeta + "/" + nombreSinCsv + "3" + ".csv") as csvfile:
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

fase2EdicionDataSets.ejecutarCicloCarrilesFase2()


# ---------------------------------------------------------------------------------------------------------------
print("------------------------------------")
end = time.time()
print("Tiempo Transcurrido: ", end - start)
# ---------------------------------------------------------------------------------------------------------------
