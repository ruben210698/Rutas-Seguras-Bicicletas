import csv
import os
import difflib
import unicodedata

def crearFichNombresId(nombreCarpeta = "", nombreSinCsv = "", nFileIni = "-1", nFileFin = "_IDs_000",
                   nRowEsCruce = -1, nRowPalabrasClave = "-1", nRowTipoVia="-1", tieneTipoCalle = False):
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
            fila = fila + ";" + "ID_CALLE"
            primeraLinea = False
        else:
            arrCalles = []
            if (nRowEsCruce != -1 and row[nRowEsCruce] == "1"):  # Si es cruce tendra varios ids
                arrCallesCruce = getArrCalles(row[nRowPalabrasClave].upper())
            else:
                arrCallesCruce = [row[nRowPalabrasClave].upper()]

            listIds = []
            nElem = 0
            for nombre in arrCallesCruce:
                #TODO: quitar
                '''if(not(nombre.__contains__("EUGENIA"))):
                    continue'''
                #TODO: quitar
                segundaVuelta = False
                nVuelta = 0
                while (nVuelta == 0 or segundaVuelta):
                    nVuelta = nVuelta + 1
                    with open("callejeroCSV" + "/" + "nombres_IDs" + ".csv") as csvCallejero:
                        csvreaderCallej = csv.reader(csvCallejero, delimiter=";")
                        primeraLinea = True
                        encontrado = False
                        for rowCallj in csvreaderCallej:
                            if (primeraLinea):
                                primeraLinea = False
                            else:
                                try:
                                    # TODO: quitar
                                    '''if (rowCallj[11].__contains__("EUGENIA")):
                                        print("OK2")'''
                                    # TODO: quitar
                                    if((nElem >0 or not(tieneTipoCalle) or
                                    (segundaVuelta and esTipoCalleOmitible(row[nRowTipoVia].upper()))
                                    or checkearPalabras(rowCallj[1].upper(), row[nRowTipoVia].upper(),False)) and
                                    #Porque si es la segunda entrada no contiene el tipo de via
                                    checkearPalabras(rowCallj[11].upper(), nombre.upper(), segundaVuelta)):
                                        listIds.append(rowCallj[0])
                                        encontrado=True
                                        nCorrect = nCorrect+1
                                        segundaVuelta=False
                                        break
                                except IndexError:
                                    print("Error")
                                    # Posible error de que haya una linea vacia extra al final
                        if (not(encontrado) and not(segundaVuelta)):
                            segundaVuelta = True
                            continue
                        if(not(encontrado) and segundaVuelta):
                            segundaVuelta = False
                            listIds.append("-1")
                            nIncorrect = nIncorrect + 1
                    csvCallejero.close()
                    nElem = nElem + 1
            fila = ";".join(row)
            fila = fila + ";" + listIds.__str__()
            contadorFila = contadorFila+1
            if(contadorFila % 20 == 0):
                print("Fila: " , contadorFila)
        file.write(fila + os.linesep)
    file.close()
    print("Incorrectas: ", nIncorrect, " || Correctas: ", nCorrect)
