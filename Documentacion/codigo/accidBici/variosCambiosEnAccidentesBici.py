import csv
import os
from re import findall

def variosCambiosEnAccidentesBici(nombreCarpeta="", nombreSinCsv="", nFileIni = "-1", nFileFin = "-1"):
    with open(nombreCarpeta + "/" + nombreSinCsv + nFileIni + ".csv") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")
        file = open(nombreCarpeta + "/" + nombreSinCsv + nFileFin + ".csv", "w")
        primeraLinea = True
        nColTypicalAge = -1
        nColGender = -1
        for row in csvreader:
            if (primeraLinea):
                fila = ";".join(row)
                nColTypicalAge = row.index("RANGO EDAD")
                nColGender = row.index("SEXO")
                # Cambio nombres: NºExpediente, FECHA, HORA, CALLE, NÚMERO , DISTRITO, TIPO ACCIDENTE,
                #                 ESTADO METEREOLÓGICO, TIPO VEHÍCULO, TIPO PERSONA, RANGO EDAD, SEXO, LESIVIDAD*
                fila = fila.replace("Nº  EXPEDIENTE", "numeroExpediente").replace("FECHA", "fecha")\
                            .replace("HORA", "hora").replace("CALLE","nombreVia").replace("NÚMERO","portal")\
                            .replace("DISTRITO", "distrito").replace("TIPO ACCIDENTE","tipoAccidente")\
                            .replace("ESTADO METEREOLÓGICO","meteorologia").replace("TIPO VEHÍCULO", "tipoVehiculo")\
                            .replace("TIPO PERSONA", "tipoPersonaAfectada").replace("RANGO EDAD", "typicalAgeRange")\
                            .replace("SEXO", "gender").replace("LESIVIDAD*", "lesividad")
                # Añadir municipio:
                fila = fila + ";" + "municipio"
                primeraLinea = False
            else:
                # Modificar el Genero:
                generoEspan = row[nColGender]
                if(generoEspan == "Hombre"):
                    row[nColGender] = "Male"
                elif(generoEspan == "Mujer"):
                    row[nColGender] = "Female"

                # Modificar TypicalAgeRange
                row[nColTypicalAge] = getTypicalAgeRangeOk(row[nColTypicalAge])

                fila = ";".join(row)
                # Añadir municipio:
                fila = fila + ";" + "Madrid"
            file.write(fila + os.linesep)
        file.close()
