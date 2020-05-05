import csv
import os
import difflib
import unicodedata
def checkearPalabras(nombreCallej = "", nombreDataset = "", segundaVuelta = False):
    # En la segunda vuelta también se omite el tipo de calle
    nombreDataset1 = nombreDataset.upper().replace("Á", "A").replace("É", "E").replace("Í", "I") \
        .replace("Ó", "O").replace("Ú", "U").replace("Ü", "U").replace(" ", "")
    nombreCallej1 = nombreCallej.upper().replace("Á", "A").replace("É", "E").replace("Í", "I") \
        .replace("Ó", "O").replace("Ú", "U").replace("Ü", "U").replace(" ", "")
    if(nombreDataset1 == nombreCallej1):    # Para aumentar la velocidad al ser cambios menores
        return True
    if(unicodedata.normalize('NFKD', nombreCallej).encode('ASCII', 'ignore').strip().upper() \
       == unicodedata.normalize('NFKD',nombreDataset).encode('ASCII', 'ignore').strip().upper()):
        return True
    # ------------------------------------------------------------------------------------------------------------------

    if(segundaVuelta):   # Excepciones cuando hay pequeños cambios que pueden deberse a errores ortograficos
        nombreDataset = nombreDataset.upper().replace("Á", "A").replace("É", "E").replace("Í", "I") \
            .replace("Ó", "O").replace("Ú", "U").replace("Ü", "U")
        nombreCallej = nombreCallej.upper().replace("Á", "A").replace("É", "E").replace("Í", "I") \
            .replace("Ó", "O").replace("Ú", "U").replace("Ü", "U")
        # ------------------------------------------------------------------------------------
        # P.ej. COMANDANTE ZORITA
        nombreDataset1 = nombreDataset
        nombreCallej1 = nombreCallej
        if(nombreDataset.__contains__("COMANDANTE")):
            nombreDataset1 = nombreDataset.replace("COMANDANTE", "AVIADOR")
        if (nombreCallej.__contains__("COMANDANTE")):
            nombreCallej1 = nombreCallej.replace("COMANDANTE", "AVIADOR")
        if(nombreCallej1.__contains__("AVIADOR") and
            (unicodedata.normalize('NFKD', nombreCallej1).encode('ASCII', 'ignore').strip().upper() \
           == unicodedata.normalize('NFKD',nombreDataset1).encode('ASCII', 'ignore').strip().upper())):
            return True
        # ------------------------------------------------------------------------------------
        if(nombreCallej.replace(" ", "").__contains__("M30") or
            nombreCallej.replace(" ", "").__contains__("M40")):
            return False #Si no la ha detectado ya es que hay problemas y las Bicicletas no pueden circular por ahi
        # ------------------------------------------------------------------------------------
        # Por ejemplo FERNADO VI --> FERNANDO VI
        longCadena1 = nombreDataset.__len__()
        longCadena2 = nombreCallej.__len__()
        if(longCadena1 < (longCadena2*0.7) or longCadena1 > (longCadena2 * 1.3)) :
            # Si el tamaño de la cadena difiere mucho
            return False
        diff = difflib.ndiff(nombreCallej1.replace(" ", ""), nombreDataset1.replace(" ", ""))
        diferenciastxt = ''.join(diff)
        # ------------------------------------------------------------------------------------
        #Primero comprobar 1 solo error en total
        if ((diferenciastxt.count('+') + diferenciastxt.count('-')) <= 1
            and not (nombreCallej.__contains__("BARROS"))  #  BARRIOS  ::   BARROS
            and not (nombreCallej.__contains__("OLIVAR"))  # Bolivar - Olivar
            and not (nombreCallej.__contains__("MANZANAR"))  # MANZANARES  ::   MANZANAR
            ):
            # Añadiendo una S por ejemplo
            print("Posible Conicidencia Simple: ", nombreDataset, " :: ", nombreCallej)
            return True
        # ------------------------------------------------------------------------------------
        # Segundo comprobar 1 sustitucion
        if (diferenciastxt.count('+') <= 1 and diferenciastxt.count('-') <=1
            and not(nombreDataset.__contains__("HORTALEZA")) #Hortaleza - Fortaleza
            and not (nombreCallej.__contains__("GALENA"))  # Gilena - Galena
            and not (nombreCallej.__contains__("PEAL"))  # Real - Peal
            and not (nombreCallej.__contains__("OLIVAR"))  # Bolivar - Olivar
            and not (nombreCallej.__contains__("CRUCES"))  # RUICES  ::   CRUCES
            and not (nombreCallej.__contains__("HAYA"))  # RAYA  ::   HAYA
            and not (nombreCallej.__contains__("OCA"))  # OÑA  ::   OCA
            and not (nombreCallej.__contains__("MANZANAR"))  # MANZANARES  ::   MANZANAR
            and not (nombreDataset.__contains__("CANDILEJAS") and nombreCallej.__contains__("CANALEJAS"))  # CANDILEJAS  ::   CANALEJAS
            and not (nombreCallej.__contains__("LIMON"))  # JUAN VIGON  ::   JUAN LIMON
            and not (nombreCallej.__contains__("CENICIENTOS"))  # CENICIENTA  ::   CENICIENTOS
            and not (nombreCallej.__contains__("CANTERAS"))  # MANOTERAS  ::   CANTERAS
            and not (nombreDataset.__contains__("MANOTERAS"))  # MANOTERAS  ::   SANTERAS
            and not (nombreCallej.__contains__("GOR"))  # SIERRA GADOR  ::   SIERRA GOR
            and not (nombreDataset.__contains__("GADOR"))  # SIERRA GADOR  ::   SIERRA GUDAR
            and not (nombreCallej.__contains__("ERASMO"))  # SANZ RASO  ::   SAN ERASMO
            and not (nombreCallej.__contains__("ALIO"))  # SANTIAGO AMON  ::   SANTIAGO ALIO
            and not (nombreDataset.__contains__("PARVILLAS"))  # PARVILLAS  ::   MARAVILLA
            and not (nombreDataset.__contains__("MARMOLINA"))  # MARMOLINA  ::   CAROLINA
            and not (nombreCallej.__contains__("SAMANIEGO"))  # SAN DIEGO  ::   SAMANIEGO
            and not (nombreDataset.replace(" ", "").__contains__("SANDIEGO"))  # SAN DIEGO  ::   SAN DACIO
            and not (nombreCallej.__contains__("BARROS"))  # BARRIOS  ::   BARROS
            and not (nombreDataset.replace(" ", "").__contains__("MADRIDRIO"))  #  MADRID RIO  ::   MADRE DIOS
            ):
            print("Posible Conicidencia Sustitucion: ", nombreDataset, " :: ", nombreCallej)
            return True
        # ------------------------------------------------------------------------------------
        # Dependiendo de la longitud de la palabra acepta 1 error o más
        if (diferenciastxt.count('+') <= (longCadena1/10+1) and diferenciastxt.count('-') <=(longCadena1/10+1)
            and not (nombreDataset.__contains__("HORTALEZA")) #Hortaleza - Fortaleza
            and not (nombreCallej.__contains__("GALENA"))  # Gilena - Galena
            and not (nombreCallej.__contains__("PEAL"))  # Real - Peal
            and not (nombreCallej.__contains__("OLIVAR"))  # Bolivar - Olivar
            and not (nombreCallej.__contains__("CRUCES"))  # RUICES  ::   CRUCES
            and not (nombreCallej.__contains__("HAYA"))  #  RAYA  ::   HAYA
            and not (nombreCallej.__contains__("OCA"))  #  OÑA  ::   OCA
            and not (nombreCallej.__contains__("MANZANAR"))  #  MANZANARES  ::   MANZANAR
            and not (nombreDataset.__contains__("CANDILEJAS") and nombreCallej.__contains__("CANALEJAS") )  #  CANDILEJAS  ::   CANALEJAS
            and not (nombreCallej.__contains__("LIMON"))  # JUAN VIGON  ::   JUAN LIMON
            and not (nombreCallej.__contains__("CENICIENTOS"))  # CENICIENTA  ::   CENICIENTOS
            and not (nombreCallej.__contains__("CANTERAS"))  #  MANOTERAS  ::   CANTERAS
            and not (nombreDataset.__contains__("MANOTERAS"))  # MANOTERAS  ::   SANTERAS
            and not (nombreCallej.__contains__("GOR"))  # SIERRA GADOR  ::   SIERRA GOR
            and not (nombreDataset.__contains__("GADOR"))  # SIERRA GADOR  ::   SIERRA GUDAR
            and not (nombreCallej.__contains__("ERASMO"))  #  SANZ RASO  ::   SAN ERASMO
            and not (nombreCallej.__contains__("ALIO"))  #  SANTIAGO AMON  ::   SANTIAGO ALIO
            and not (nombreDataset.__contains__("PARVILLAS"))  # PARVILLAS  ::   MARAVILLA
            and not (nombreDataset.__contains__("MARMOLINA"))  # MARMOLINA  ::   CAROLINA
            and not (nombreCallej.__contains__("SAMANIEGO"))  # SAN DIEGO  ::   SAMANIEGO
            and not (nombreDataset.replace(" ", "").__contains__("SANDIEGO"))  # SAN DIEGO  ::   SAN DACIO
            and not (nombreCallej.__contains__("BARROS"))  #  BARRIOS  ::   BARROS -
            and not (nombreDataset.replace(" ", "").__contains__("MONTEAYA"))  # MONTE AYA  ::   MONTANA -
            and not (nombreCallej.__contains__("SANTERAS"))  # SANZ RASO  ::   SANTERAS -
            and not (nombreDataset.replace(" ", "").__contains__("PALOROSA"))  # PALO ROSA  ::   ALCORISA
            and not (nombreDataset.__contains__("SACROMONTE"))  #  SACROMONTE  ::   CERRO MONTE -
            and not (nombreDataset.replace(" ", "").__contains__("EDUARDOAUNOS"))  #  EDUARDO AUNOS  ::   EDUARDO UROSA -
            and not (nombreDataset.replace(" ", "").__contains__("MADRIDRIO"))  # MADRID RIO  ::   MADRE DIOS
            ):
            # Si se han añadido o quitado 2 o menos letras, se puede considerar igual
            print("-------Posible Conicidencia: ", nombreDataset, " :: ", nombreCallej)
            return True
        # ------------------------------------------------------------------------------------
    return False
