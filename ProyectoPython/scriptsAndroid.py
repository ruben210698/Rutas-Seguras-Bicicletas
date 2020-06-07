import csv
import os
from re import findall
import math


def crearArraysNombresCalles():
    file = open("callejeroCSV/callejeroMadridArrayJava.java", 'w')

    with open("callejeroCSV/callejeroMadrid.csv") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")
        primeraLinea = True
        contador = 1
        file.write("private String[] callesArr = {")
        for row in csvreader:
            if (primeraLinea):
                fila = ";".join(row)
                primeraLinea = False
            else:
                nombreVia = "\"" + row[1].replace(" ", "") + " "
                nombreVia = nombreVia + row[2].replace("  ", " ") + " "
                nombreVia = nombreVia + row[3].replace("  ", " ") + "\""
                file.write(nombreVia + ",")
                if(contador %10 == 0):
                    file.write("\n")
        file.close()


crearArraysNombresCalles()