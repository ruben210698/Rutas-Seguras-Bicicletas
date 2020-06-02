def chequearPalabras(nombreCallej = "", nombreDataset = "", nVuelta = 1):
    if(nombreDataset.replace(" ", "") == "" or nombreCallej.replace(" ", "") == ""):
        return False
    nombreDataset = nombreDataset.upper().replace("Á", "A").replace("É", "E").replace("Í", "I") \
        .replace("Ó", "O").replace("Ú", "U").replace("Ü", "U").replace(",", " ").replace("-", " ")
    nombreCallej = nombreCallej.upper().replace("Á", "A").replace("É", "E").replace("Í", "I") \
        .replace("Ó", "O").replace("Ú", "U").replace("Ü", "U").replace(",", " ").replace("-", " ")

    # Comprobaciones básicas
    # -------------------------------------------------------------------
    if(unicodedata.normalize('NFKD', nombreCallej.replace(" ", "")).encode('ASCII', 'ignore').strip().upper() \
       == unicodedata.normalize('NFKD',nombreDataset.replace(" ", "")).encode('ASCII', 'ignore').strip().upper()):
        return True
    elif(nVuelta ==1):
        return False #La primera vuelta solo hace estas comprobación
    # -------------------------------------------------------------------
    longCadena1 = nombreDataset.__len__()
    longCadena2 = nombreCallej.__len__()
    if (longCadena1 < (longCadena2 * 0.7) or longCadena1 > (longCadena2 * 1.3)):
        return False # Si el tamaño de la cadena difiere mucho
    diff = difflib.ndiff(nombreCallej.replace(" ", ""), nombreDataset.replace(" ", ""))
    diferenciastxt = ''.join(diff)
    # -------------------------------------------------------------------
    # -------------------------------------------------------------------
    # -------------------------------------------------------------------
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
    # -------------------------------------------------------------------
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
    # -------------------------------------------------------------------
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
        # ----------------------------------------------------------------
    return False

