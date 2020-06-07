import csv
import os
from re import findall




def getTipoVia(nombreViaIni = ""):
    if(nombreViaIni.replace(" ", "") == ""):
        return ""
    arr = nombreViaIni.upper().split()
    # Para solo tener las primeras palabras y no por ejemplo Gran VIA
    nombreVia = arr[0]
    if (nombreVia.__contains__("CALLE")):
        return "Calle"
    elif (nombreVia.__contains__("CUESTA")):
        return "CUESTA"
    elif (nombreVia.__contains__("PASEO")):
        return "Paseo"
    elif (nombreVia.__contains__("PLAZA")):
        return "Plaza"
    elif (nombreVia.__contains__("GLORIETA")):
        return "Glorieta"
    elif (nombreVia.__contains__("CAMINO")):
        return "Camino"
    elif (nombreVia.__contains__("PISTA")):
        return "Pista"
    elif (nombreVia.__contains__("ANILLO")):
        return "Anillo"
    elif (nombreVia.__contains__("CRUCE")):
        return "Cruce"
    elif (nombreVia.__contains__("AUTOVIA")):
        return "Autovia"
    elif (nombreVia.__contains__("CARRETERA")):
        return "Carretera"
    elif (nombreVia.__contains__("AVENIDA")):
        return "Avenida"
    elif (nombreVia.__contains__("BULEVAR")):
        return "Bulevar"
    elif (nombreVia.__contains__("VIA")):
        return "Via"
    elif (nombreVia.__contains__("PASARELA")):
        return "Pasarela"
    elif (nombreVia.__contains__("PASAJE")):
        return "Pasaje"
    elif (nombreVia.__contains__("CARRERA")):
        return "Carrera"
    elif (nombreVia.__contains__("ACCESO")):
        return "Acceso"
    elif (nombreVia.__contains__("POBLADO")):
        return "Poblado"
    elif (nombreVia.__contains__("PASADIZO")):
        return "Pasadizo"
    elif (nombreVia.__contains__("SENDA")):
        return "Senda"
    elif (nombreVia.__contains__("VALLE")):
        return "Valle"
    elif (nombreVia.__contains__("ESCALINATA")):
        return "ESCALINATA"
    elif (nombreVia.__contains__("PASO_ELEVADO")):
        return "Paso Elevado"
    elif (nombreVia.__contains__("SENDA_CICLABLE")):
        return "Senda Ciclable"
    elif (nombreVia.__contains__("GALERIA")):
        return "Galeria"
    elif (nombreVia.__contains__("CAÑADA")):
        return "Cañada"
    elif (nombreVia.__contains__("AUTOPISTA")):
        return "Autopista"
    elif (nombreVia.__contains__("POLIGONO")):
        return "Poligono"
    elif (nombreVia.__contains__("RONDA")):
        return "Ronda"
    elif (nombreVia.__contains__("AEROPUERTO")):
        return "Aeropuerto"
    elif (nombreVia.__contains__("PUENTE")):
        return "Puente"
    elif (nombreVia.__contains__("TRAVESIA")):
        return "Travesia"
    elif (nombreVia.__contains__("PLAZUELA")):
        return "Plazuela"
    elif (nombreVia.__contains__("CALLEJON")):
        return "Callejon"
    elif (nombreVia.__contains__("COSTANILLA")):
        return "Costanilla"
    elif (nombreVia.__contains__("JARDIN")):
        return "Jadin"
    elif (nombreVia.__contains__("ARROYO")):
        return "Arroyo"
    elif (nombreVia.__contains__("PARTICULAR")):
        return "Particular"
    elif (nombreVia.__contains__("TRASERA")):
        return "Trasera"
    elif (nombreVia.__contains__("COLONIA")):
        return "Colonia"
    else:
        return ""

def quitarConectores(nombreVia = ""):
    nombreVia = nombreVia.upper()
    listaPosibles = ['DEL', 'DE', 'Y', 'LAS', 'LA', 'LOS', 'A', 'POR', 'CON',
                     'EL', 'EN', 'O', 'I', 'AL', ',', '-', 'S/N', 'JUNTO', '_', 'SOBRE',
                     'ENTRE', 'FRENTE']
    for a in listaPosibles:
        if(nombreVia.__contains__(a)):
            if(nombreVia.__contains__(' ' + a + ' ')):
                nombreVia = nombreVia.replace(' ' + a + ' ', " ")
            elif( # Para evitar que pertenezca a una palabra
            (findall('([A-z, 0-9, \s, À-ÿ]{1})' + a, nombreVia) == [] or findall('([A-z, 0-9, \s, À-ÿ]{1})' + a, nombreVia) == [' '])
            and (findall(a + '([A-z, 0-9,\s, À-ÿ]{1})', nombreVia) == [] or findall(a + '([A-z, 0-9,\s, À-ÿ]){1}', nombreVia) == [' '] )):
                nombreVia = nombreVia.replace(a, " ")
    return nombreVia


def quitarTextoEntreParentesis(nombreVia = ""):
    # Quitar texto entre parentesis:
    if(nombreVia.__contains__("(") and nombreVia.__contains__(")")):
        posIni = nombreVia.index("(")
        posFin = nombreVia.index(")")
        txtElim = nombreVia[posIni:posFin+1]
        return nombreVia.replace(txtElim, "")
    if (nombreVia.__contains__("(")):
        posIni = nombreVia.index("(")
        txtElim = nombreVia[posIni:]
        return nombreVia.replace(txtElim, "")
    else:
        return nombreVia


def quitarPalabrasConflicto(nombreVia = ""):
    nombreVia = nombreVia.upper()
    if(nombreVia == ""):
        return ""
    if(nombreVia.__contains__("\"")):
        nombreVia = nombreVia.replace("\"", "")
    nombreVia = quitarTextoEntreParentesis(nombreVia)

    listaPalabrasQuitar = ["CRUCE", "CALLE", "PASEO", "PLAZA", "GLORIETA", "CAMINO", "PISTA",
                           "AUTOVIA", "CARRETERA", "CUESTA", "AVENIDA", "VIA", "PASARELA",
                           "PASAJE", "COSTANILLA", "COLONIA", "POLIGONO", "CARRERA", "PLAZUELA", "BULEVAR",
                           "ESCALINATA", "JARDIN", "PARTICULAR",  "ACCESO", "POBLADO",
                           "PASADIZO", "TRASERA", "SENDA", "GALERIA", "VALLE",
                           "PASO_ELEVADO", "SENDA_CICLABLE", "ANILLO", "TRAVESIA", "ESTACION_FERROCARRIL",
                           "CAÑADA", "AUTOPISTA", "RONDA", "AEROPUERTO", "PUENTE", "CALLEJON",
                           "COLPB.", "INS.", "IDB."]

    for a in listaPalabrasQuitar:

        if(nombreVia.__contains__(a)):
            existePalQuit = False
            if (nombreVia.__contains__(' ' + a + ' ')):
                existePalQuit = True
                arr = nombreVia.split()

            elif (  # Para evitar que pertenezca a una palabra
            (findall('([A-z, 0-9, \s, À-ÿ]{1})' + a, nombreVia) == [] or findall('([A-z, 0-9, \s, À-ÿ]{1})' + a, nombreVia) == [' '])
            and (findall(a + '([A-z, 0-9,\s, À-ÿ]{1})', nombreVia) ==[] or findall(a + '([A-z, 0-9,\s, À-ÿ]){1}', nombreVia) ==[' '] )):
                #Para evitar errores por ejemplo en SegoVIA
                #Para evitar errores por ejemplo en PUENTECESURES
                arr = nombreVia.split()
                existePalQuit = True


            if (existePalQuit and arr.index(a) == 0): # Para evitar suprimir Gran VIA p.ej. (que este al inicio) ó FRANCISCO JOSÉ ARROYO
                nombreVia = nombreVia.replace(a, ' ')
            if (existePalQuit and nombreVia.__contains__('/') and findall('[A-z, À-ÿ]{1}' + '/', nombreVia) == []):
                if (arr.index(a) == arr.index('/') + 1):  # Para cuando es un cruce
                    nombreVia = nombreVia.replace(a + ' ', ' ')


        # Podria ser M11 por ejemplo
    if(nombreVia.replace(" ", "") != "" and nombreVia.strip()[0] == '/'):
        # Para eliminar descripciones al inicio y su / p.ej. SENDA_CICLABLE / AV.ROSALES / CARRET.VILLAV. A VALLECA
        nombreVia = nombreVia.replace('/', '', 1)
    return nombreVia

def palablasMalEscritas(nombreCalle = ""):  #Arreglar errores de codificación y abreviaturas
    if(nombreCalle == ""):
        return ""
    if (nombreCalle.__contains__(")")):
        nombreCalle = nombreCalle.replace(")", " ) ")
    if (nombreCalle.__contains__("(")):
        nombreCalle = nombreCalle.replace("(", " ( ")

    nuevaPalabra = ""
    for palabra in nombreCalle.split():
        palabra = palabra.replace(" ", "").upper()
        if(palabra == "PNTE."):
            palabra = "PUENTE"
        elif (palabra == "CÑADA." or palabra == "CÑADA"):
            palabra = "CAÑADA"
        elif (palabra == "AVDA." or palabra == "AVDA" or palabra == "AV." or palabra == "AV"):
            palabra = "AVENIDA"
        elif (palabra.__contains__("AV.")):
            palabra = palabra.replace("AV.", "AVENIDA")
        elif (palabra == "JARDÍN" or palabra == "JARDINES"):
            palabra = "JARDIN"
        elif (palabra == "CUSTA." or palabra == "CUSTA"):
            palabra = "CUESTA"
        elif (palabra == "POLÍGONO" or palabra == "POLIG."):
            palabra = "POLIGONO"
        elif (palabra == "GALERÍA"):
            palabra = "GALERIA"
        elif (palabra == "PLAZA."):
            palabra = "PLAZA"
        elif (palabra == "PISTA."):
            palabra = "PISTA"
        elif (palabra == "CMNO." or palabra == "CMNO"):
            palabra = "CAMINO"
        elif (palabra == "BULEV."):
            palabra = "BULEVAR"
        elif (palabra == "RONDA."):
            palabra = "RONDA"
        elif (palabra == "GTA." or palabra == "GTA"):
            palabra = "GLORIETA"
        elif (palabra == "CUSTA." or palabra == "CUSTA"):
            palabra = "CUESTA"
        elif (palabra == "PQUE." or palabra == "PQUE"):
            palabra = "PARQUE"
        elif (palabra == "CTRA." or palabra == "CTRA" or palabra == "CRA." or palabra == "CARRET."):
            palabra = "CARRETERA"
        elif (palabra.__contains__("CARRET.")):
            palabra.replace("CARRET.", "CARRETERA")
        elif (palabra == "AUTOV." or palabra == "AUTOV"):
            palabra = "AUTOVIA"
        elif (palabra == "CRUCE."):
            palabra = "CRUCE"
        elif (palabra == "ANILLO."):
            palabra = "ANILLO"
        elif (palabra == "PASEO."):
            palabra = "PASEO"
        elif(palabra == "TRVA."):
            palabra = "TRAVESIA"
        elif(palabra == "ESTFE."):
            palabra = "ESTACION_FERROCARRIL"
        elif (palabra == "P?"):
            palabra = "PLAZA"
        elif (palabra == "PZA."):
            palabra = "PLAZA"
        elif (palabra == "C¬" or palabra == "CALL." or palabra == "CALL" or palabra == "C/" or palabra == "C?"):
            palabra = "CALLE"
        elif (palabra == "GRAL"):
            palabra = "GENERAL"
        elif (palabra == "STA." or palabra == "STA"):
            palabra = "SANTA"
        elif (palabra == "PTA."):
            palabra = "PUERTA"
        elif (palabra == "PALAC."):
            palabra = "PALACIO"
        elif (palabra == "METRO."):
            palabra = "METRO"

        elif(palabra.__contains__("Ý")):
            palabra = palabra.replace("Ý", "Í")
        elif (palabra.__contains__("±")):
            palabra = palabra.replace("±", "Ñ")
        elif (findall('([B-DF-HJ-NP-TV-Z]{1})SS', palabra) != [] or findall('SS([B-DF-HJ-NP-TV-Z]{1})', palabra) != []):
            #P.ej. BSSRBARA ó NARVSSEZ ó GUZMSSN Ó "Ortega Y GASSET" Ó ALCALSS
            palabra = palabra.replace("SS", "Á")
        elif (findall('([A-z]{1})·N', palabra) != []):  #P.ej. SAHAG·N
            palabra = palabra.replace("·N", "ÚN")
        elif (palabra[0] == '?'):  #P.ej. ?LVAREZ --> ? ASCII 63
            palabra = palabra.replace("?", "Á")
        elif (palabra.__contains__(chr(190))):  #P.ej. MOSCARD¾ --> ASCII 190, PER¾N
            palabra = palabra.replace(chr(190), "Ó")
        elif (palabra.__contains__(chr(179))):  #P.ej. MOSCARD¾ --> ASCII 179, YAG³E
            palabra = palabra.replace(chr(179), "Ü")
        elif (findall('QUÚ', palabra) != []):  # P.ej MarquÚs --> Marqués
            palabra = palabra.replace("QUÚ", "QUÉ")
        elif (palabra == "JES·S"):
            palabra = "JESÚS"

        #Quitar numeros (posiblemente de portales, los nombres propios son en numeros romanos)
        elif (findall('[0-9]{1}', palabra) != []):
            for a in findall('[0-9]{1}', palabra):
                palabra = palabra.replace(a, '')
            if(findall('[A-Z, À-ÿ]{3}', palabra) == []):
                # En el caso de que le acompañen 1 o 2 letras (letras de portal)
                palabra = ""
        nuevaPalabra = nuevaPalabra + " " + palabra
    return nuevaPalabra





def cambiosBasicos(nombreCarpeta="", nombreSinCsv="", nRowNombre=-1, nFileIni = "-1", nFileFin = "-1", separarCruces = False):
    with open(nombreCarpeta + "/" + nombreSinCsv + nFileIni + ".csv") as csvfile:
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
                if (separarCruces and findall('CRUCE\s.*\sCON\s', nombreVia) != []):  # Escritura estandar de "Cruce"
                    nombreVia = nombreVia.replace(" CON ", " / ")
                    nombreVia = nombreVia.replace("CRUCE ", "")
                if (separarCruces and findall('\sCON\s', nombreVia) != []):  # Escritura estandar de "Cruce"
                    nombreVia = nombreVia.replace(" CON ", " / ")
                if (nombreVia.__contains__(", CALLE")):
                    nombreVia = nombreVia.replace(", CALLE", " / CALLE")
                if (nombreVia.__contains__("-AV.")):
                    nombreVia = nombreVia.replace("-AV.", " / AVENIDA")
                if (nombreVia.__contains__("-CARRET.")):
                    nombreVia = nombreVia.replace("-CARRET.", " / CARRET.")

                if (nombreVia.__contains__(", FRENTE ")): # Solo si contiene coma
                    posIni = nombreVia.index(", FRENTE ")
                    nombreVia = nombreVia.replace(nombreVia[posIni:], "") # Eliminarlo
                if (nombreVia.__contains__("FAROLA ") or nombreVia.__contains__("FAROLAS ")):
                    posIni = 0
                    if(nombreVia.__contains__("FAROLA ")):
                        posIni = nombreVia.index("FAROLA ")
                    if (nombreVia.__contains__("FAROLAS ")):
                        posIni = nombreVia.index("FAROLAS ")
                    if(nombreVia[posIni:].__contains__(",")):
                        posFin = nombreVia[posIni:].index(",")
                        nombreVia = nombreVia.replace(nombreVia[posIni:posFin], "")
                    elif(nombreVia[posIni:].__contains__("/")):
                        posFin = nombreVia[posIni:].index("/")
                        nombreVia = nombreVia.replace(nombreVia[posIni:posFin], "")
                    else:
                        nombreVia = nombreVia.replace(nombreVia[posIni:], "")  # Eliminarlo
                if(nombreVia.__contains__("S/N")):  # P.ej. SAN FRANCISCO S/N, casos que generan error
                    nombreVia = nombreVia.replace('S/N', "")
                if (nombreVia.__contains__("KM-0")):  # Palabras con numero como KM-0 (quitar)
                    nombreVia = nombreVia.replace('KM-0', "")
                if (nombreVia.__contains__("PKM")):  # Eliminar PKM
                    nombreVia = nombreVia.replace('PKM', "")
                if (nombreVia.__contains__("C/ ")):
                    nombreVia = nombreVia.replace("C/ ", "CALLE ")
                if (findall('([A-z, ·, 0-9, À-ÿ]{1})/[A-z]{1}', nombreVia) != []):  # Escritura estandar de "Cruce"
                    nombreVia = nombreVia.replace("/", " / ")
                # C/  MONASTERIO DE ARLANZA-AV. SANTUARIO DE VALVERDE
                if (findall('([A-z, ·, 0-9, À-ÿ]{1})/', nombreVia) != []):  # Escritura estandar de "Cruce"
                    nombreVia = nombreVia.replace("/", " /")
                if (findall('/[A-z, À-ÿ]{1}', nombreVia) != []):  # Escritura estandar de "Cruce"
                    nombreVia = nombreVia.replace("/", "/ ")
                if (findall('(?!\d)[\-{1}](?!\d)', nombreVia) != []): # Evitar palabras con numeros como M-30
                    arr1 = nombreVia.replace("-", " - ").split()
                    if(separarCruces and getTipoVia(palablasMalEscritas(arr1[arr1.index("-")+1])) != ""):  # Si es palabra clave indicadora de nueva via, es Cruce
                        nombreVia = nombreVia.replace("-", " / ")
                if (findall('(?!\d)[\-{1}](\d)', nombreVia) != []): # Palabras con numero como M-30
                    nombreVia = nombreVia.replace("-", "")

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







# OJOOO Solo para accidentes:
def annadirEsCruceAccidentes(nombreCarpeta = "", nombreSinCsv = "", nRowNombre = -1, nFileIni = "-1", nFileFin = "-1"):
    with open(nombreCarpeta + "/" + nombreSinCsv + nFileIni + ".csv") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")
        file = open(nombreCarpeta + "/" + nombreSinCsv + nFileFin + ".csv", "w")
        primeraLinea = True
        for row in csvreader:
            if (primeraLinea):
                fila = ";".join(row)
                fila = fila + ";" + "esCruce"
                primeraLinea = False
            else:
                fila = ";".join(row)
                if (row[nRowNombre].__contains__(" / ")):
                    fila = fila + ";" + "1"
                else:
                    fila = fila + ";" + "0"
            file.write(fila + os.linesep)
        file.close()


def annadirTipoVia(nombreCarpeta = "", nombreSinCsv = "", nRowNombre = -1, nFileIni = "-1", nFileFin = "-1"):
    with open(nombreCarpeta + "/" + nombreSinCsv + nFileIni + ".csv") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")
        file = open(nombreCarpeta + "/" + nombreSinCsv + nFileFin + ".csv", "w")
        primeraLinea = True
        for row in csvreader:
            if (primeraLinea):
                fila = ";".join(row)
                fila = fila + ";" + "tipoVia"
                primeraLinea = False
            else:
                tipoVia = getTipoVia(row[nRowNombre])
                fila = ";".join(row)
                fila = fila + ";" + tipoVia
            file.write(fila + os.linesep)
        file.close()



def annadirPalabrasClave(nombreCarpeta = "", nombreSinCsv = "", nRowNombre = -1, nFileIni = "-1", nFileFin = "-1"):
    with open(nombreCarpeta + "/" + nombreSinCsv + nFileIni + ".csv") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")
        file = open(nombreCarpeta + "/" + nombreSinCsv + nFileFin + ".csv", "w")
        primeraLinea = True
        for row in csvreader:
            if (primeraLinea):
                fila = ";".join(row)
                fila = fila + ";" + "palabrasClave"
                primeraLinea = False
            else:
                palabrasClave = quitarConectores(row[nRowNombre])
                palabrasClave = quitarPalabrasConflicto(palabrasClave)
                # Eliminar espacios innecesarios:
                palabrasClave = palabrasClave.replace("     ", " ").replace("    ", " ")\
                                            .replace("   ", " ").replace("  ", " ")
                #Eliminar espacios al principio y al final
                try:
                    if(len(palabrasClave)>1 and palabrasClave[0] == " "):
                        palabrasClave = palabrasClave.replace(" ", "", 1)
                    if(len(palabrasClave)>1 and palabrasClave[len(palabrasClave)-1] == " "):
                        palabrasClave = palabrasClave[0: len(palabrasClave)-1]
                except IndexError:
                    print("annadirPalabrasClave: Fuera de rango :: ", palabrasClave)
                fila = ";".join(row)
                fila = fila + ";" + palabrasClave
            file.write(fila + os.linesep)
        file.close()


def copiarNombreViaOrigin(nombreCarpeta = "", nombreSinCsv = "", nRowNombre = -1, nFileFin = "-1"):
    with open(nombreCarpeta + "/" + nombreSinCsv + ".csv") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")
        file = open(nombreCarpeta + "/" + nombreSinCsv + nFileFin + ".csv", "w")
        primeraLinea = True
        for row in csvreader:
            if (primeraLinea):
                fila = "nombreOriginal;"
                fila = fila + ";".join(row)
                primeraLinea = False
            else:
                fila = row[nRowNombre] + ";"
                fila = fila + ";".join(row)
            file.write(fila + os.linesep)
        file.close()


#--------------Funciopnes para obtener las calles, si hay cruce, en forma de array--------------------------------------
def getArrCallesRec(nombreDataset = ""):
    listaNombres = []
    if (nombreDataset.__contains__('/')):
        n1 = nombreDataset.split().index('/')
        txtRestante = " ".join(nombreDataset.split()[n1 + 1:])
        nombre = " ".join(nombreDataset.split()[0:n1])
        elemRecursiv = getArrCallesRec(txtRestante)
        listaNombres = [nombre, elemRecursiv]
    else:
        listaNombres = [nombreDataset]

    return listaNombres

def getArrCalles(nombreDataset = ""):
    list1 = getArrCallesRec(nombreDataset)
    txt = list1.__str__().replace('[', '').replace(']', '')
    list3 = []
    nombre=""

    for elem in txt.split():
        if(elem.__contains__("'") and nombre != ""):
            nombre = nombre + " " + elem.replace("'", "").replace(",", "")
            list3.append(nombre)
            nombre = ""
        elif (elem.__contains__("'") and nombre == "" and elem.replace("'", "", 1).__contains__("'")):
            nombre = elem.replace("'", "").replace(",", "")
            list3.append(nombre)
            nombre = ""
        elif (elem.__contains__("'") and nombre == ""):
            nombre = elem.replace("'", "").replace(",", "")
        else:
            nombre = nombre + " " + elem
    return list3


def separarCucesAccidentes(nombreCarpeta = "", nombreSinCsv = "", nRowNombre = -1, nFileIni = "-1", nFileFin = "-1"):
    with open(nombreCarpeta + "/" + nombreSinCsv + nFileIni + ".csv") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")
        file = open(nombreCarpeta + "/" + nombreSinCsv + nFileFin + ".csv", "w")
        primeraLinea = True
        nColPalClav = -1
        nColEsCruce = -1
        for row in csvreader:
            if (primeraLinea):
                fila = ";".join(row)
                nColPalClav = row.index("CALLE")
                nColEsCruce = row.index("esCruce")
                primeraLinea = False
                fila = ";".join(row)
                file.write(fila + os.linesep)
            elif(row[nColEsCruce] == "1"):
                arrCalles = getArrCalles(row[nColPalClav])
                # Se le asigna a cada registro una de las calles
                for calle in arrCalles:
                    row[nColPalClav] = calle
                    row[nColEsCruce] = arrCalles.__len__().__str__()
                    fila = ";".join(row)
                    file.write(fila + os.linesep)
            else:
                fila = ";".join(row)
                file.write(fila + os.linesep)
        file.close()

#---------------------------------------



def ejecutarCallejero():
    nombreCarpeta = "callejeroCSV"
    nombreSinCsv = "callejeroMadrid"
    nRowNombre = 3+1 #de la nombreOrigin añadido
    copiarNombreViaOrigin(nombreCarpeta, nombreSinCsv, nRowNombre-1, "0")
    print("OK: copiarNombreViaOrigin")
    cambiosBasicos(nombreCarpeta, nombreSinCsv, nRowNombre, "0", "1")
    annadirTipoVia(nombreCarpeta, nombreSinCsv, nRowNombre, "1", "3")
    annadirPalabrasClave(nombreCarpeta, nombreSinCsv, nRowNombre, "3", "4")

def ejecutarAccidentes():
    nombreCarpeta = "accidentesCSV"
    nombreSinCsv = "AccidentesBicicletas"
    nRowNombre = 3+1 #de la nombreOrigin añadido
    copiarNombreViaOrigin(nombreCarpeta, nombreSinCsv, nRowNombre-1, "0")
    print("OK: copiarNombreViaOrigin")
    cambiosBasicos(nombreCarpeta, nombreSinCsv, nRowNombre, "0", "1", True)
    print("OK: cambiosBasicos")
    annadirEsCruceAccidentes(nombreCarpeta, nombreSinCsv, nRowNombre, "1", "2") ## OJOO Solo accidentes
    print("OK: annadirEsCruceAccidentes")
    separarCucesAccidentes(nombreCarpeta, nombreSinCsv, nRowNombre, "2", "3")
    print("OK: separarCucesAccidentes")
    annadirTipoVia(nombreCarpeta, nombreSinCsv, nRowNombre, "3", "4")
    print("OK: annadirTipoVia")
    annadirPalabrasClave(nombreCarpeta, nombreSinCsv, nRowNombre, "4", "5")
    print("OK: annadirPalabrasClave")

def ejecutarCicloCarriles():
    nombreCarpeta = "ciclocarrilesCSV"
    nombreSinCsv = "ciclocarriles"
    nRowNombre = 1+1 #de la nombreOrigin añadido
    copiarNombreViaOrigin(nombreCarpeta, nombreSinCsv, nRowNombre-1, "0")
    print("OK: copiarNombreViaOrigin")
    cambiosBasicos(nombreCarpeta, nombreSinCsv, nRowNombre, "0", "1", False)
    print("OK: cambiosBasicos")
    annadirTipoVia(nombreCarpeta, nombreSinCsv, nRowNombre, "1", "4")
    print("OK: annadirTipoVia")
    annadirPalabrasClave(nombreCarpeta, nombreSinCsv, nRowNombre, "4", "5")
    print("OK: annadirPalabrasClave")

def ejecutarCallesTranquilas():
    nombreCarpeta = "callesTranquiCSV"
    nombreSinCsv = "callesTranquilas"
    nRowNombre = 7+1 #de la nombreOrigin añadido
    copiarNombreViaOrigin(nombreCarpeta, nombreSinCsv, nRowNombre-1, "0")
    print("OK: copiarNombreViaOrigin")
    cambiosBasicos(nombreCarpeta, nombreSinCsv, nRowNombre, "0", "1", False)
    print("OK: cambiosBasicos")
    annadirTipoVia(nombreCarpeta, nombreSinCsv, nRowNombre, "1", "4")
    print("OK: annadirTipoVia")
    annadirPalabrasClave(nombreCarpeta, nombreSinCsv, nRowNombre, "4", "5")
    print("OK: annadirPalabrasClave")
#---------------------------------------------------------------------------------------------------------------






