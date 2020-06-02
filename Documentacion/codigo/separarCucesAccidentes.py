
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

