import csv
import os
from re import findall
import codecs




def eliminarColumnaCompleta(nombreCarpeta="", nombreSinCsv="", nFileIni = "-1", nFileFin = "-1", nombreColumna = ""):
    with codecs.open(nombreCarpeta + "/" + nombreSinCsv + nFileIni + ".csv", 'r', encoding='utf-8',
                 errors='ignore') as csvfile:
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


def getTypicalAgeRangeOk(txtOld = ""):
    if(txtOld.replace(" ", "") == ""):
        return ""
    if(txtOld.upper().__contains__("DESCONOCIDA")):
        return ""
    arrPal = txtOld.split()
    # "DE 30 A 34 AÑOS"
    try:
        fIni = arrPal[1]
        fFin = arrPal[3]
        if (fIni > fFin):
            fIni, fFin = fFin, fIni
        txtFin = fIni + "-" + fFin
    except IndexError:
        txtFin = ""
        print("Distinto formato Rango Edad: ", txtOld)
    # En caso de que no siga el formato estandar
    if(findall('([0-9]{1})-([0-9]{1})', txtFin) == []):
        fIni = -1
        fFin = -1
        i = 1
        for elem in arrPal:
            if(fIni == fFin and findall('([0-9]{1})', elem) != []):
                if (fIni == -1):
                    fIni = elem
                fFin = elem
        if(fIni != fFin):
            if(fIni > fFin):
                fIni, fFin = fFin, fIni
            return fIni + "-" + fFin
        else:
            return ""
    return txtFin


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

def ponerColIdAlPrincipio(nombreCarpeta="", nombreSinCsv="", nFileIni = "-1", nFileFin = "-1", nombreColumna = ""):
    with open(nombreCarpeta + "/" + nombreSinCsv + nFileIni + ".csv") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")
        file = open(nombreCarpeta + "/" + nombreSinCsv + nFileFin + ".csv", "w")
        primeraLinea = True
        nRowId = -1
        for row in csvreader:
            if (primeraLinea):
                nRowId = row.index(nombreColumna)
                del row[nRowId]
                fila = nombreColumna + ";" + ";".join(row)
                primeraLinea = False
            else:
                id = row[nRowId]
                del row[nRowId]
                fila = id + ";" + ";".join(row)
            file.write(fila + os.linesep)
        file.close()




#---------------------------------------------------------------------------------------------------------------

def ejecutarCicloCarrilesFase2():
    nombreCarpeta = "ciclocarrilesCSV"
    nombreSinCsv = "ciclocarriles_IDs_"
    variosCambiosEnCicloCarriles(nombreCarpeta, nombreSinCsv, "1", "2")
    print("OK: variosCambiosEnCicloCarriles")
    eliminarColumnaCompleta(nombreCarpeta, nombreSinCsv, "2", "3", "FECHA")
    print("OK: eliminar FECHA")
    # OJO con eliminar este que hay que primero obtener los otros valores:
    eliminarColumnaCompleta(nombreCarpeta, nombreSinCsv, "3", "4", "MinSimpTol")
    print("OK: eliminar MinSimpTol")
    eliminarColumnaCompleta(nombreCarpeta, nombreSinCsv, "4", "5", "tipoVia")
    print("OK: eliminar tipoVia")
    ponerColIdAlPrincipio(nombreCarpeta, nombreSinCsv, "5", "6", "idVia")
    print("OK: idVia al prinicpio")


def ejecutarAccidentesBiciFase2():
    nombreCarpeta = "accidentesCSV"
    nombreSinCsv = "AccidentesBicicletas_IDs_"
    variosCambiosEnAccidentesBici(nombreCarpeta, nombreSinCsv, "1", "2")
    print("OK: variosCambiosEnAccidentesBici")
    ponerColIdAlPrincipio(nombreCarpeta, nombreSinCsv, "2", "3", "idVia")
    print("OK: idVia al prinicpio")

def ejecutarCallesTranquilasFase2():
    nombreCarpeta = "callesTranquiCSV"
    nombreSinCsv = "callesTranquilas_IDs_"
    variosCambiosEnCallesTranquilas(nombreCarpeta, nombreSinCsv, "1", "2")
    print("OK: variosCambiosEnCallesTranquilas")
    eliminarColumnaCompleta(nombreCarpeta, nombreSinCsv, "2", "3", "ID_TIPO")
    print("OK: eliminar ID_TIPO")
    ponerColIdAlPrincipio(nombreCarpeta, nombreSinCsv, "3", "4", "idVia")
    print("OK: idVia al prinicpio")


#---------------------------------------------------------------------------------------------------------------







