import csv
import os
from re import findall
import math
from fase2EdicionDataSets import eliminarColumnaCompleta

# 0.0001389 +-= 0.00015 = 15m
# 1km = 0.00926 coordDec =+- 0.01


#primero 2 digitos de LAT y luego 2 digitos de LON
ARRLAT = [40.31, 40.32, 40.33, 40.34, 40.35, 40.36, 40.37, 40.38, 40.39, 40.4,
          40.41, 40.42, 40.43, 40.44, 40.45, 40.46, 40.47, 40.48, 40.49, 40.5,
          40.51, 40.52, 40.53, 40.54, 40.55, 40.56, 40.57, 40.58, 40.6, 40.61]

ARRLON = [-3.84, -3.83, -3.82, -3.81, -3.8, -3.79, -3.78, -3.77, -3.76, -3.75,
          -3.74, -3.73, -3.72, -3.71, -3.7, -3.69, -3.68, -3.67, -3.66, -3.65,
          -3.64, -3.63, -3.62, -3.61, -3.6, -3.59, -3.58, -3.57, -3.56, -3.55,
          -3.54, -3.53, -3.52]

def asignarCuadrante(nombreCarpeta="", nombreSinCsv="", nFileIni = "-1", nFileFin = "-1"):
    with open(nombreCarpeta + "/" + nombreSinCsv + nFileIni + ".csv") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")
        file = open(nombreCarpeta + "/" + nombreSinCsv + nFileFin + ".csv", "w")
        primeraLinea = True
        nColLon = -1
        nColLat = -1
        contador = 0
        for row in csvreader:
            if (primeraLinea):
                fila = ";".join(row)
                nColLat = row.index('LATITUD')
                nColLon = row.index('LONGITUD')
                fila = fila + ";" + "codCuadrante"
                primeraLinea = False
            else:
                numCuadrante = 0 #primero 2 digitos de LAT y luego 2 digitos de LON
                # Latitud:
                txt = row[nColLat]  # 40.4105972
                dato = float(txt)
                round(dato, 2)
                sumTotal = round(dato, 2)
                dato = float(sumTotal)
                if (ARRLAT.__contains__(dato)):
                    numCuadrante = ARRLAT.index(dato)*100
                else:
                    numCuadrante = 0
                    print("----Error con Lat: ", sumTotal)
                # Longitud:
                txt = row[nColLon]  # 40.4105972
                dato = float(txt)
                sumTotal = round(dato, 2)
                dato = float(sumTotal)
                if (ARRLON.__contains__(dato)):
                    numCuadrante = numCuadrante + ARRLON.index(dato)
                else:
                    print("----Error con Long: ", sumTotal)

                fila = ";".join(row)
                fila = fila + ";" + numCuadrante.__str__()

            contador = contador + 1
            file.write(fila + os.linesep)
            if(contador%10000==0):
                print(contador)
        file.close()


# Código copiado de:
# https://stackoverflow.com/questions/343865/how-to-convert-from-utm-to-latlng-in-python-or-javascript/344083#344083
# http://www.juntadeandalucia.es/economiainnovacioncienciayempleo/pam/ConvED50.action
# La zona, obtenida de la web de la junta de Andalucia, es 30.
def utmToLatLng(zone, easting, northing, northernHemisphere=True):
    if not northernHemisphere:
        northing = 10000000 - northing
    a = 6378137
    e = 0.081819191
    e1sq = 0.006739497
    k0 = 0.9996

    arc = northing / k0
    mu = arc / (a * (1 - math.pow(e, 2) / 4.0 - 3 * math.pow(e, 4) / 64.0 - 5 * math.pow(e, 6) / 256.0))

    ei = (1 - math.pow((1 - e * e), (1 / 2.0))) / (1 + math.pow((1 - e * e), (1 / 2.0)))

    ca = 3 * ei / 2 - 27 * math.pow(ei, 3) / 32.0

    cb = 21 * math.pow(ei, 2) / 16 - 55 * math.pow(ei, 4) / 32
    cc = 151 * math.pow(ei, 3) / 96
    cd = 1097 * math.pow(ei, 4) / 512
    phi1 = mu + ca * math.sin(2 * mu) + cb * math.sin(4 * mu) + cc * math.sin(6 * mu) + cd * math.sin(8 * mu)

    n0 = a / math.pow((1 - math.pow((e * math.sin(phi1)), 2)), (1 / 2.0))

    r0 = a * (1 - e * e) / math.pow((1 - math.pow((e * math.sin(phi1)), 2)), (3 / 2.0))
    fact1 = n0 * math.tan(phi1) / r0

    _a1 = 500000 - easting
    dd0 = _a1 / (n0 * k0)
    fact2 = dd0 * dd0 / 2

    t0 = math.pow(math.tan(phi1), 2)
    Q0 = e1sq * math.pow(math.cos(phi1), 2)
    fact3 = (5 + 3 * t0 + 10 * Q0 - 4 * Q0 * Q0 - 9 * e1sq) * math.pow(dd0, 4) / 24

    fact4 = (61 + 90 * t0 + 298 * Q0 + 45 * t0 * t0 - 252 * e1sq - 3 * Q0 * Q0) * math.pow(dd0, 6) / 720

    lof1 = _a1 / (n0 * k0)
    lof2 = (1 + 2 * t0 + Q0) * math.pow(dd0, 3) / 6.0
    lof3 = (5 - 2 * Q0 + 28 * t0 - 3 * math.pow(Q0, 2) + 8 * e1sq + 24 * math.pow(t0, 2)) * math.pow(dd0, 5) / 120
    _a2 = (lof1 - lof2 + lof3) / math.cos(phi1)
    _a3 = _a2 * 180 / math.pi

    latitude = 180 * (phi1 - fact1 * (fact2 + fact3 + fact4)) / math.pi

    if not northernHemisphere:
        latitude = -latitude

    longitude = ((zone > 0) and (6 * zone - 183.0) or 3.0) - _a3

    return (latitude, longitude)







def calcularCoordenadasDecimales(nombreCarpeta="", nombreSinCsv="", nFileIni = "-1", nFileFin = "-1"):
    with open(nombreCarpeta + "/" + nombreSinCsv + nFileIni + ".csv") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")
        file = open(nombreCarpeta + "/" + nombreSinCsv + nFileFin + ".csv", "w")
        primeraLinea = True
        nColEasting = -1
        nColNorthing = -1
        nColLat = -1
        nColLon = -1
        contador = 0
        for row in csvreader:
            if (primeraLinea):
                fila = ";".join(row)
                nColEasting = row.index("UTMX_ETRS")
                nColNorthing = row.index("UTMY_ETRS")
                nColLat = row.index("LATITUD")
                nColLon = row.index("LONGITUD")
                primeraLinea = False
            else:
                # Calculo del numero decimal:
              #  print("---", nColEasting)
                utmx = float(row[nColEasting].replace(",", "."))  #438104,97
                utmy = float(row[nColNorthing].replace(",", "."))   # 438104,97
                latitud, longitud = utmToLatLng(30, utmx, utmy, True)


                # Redondea a 5 decimales (distancia +- 1 metro)
                row[nColLat] = round(latitud, 5).__str__()
                row[nColLon] = round(longitud, 5).__str__()

               # print(latitud, " ", longitud)
                # print(sumTotal)
               # row[nCol] = sumTotal

                fila = ";".join(row)

            contador = contador + 1
            file.write(fila + os.linesep)
            if(contador%10000==0):
                print(contador)
        file.close()

def sacarTodosLosDif001(nombreCarpeta="", nombreSinCsv="", nFileIni = "-1", nameCol = "", lenguaje = "Python"):
    with open(nombreCarpeta + "/" + nombreSinCsv + nFileIni + ".csv") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")
        primeraLinea = True
        nCol = -1
        contador = 0
        arrElem=[]
        for row in csvreader:
            if (primeraLinea):
                nCol = row.index(nameCol)
                primeraLinea = False
            else:
                #0.01 dif --> 2 decimales
                txt = row[nCol] #40.4105972
                dato = float(txt)
                sumTotal = "%.2f" % dato
                dato = float(sumTotal)
                if(not(arrElem.__contains__(dato))):
                    arrElem.append(dato)

            contador = contador + 1
            if(contador%10000==0):
                print(contador)
        arrElem.sort()
        if(lenguaje == "Python"):
            print(arrElem)
        elif(lenguaje == "Java"):
            txtFinal = "final static double[] ARR" + nameCol + " = {"
       #     {'a', 'b', 'c', 'd', 'e'};
            for elem in arrElem:
                txtFinal = txtFinal + ", " + elem.__str__()
            txtFinal = txtFinal.replace(",", "", 1)
            txtFinal = txtFinal + " };"
            print(txtFinal)
        else:
            print("Lenguaje no reconocido")
        print(arrElem.__len__())





def ejecutarTransformacionDatasetCoordenadas():
    nombreCarpeta = "callejeroCoorden"
    nombreSinCsv = "datasetCoordenadas"
    eliminarColumnaCompleta(nombreCarpeta, nombreSinCsv, "", "1", "VIA_CLASE")
    print("-----Ok1")
    eliminarColumnaCompleta(nombreCarpeta, nombreSinCsv, "1", "2", "VIA_PAR")
    eliminarColumnaCompleta(nombreCarpeta, nombreSinCsv, "2", "1", "VIA_NOMBRE")
    print("-----Ok2")
    eliminarColumnaCompleta(nombreCarpeta, nombreSinCsv, "1", "2", "VIA_NOMBRE_ACENTOS")
    eliminarColumnaCompleta(nombreCarpeta, nombreSinCsv, "2", "1", "CLASE_APP")
    print("-----Ok3")
    eliminarColumnaCompleta(nombreCarpeta, nombreSinCsv, "1", "2", "NUMERO")
    eliminarColumnaCompleta(nombreCarpeta, nombreSinCsv, "2", "1", "CALIFICADOR")
    print("-----Ok4")
    eliminarColumnaCompleta(nombreCarpeta, nombreSinCsv, "1", "2", "TIPO_NDP")
    eliminarColumnaCompleta(nombreCarpeta, nombreSinCsv, "2", "1", "COD_NDP")
    print("-----Ok5")
    eliminarColumnaCompleta(nombreCarpeta, nombreSinCsv, "1", "2", "UTMY_ED")
    eliminarColumnaCompleta(nombreCarpeta, nombreSinCsv, "2", "1", "UTMX_ED")
    eliminarColumnaCompleta(nombreCarpeta, nombreSinCsv, "1", "3", "ANGULO_ROTULACION")
    print("-----Ok6")

    print("-----Ok6")
    calcularCoordenadasDecimales(nombreCarpeta, nombreSinCsv, "3", "4")
    calcularCoordenadasDecimales(nombreCarpeta, nombreSinCsv, "4", "5")
    print("-----Ok7")
    eliminarColumnaCompleta(nombreCarpeta, nombreSinCsv, "5", "4", "UTMY_ETRS")
    eliminarColumnaCompleta(nombreCarpeta, nombreSinCsv, "4", "5", "UTMX_ETRS")
    print("-----Ok8")
    asignarCuadrante(nombreCarpeta, nombreSinCsv, "5", "6")




def generarFichBBDDAndroid():
    f = open("callejeroCoorden/sql/datasetCoordSQLITE.sql", "r")

    count = 1
    nArray = 0
    matrizIds = "int[][] matrizIds = {"
    matrizLat = "double[][] matrizLat = {"
    matrizLon = "double[][] matrizLon = {"

    arrayIds = ""
    arrayLat = ""
    arrayLon = ""
    for row in f:
        row = row.replace("\n", "")
        idVia = row[1:row.index(",")].replace(" ", "")
        row = row[row.index(",")+2:]
        codPostal = row[0:row.index('\'')].replace(" ", "")
        row = row[row.index('\'') + 2:]
        latitud = row[0:row.index(',')].replace(" ", "")
        row = row[row.index(',') + 1:]
        longitud = row[0:row.index(',')].replace(" ", "")
        row = row[row.index(',') + 1:]
        codCuadrante = row[0:row.index(')')].replace(" ", "")

        arrayIds = arrayIds + "," + idVia
        arrayLat = arrayLat + "," + latitud
        arrayLon = arrayLon + "," + longitud


        if (count % 8200 == 0):
            nArray = nArray+1
            fwIds = open("callejeroCoorden/sql/javaFiles/ArrayDatosCoordIds" + nArray.__str__() + ".java", 'w')
            fwLat = open("callejeroCoorden/sql/javaFiles/ArrayDatosCoordLat" + nArray.__str__() + ".java", 'w')
            fwLon = open("callejeroCoorden/sql/javaFiles/ArrayDatosCoordLon" + nArray.__str__() + ".java", 'w')

            fwIds.write("package com.example.rutasbicimadrid.sqlData;\n\n"+
                "public class ArrayDatosCoordIds" + nArray.__str__() +"{\n\n"+
                "public static int[] arrIds"+nArray.__str__()+" = { " + arrayIds.replace(",", "", 1) + " };\n\n}")
            fwLat.write("package com.example.rutasbicimadrid.sqlData;\n\n"+
                "public class ArrayDatosCoordLat" + nArray.__str__() +"{\n\n"+
                "public static double[] arrLat"+nArray.__str__()+" = { " + arrayLat.replace(",", "", 1) + " };\n\n}")
            fwLon.write("package com.example.rutasbicimadrid.sqlData;\n\n"+
                "public class ArrayDatosCoordLon" + nArray.__str__() +"{\n\n"+
                "public static double[] arrLon"+nArray.__str__()+" = { " + arrayLon.replace(",", "", 1) + " };\n\n}")
            matrizIds = matrizIds + "ArrayDatosCoordIds"+nArray.__str__()+".arrIds" + nArray.__str__() +", "
            matrizLat = matrizLat + "ArrayDatosCoordLat"+nArray.__str__()+".arrLat" + nArray.__str__() + ", "
            matrizLon = matrizLon + "ArrayDatosCoordLon"+nArray.__str__()+".arrLon" + nArray.__str__() + ", "
            arrayIds = ""
            arrayLat = ""
            arrayLon = ""
            fwIds.close()
            fwLat.close()
            fwLon.close()
        elif (count % 50 == 0):
            arrayIds = arrayIds+ "\n"
            arrayLat = arrayLat + "\n"
            arrayLon = arrayLon + "\n"

        count = count+1
        if(count%5000 == 0):
            print(count)

    nArray = nArray+1
    fwIds = open("callejeroCoorden/sql/javaFiles/ArrayDatosCoordIds" + nArray.__str__() + ".java", 'w')
    fwLat = open("callejeroCoorden/sql/javaFiles/ArrayDatosCoordLat" + nArray.__str__() + ".java", 'w')
    fwLon = open("callejeroCoorden/sql/javaFiles/ArrayDatosCoordLon" + nArray.__str__() + ".java", 'w')
    fwIds.write("package com.example.rutasbicimadrid.sqlData;\n\n" +
                "public class ArrayDatosCoordIds" + nArray.__str__() + "{\n\n" +
                "public static int[] arrIds" + nArray.__str__() + " = { " + arrayIds.replace(",", "", 1) + " };\n\n}")
    fwLat.write("package com.example.rutasbicimadrid.sqlData;\n\n" +
                "public class ArrayDatosCoordLat" + nArray.__str__() + "{\n\n" +
                "public static double[] arrLat" + nArray.__str__() + " = { " + arrayLat.replace(",", "",
                                                                                                1) + " };\n\n}")
    fwLon.write("package com.example.rutasbicimadrid.sqlData;\n\n" +
                "public class ArrayDatosCoordLon" + nArray.__str__() + "{\n\n" +
                "public static double[] arrLon" + nArray.__str__() + " = { " + arrayLon.replace(",", "",
                                                                                                1) + " };\n\n}")
    matrizIds = matrizIds + "ArrayDatosCoordIds" + nArray.__str__() + ".arrIds" + nArray.__str__() + "};"
    matrizLat = matrizLat + "ArrayDatosCoordLat" + nArray.__str__() + ".arrLat" + nArray.__str__() + "};"
    matrizLon = matrizLon + "ArrayDatosCoordLon" + nArray.__str__() + ".arrLon" + nArray.__str__() + "};"

    fwIds.close()
    fwLat.close()
    fwLon.close()
    fwIds = open("callejeroCoorden/sql/datasetCoordSQLITE2Ids.java", 'w')
    fwLat = open("callejeroCoorden/sql/datasetCoordSQLITE2Lat.java", 'w')
    fwLon = open("callejeroCoorden/sql/datasetCoordSQLITE2Lon.java", 'w')
    fwIds.write(matrizIds + "\n")
    fwLat.write(matrizLat + "\n")
    fwLon.write(matrizLon + "\n")
    f.close()
    fwIds.close()
    fwLat.close()
    fwLon.close()


generarFichBBDDAndroid()

