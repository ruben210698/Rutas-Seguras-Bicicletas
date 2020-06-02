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
