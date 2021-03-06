
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

