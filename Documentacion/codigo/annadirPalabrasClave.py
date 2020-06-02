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
