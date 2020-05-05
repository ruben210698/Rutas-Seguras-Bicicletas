import csv
import os
from re import findall

def cambiosBasicos(nombreCarpeta="", nombreSinCsv="", nRowNombre=-1, nFileFin = "-1"):
    with open(nombreCarpeta + "/" + nombreSinCsv + ".csv") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")
        file = open(nombreCarpeta + "/" + nombreSinCsv + nFileFin + ".csv", "w")
        primeraLinea = True
        for row in csvreader:
            if (primeraLinea):
                fila = ";".join(row)
                primeraLinea = False
            else:
                nombreVia = row[nRowNombre].upper()
                if (nombreVia.__contains__("C/")):
                    nombreVia = nombreVia.replace("C/", "C/ ")
                if (findall('CRUCE\s.*\sCON\s', nombreVia) != []):  # Escritura estandar de "Cruce"
                    nombreVia = nombreVia.replace(" CON ", " / ")
                    nombreVia = nombreVia.replace("CRUCE ", "")
                if(nombreVia.__contains__("S/N")):  # P.ej. SAN FRANCISCO S/N, casos que generan error
                    nombreVia = nombreVia.replace('S/N', "")
                if (findall('([A-z, C!, ·, 0-9]{1})/[A-z]{1}', nombreVia) != []):  # Escritura estandar de "Cruce"
                    nombreVia = nombreVia.replace("/", " / ")
                # C/  MONASTERIO DE ARLANZA-AV. SANTUARIO DE VALVERDE
                if (findall('(?!\d)[\-{1}](?!\d)', nombreVia) != []): # Evitar palabras con numeros como M-30
                    arr1 = nombreVia.replace("-", " - ").split()
                    if(getTipoVia(palablasMalEscritas(arr1[arr1.index("-")+1])) != ""):  # Si es palabra clave indicadora de nueva via, es Cruce
                        nombreVia = nombreVia.replace("-", " / ")
                if (findall('(?!\d)[\-{1}](\d)', nombreVia) != []): # Palabras con numero como M-30
                    nombreVia = nombreVia.replace("-", "")

                # ;19:10;"CAMINO EN ZONA DENOMIDADA COMO ""ESPACIO MÉXICO""";
                if (nombreVia.__contains__('"')): #Quitar comillas
                    nombreVia = nombreVia.replace('"', ' ')
                if (nombreVia.__contains__("PASO ELEVADO")):
                    nombreVia = nombreVia.replace('PASO ELEVADO', 'PASO_ELEVADO')
                elif (nombreVia.__contains__("SENDA CICLABLE")):
                    nombreVia = nombreVia.replace('SENDA CICLABLE', 'SENDA_CICLABLE')

                #Cambios varios en nueva funcion
                nombreVia = palablasMalEscritas(nombreVia)

                row[nRowNombre] = nombreVia
                fila = ";".join(row)
            file.write(fila + os.linesep)
        file.close()
