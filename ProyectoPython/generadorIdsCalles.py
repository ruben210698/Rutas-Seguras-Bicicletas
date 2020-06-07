import csv
import os
from re import findall
import difflib
import unicodedata

POS_IS_CALL = 0
POS_PALCLAV_CALL = 12
POS_TIPVIA_CALL = 2
RUTA_CALLEJERO = "callejeroCSV/nombres_IDs.csv"



# Si es o no un tipo de calle que pueda haberse usado con otro nombre y por tanto omitible
def esTipoCalleOmitible(nombreVia = ""):
    if(nombreVia == ""):
        return True
    nombreVia = nombreVia.upper().replace("Á", "A").replace("É", "E").replace("Í", "I") \
            .replace("Ó", "O").replace("Ú", "U").replace("Ü", "U").replace(" ", "")
    if (nombreVia.__contains__("CALLE")):
        return True
    elif (nombreVia.__contains__("PASEO")):
        return True
    elif (nombreVia.__contains__("PLAZA")):
        return True
    elif (nombreVia.__contains__("GLORIETA")):
        return True
    elif (nombreVia.__contains__("CAMINO")):
        return True
    elif (nombreVia.__contains__("PISTA")):
        return True
    elif (nombreVia.__contains__("ANILLO")):
        return True
    elif (nombreVia.__contains__("CRUCE")):
        return True
    elif (nombreVia.__contains__("AUTOVIA")):
        return False #No pueden circular bicicletas
    elif (nombreVia.__contains__("CARRETERA")):
        return True
    elif (nombreVia.__contains__("AVENIDA")):
        return True
    elif (nombreVia.__contains__("BULEVAR")):
        return True
    elif (nombreVia.__contains__("VIA")):
        return True
    elif (nombreVia.__contains__("PASARELA")):
        return True
    elif (nombreVia.__contains__("PASAJE")):
        return True
    elif (nombreVia.__contains__("CARRERA")):
        return True
    elif (nombreVia.__contains__("ACCESO")):
        return True
    elif (nombreVia.__contains__("POBLADO")):
        return False
    elif (nombreVia.__contains__("PASADIZO")):
        return True
    elif (nombreVia.__contains__("SENDA")):
        return True
    elif (nombreVia.__contains__("VALLE")):
        return False
    elif (nombreVia.__contains__("ESCALINATA")):
        return False
    elif (nombreVia.__contains__("PASO_ELEVADO")):
        return False
    elif (nombreVia.__contains__("SENDA_CICLABLE")):
        return False


    elif (nombreVia.__contains__("GALERIA")):
        return False
    elif (nombreVia.__contains__("CAÑADA")):
        return False
    elif (nombreVia.__contains__("AUTOPISTA")):
        return False
    elif (nombreVia.__contains__("POLIGONO")):
        return False
    elif (nombreVia.__contains__("RONDA")):
        return False
    elif (nombreVia.__contains__("AEROPUERTO")):
        return False
    elif (nombreVia.__contains__("PUENTE")):
        return False
    elif (nombreVia.__contains__("TRAVESIA")):
        return True
    elif (nombreVia.__contains__("PLAZUELA")):
        return False
    elif (nombreVia.__contains__("CALLEJON")):
        return True
    elif (nombreVia.__contains__("COSTANILLA")):
        return False
    elif (nombreVia.__contains__("JARDIN")):
        return False
    elif (nombreVia.__contains__("ARROYO")):
        return False
    elif (nombreVia.__contains__("PARTICULAR")):
        return False
    elif (nombreVia.__contains__("TRASERA")):
        return False
    elif (nombreVia.__contains__("COLONIA")):
        return False
    return False

'''
Esto va a dar 4 vueltas:
1. chequea la palabra tal cual y mirando el tipo de via
2. NO mira el tipo de via y acepta 1 errata de añadir o eliminar 1 letra
3. Permite 1 letra cambiada (es decir 2 cambios uno de + y otro de -)
4. Permite 2 o más cambios

'''


# ------------------------------------------------------------------------------------------------------------------
# En la segunda vuelta también se omite el tipo de calle

def chequearPalabras(nombreCallej = "", nombreDataset = "", nVuelta = 1):
    if(nombreDataset.replace(" ", "") == "" or nombreCallej.replace(" ", "") == ""):
        return False
    nombreDataset = nombreDataset.upper().replace("Á", "A").replace("É", "E").replace("Í", "I") \
        .replace("Ó", "O").replace("Ú", "U").replace("Ü", "U").replace(",", " ").replace("-", " ")
    nombreCallej = nombreCallej.upper().replace("Á", "A").replace("É", "E").replace("Í", "I") \
        .replace("Ó", "O").replace("Ú", "U").replace("Ü", "U").replace(",", " ").replace("-", " ")

    # Comprobaciones básicas
    # ------------------------------------------------------------------------------------------------------------------
    if(unicodedata.normalize('NFKD', nombreCallej.replace(" ", "")).encode('ASCII', 'ignore').strip().upper() \
       == unicodedata.normalize('NFKD',nombreDataset.replace(" ", "")).encode('ASCII', 'ignore').strip().upper()):
        return True
    elif(nVuelta ==1):
        return False #La primera vuelta solo hace estas comprobación
    # ------------------------------------------------------------------------------------------------------------------
    longCadena1 = nombreDataset.__len__()
    longCadena2 = nombreCallej.__len__()
    if (longCadena1 < (longCadena2 * 0.7) or longCadena1 > (longCadena2 * 1.3)):
        return False # Si el tamaño de la cadena difiere mucho
    diff = difflib.ndiff(nombreCallej.replace(" ", ""), nombreDataset.replace(" ", ""))
    diferenciastxt = ''.join(diff)
    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------
    if(nVuelta == 2): # Excepciones cuando hay pequeños cambios que pueden deberse a errores ortograficos
        # Por ejemplo FERNADO VI --> FERNANDO VI
        # Añadiendo una S por ejemplo
        # Vuelta2: comprobar 1 solo error en total
        if ((diferenciastxt.count('+') + diferenciastxt.count('-')) <= 1
            and not (nombreCallej.__contains__("BARROS") and nombreDataset.__contains__("BARRIOS"))  #  BARRIOS  ::   BARROS
            and not (nombreCallej.__contains__("OLIVAR") and nombreDataset.__contains__("BOLIVAR"))  # Bolivar - Olivar
            and not (nombreCallej.__contains__("ESTE") and nombreDataset.__contains__("OESTE")) # OESTE::  ESTE
            and not (nombreCallej.__contains__("OESTE") and nombreDataset.__contains__("ESTE"))
            and not (nombreCallej.__contains__("VIAR") and nombreDataset.__contains__("VIA")) # VIA :: VIAR
            and not (nombreDataset.__contains__("VIA") and not (nombreCallej.__contains__("VIA")))
        ):
            print("Vuelta2: Posible Conicidencia: ", nombreDataset, " :: ", nombreCallej)
            return True
    # ------------------------------------------------------------------------------------------------------------------
    if (nVuelta == 3):
        # Vuelta3: comprobar 1 sustitucion (quitar 1 letra y añadir otra)
        if (diferenciastxt.count('+') <= 1 and diferenciastxt.count('-') <=1
            and not((diferenciastxt.count('+') + diferenciastxt.count('-')) <= 1)

            and not (nombreDataset.__contains__("HORTALEZA") and nombreCallej.__contains__("FORTALEZA")) #Hortaleza - Fortaleza
            and not (nombreCallej.__contains__("GALENA") and nombreDataset.__contains__("GILENA"))  # Gilena - Galena
            and not (nombreCallej.__contains__("PEAL") and nombreDataset.__contains__("REAL"))  # Real - Peal
            and not (nombreCallej.__contains__("HAYA") and nombreDataset.__contains__("RAYA"))  # RAYA  ::   HAYA
            and not (nombreCallej.__contains__("OCA") and nombreDataset.__contains__("OÑA"))  # OÑA  ::   OCA
            and not (nombreDataset.__contains__("CANDILEJAS") and nombreCallej.__contains__("CANALEJAS"))  # CANDILEJAS  ::   CANALEJAS
            and not (nombreDataset.__contains__("PASO") and nombreCallej.__contains__("MASO")) # PASO::  MASO
            and not (nombreCallej.__contains__("VID") and nombreDataset.__contains__("VIA"))  # VIA :: VID
            and not (nombreDataset.__contains__("VIA") and not (nombreCallej.__contains__("VIA")))
        ):
            print("Vuelta3: Posible Conicidencia: ", nombreDataset, " :: ", nombreCallej)
            return True
    # ------------------------------------------------------------------------------------------------------------------
    if(nVuelta == 4):
        # Si se han añadido o quitado 2 o menos letras, se puede considerar igual
        # Dependiendo de la longitud de la palabra acepta 1 error o más
        if (diferenciastxt.count('+') <= (longCadena1/10+1) and diferenciastxt.count('-') <=(longCadena1/10+1)
            and not(diferenciastxt.count('+') <= 1 and diferenciastxt.count('-') <=1)
            and not((diferenciastxt.count('+') + diferenciastxt.count('-')) <= 1)

            and not (nombreDataset.__contains__("HORTALEZA")) #Hortaleza - Fortaleza
            and not (nombreCallej.__contains__("GALENA"))  # Gilena - Galena
            and not (nombreCallej.__contains__("PEAL"))  # Real - Peal
            and not (nombreCallej.__contains__("OLIVAR"))  # Bolivar - Olivar
            and not (nombreCallej.__contains__("CRUCES") and nombreDataset.__contains__("RUICES"))  # RUICES  ::   CRUCES
            and not (nombreCallej.__contains__("HAYA"))  #  RAYA  ::   HAYA
            and not (nombreCallej.__contains__("OCA"))  #  OÑA  ::   OCA
            and not (nombreCallej.__contains__("MANZANAR") and nombreDataset.__contains__("MANZANARES"))  # MANZANARES  ::   MANZANAR
            and not (nombreDataset.__contains__("CANDILEJAS") and nombreCallej.__contains__("CANALEJAS") )  #  CANDILEJAS  ::   CANALEJAS
            and not (nombreCallej.__contains__("CENICIENTOS") and nombreDataset.__contains__("CENICIENTA"))  # CENICIENTA  ::   CENICIENTOS
            and not (nombreCallej.__contains__("CANTERAS") and nombreDataset.__contains__("MANOTERAS"))  # MANOTERAS  ::   CANTERAS
            and not (nombreDataset.__contains__("MANOTERAS") and nombreDataset.__contains__("SANTERAS"))  # MANOTERAS  ::   SANTERAS
            and not (nombreCallej.__contains__("GOR") and nombreDataset.__contains__("GADOR"))  # SIERRA GADOR  ::   SIERRA GOR
            and not (nombreDataset.__contains__("GADOR") and nombreDataset.__contains__("GUDAR"))  # SIERRA GADOR  ::   SIERRA GUDAR

            and not (nombreCallej.__contains__("ERASMO") and nombreDataset.__contains__("RASO"))  # SANZ RASO  ::   SAN ERASMO
            and not (nombreCallej.__contains__("ALIO") and nombreDataset.__contains__("AMON"))  # SANTIAGO AMON  ::   SANTIAGO ALIO
            and not (nombreDataset.__contains__("PARVILLAS") and nombreCallej.__contains__("MARAVILLA"))  # PARVILLAS  ::   MARAVILLA
            and not (nombreDataset.__contains__("MARMOLINA") and nombreCallej.__contains__("CAROLINA"))  # MARMOLINA  ::   CAROLINA
            and not (nombreCallej.__contains__("SAMANIEGO") and nombreDataset.replace(" ", "").__contains__("SANDIEGO"))  # SAN DIEGO  ::   SAMANIEGO
            and not (nombreDataset.replace(" ", "").__contains__("SANDIEGO")
                        and nombreCallej.replace(" ", "").__contains__("SANDACIO"))  # SAN DIEGO  ::   SAN DACIO
            and not (nombreDataset.replace(" ", "").__contains__("MONTEAYA") and nombreCallej.__contains__("MONTANA"))  # MONTE AYA  ::   MONTANA -
            and not (nombreCallej.__contains__("SANTERAS") and nombreDataset.__contains__("SANTERAS"))  # SANZ RASO  ::   SANTERAS -
            and not (nombreCallej.__contains__("ALCORISA") and nombreDataset.replace(" ", "").__contains__("PALOROSA"))  # PALO ROSA  ::   ALCORISA
            and not (nombreCallej.replace(" ", "").__contains__("CERROMONTE") and nombreDataset.__contains__("SACROMONTE"))  #  SACROMONTE  ::   CERRO MONTE -
            and not (nombreCallej.replace(" ", "").__contains__("EDUARDOUROSA")
                        and nombreDataset.replace(" ", "").__contains__("EDUARDOAUNOS"))  #  EDUARDO AUNOS  ::   EDUARDO UROSA -
            and not (nombreCallej.replace(" ", "").__contains__("MADREDIOS")
                        and nombreDataset.replace(" ", "").__contains__("MADRIDRIO"))  # MADRID RIO  ::   MADRE DIOS
            and not (nombreCallej.__contains__("FORTEA") and nombreDataset.replace(" ", "").__contains__("ZORITA"))  # COMANDANTE ZORITA  ::   COMANDANTE FORTEA
            and not (nombreCallej.__contains__("LIMON") and nombreDataset.__contains__("VIGON")) # JUAN VIGON  ::   JUAN LIMON
            and not (nombreCallej.__contains__("ACUARELA") and nombreDataset.__contains__("PASARELA")) # PASARELA   ::   ACUARELA
            and not (nombreCallej.__contains__("PASA") and nombreDataset.__contains__("PASO")) # PASO  ::  PASA
            and not (nombreCallej.__contains__("PASO") and nombreDataset.__contains__("PASA"))
            and not (nombreDataset.__contains__("VIA") and not(nombreCallej.__contains__("VIA")))
        ):

            print("------Vuelta4: Posible Conicidencia: ", nombreDataset, " :: ", nombreCallej)
            return True
        # --------------------------------------------------------------------------------------------------------------
    return False





def crearFichNombresId(nombreCarpeta = "", nombreSinCsv = "", nFileIni = "-1", nFileFin = "_IDs_000",
                       nRowPalabrasClave = "-1", nRowTipoVia="-1", tieneTipoCalle = False):
    with open(nombreCarpeta + "/" + nombreSinCsv + nFileIni + ".csv") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")
        file = open(nombreCarpeta + "/" + nombreSinCsv + nFileFin + ".csv", "w")
        primeraLinea = True
        nCorrect = 0
        nIncorrect = 0
        contadorFila = 0
        for row in csvreader:
            if (primeraLinea):
                fila = ";".join(row)
                fila = fila + ";" + "idVia"
                primeraLinea = False
            else:
                idVia = "-1"
                nombre = row[nRowPalabrasClave].upper()
                nVuelta = 1
                while (nVuelta <=8 ):
                    with open( RUTA_CALLEJERO ) as csvCallejero:
                        csvreaderCallej = csv.reader(csvCallejero, delimiter=";")
                        primeraLinea = True
                        encontrado = False
                        for rowCallj in csvreaderCallej:
                            if (primeraLinea):
                                primeraLinea = False
                            else:
                                try:
                                    if(
                                    not(rowCallj[1].upper().__contains__("AUTOVIA") or rowCallj[2].upper().__contains__("AUTOVÍA")
                                        or row[nRowTipoVia].upper() == "Autovia" or row[nRowTipoVia].upper() == "Autopista"
                                    )  # Si es autovia no debe comprobarlo porque no pueden circular bicicletas
                                    and (
                                        (not(tieneTipoCalle) or
                                        chequearPalabras(rowCallj[POS_TIPVIA_CALL].upper(), row[nRowTipoVia].upper(), -1))
                                        or
                                        (nVuelta > 4 and tieneTipoCalle
                                        and esTipoCalleOmitible(row[nRowTipoVia].upper())
                                        and not(chequearPalabras(rowCallj[POS_TIPVIA_CALL].upper(), row[nRowTipoVia].upper(), -1)))
                                    ) # En la 5a, 6a, 7a y 8a vuelta se comprobará sin tipo de via y de nuevo con las mismas comprobaciones
                                    and ((nVuelta<=4 and chequearPalabras(rowCallj[POS_PALCLAV_CALL].upper(), nombre.upper(), nVuelta))
                                        or(nVuelta>=5 and chequearPalabras(rowCallj[POS_PALCLAV_CALL].upper(), nombre.upper(), nVuelta-4)))
                                    ):
                                        idVia = rowCallj[POS_IS_CALL]
                                        encontrado=True
                                        nCorrect = nCorrect+1
                                        nVuelta = 99
                                        break
                                except IndexError:
                                    print("Error")
                                    # Posible error de que hay una linea vacia extra al final
                        if(not(encontrado) and nVuelta < 6):
                            nVuelta = nVuelta + 1
                            continue
                        if(not(encontrado) and nVuelta>=6):
                            nVuelta = 99
                            idVia = "-1"
                            nIncorrect = nIncorrect + 1
                    csvCallejero.close()
                fila = ";".join(row)
                fila = fila + ";" + idVia.__str__()
                contadorFila = contadorFila+1
                if(contadorFila % 10 == 0):
                    print("Fila: " , contadorFila)
            file.write(fila + os.linesep)
        file.close()
        print("Incorrectas: ", nIncorrect, " || Correctas: ", nCorrect)



def ejecutarAccidentesIDs():
    nombreCarpeta = "accidentesCSV"
    nombreSinCsv = "AccidentesBicicletas"
    nRowPalabrasClave = 16
    nRowTipoVia = 15
    print("Entrando en: crearFichNombresId")
    crearFichNombresId(nombreCarpeta, nombreSinCsv, "5", "_IDs_1",
                       nRowPalabrasClave, nRowTipoVia, True)
def ejecutarCicloCarrilesIDs():
    nombreCarpeta = "ciclocarrilesCSV"
    nombreSinCsv = "ciclocarriles"

    nRowPalabrasClave = 8
    nRowTipoVia = 7
    print("Entrando en: crearFichNombresId")
    crearFichNombresId(nombreCarpeta, nombreSinCsv, "5", "_IDs_1",
                       nRowPalabrasClave, nRowTipoVia, False)

def ejecutarCallesTranqIDs():
    nombreCarpeta = "callesTranquiCSV"
    nombreSinCsv = "callesTranquilas"

    nRowPalabrasClave = 12
    nRowTipoVia = 11
    print("Entrando en: crearFichNombresId")
    crearFichNombresId(nombreCarpeta, nombreSinCsv, "5", "_IDs_1",
                       nRowPalabrasClave, nRowTipoVia, True)
#---------------------------------------------------------------------------------------------------------



