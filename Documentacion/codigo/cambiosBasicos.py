
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

