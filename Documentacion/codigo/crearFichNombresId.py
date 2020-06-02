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
                                #------------ Bloque desplazado para mejor comprensión -------
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
                            #------------------------------------------------------
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

