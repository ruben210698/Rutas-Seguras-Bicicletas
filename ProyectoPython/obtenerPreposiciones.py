
import csv

import unicodedata
from re import findall


def getTipoVia(nombreViaIni = ""):
    nombreVia = nombreViaIni.upper()
    if(nombreVia.__contains__("CALL.") | nombreVia.__contains__("CALL") | nombreVia.__contains__("CALLE") ):
        return "Calle"
    elif (nombreVia.__contains__("PASEO.") | nombreVia.__contains__("PASEO") ):
        return "Paseo"
    elif (nombreVia.__contains__("PLAZA.") | nombreVia.__contains__("PLAZA") ):
        return "Plaza"
    elif (nombreVia.__contains__("GTA.") | nombreVia.__contains__("GTA") | nombreVia.__contains__("GLORIETA")):
        return "Glorieta"
    elif (nombreVia.__contains__("RONDA.") | nombreVia.__contains__("RONDA")):
        return "Ronda"
    elif (nombreVia.__contains__("CMNO.") | nombreVia.__contains__("CMNO") | nombreVia.__contains__("CAMINO")):
        return "Camino"
    elif (nombreVia.__contains__("PISTA.") | nombreVia.__contains__("PISTA")):
        return "Camino"
    elif (nombreVia.__contains__("ANILLO.") | nombreVia.__contains__("ANILLO")):
        return "Anillo"
    elif (nombreVia.__contains__("CRUCE.") | nombreVia.__contains__("CRUCE")):
        return "Cruce"
    elif (nombreVia.__contains__("AUTOV.") | nombreVia.__contains__("AUTOV")):
        return "Autovia"
    elif (nombreVia.__contains__("CTRA.") | nombreVia.__contains__("CTRA") | nombreVia.__contains__("CARRETERA")):
        return "Carretera"
    elif (nombreVia.__contains__("PQUE.") | nombreVia.__contains__("PQUE") | nombreVia.__contains__("PARQUE")):
        return "Parque"
    elif (nombreVia.__contains__("CUSTA.") | nombreVia.__contains__("CUSTA") | nombreVia.__contains__("CUESTA")):
        return "Cuesta"
    elif (nombreVia.__contains__("CÑADA.") | nombreVia.__contains__("CÑADA") | nombreVia.__contains__("CAÑADA")):
        return "Cañada"
    elif (nombreVia.__contains__("AVDA.") | nombreVia.__contains__("AVDA") | nombreVia.__contains__("AV") | nombreVia.__contains__("AVENIDA") ):
        return "Avenida"
    elif (nombreVia.__contains__("PASARELA") ):
        return "Pasarela"
    elif (nombreVia.__contains__("PASAJE") ):
        return "Pasaje"
    elif (nombreVia.__contains__("PUENTE") ):
        return "Puente"
    elif (nombreVia.__contains__("COSTANILLA") ):
        return "Costanilla"
    elif (nombreVia.__contains__("COLONIA") ):
        return "Colonia"
    elif (nombreVia.__contains__("CARRERA") ):
        return "Carrera"
    elif (nombreVia.__contains__("PASO ELEVADO")):
        return "Paso Elevado"
    elif (nombreVia.__contains__("PLAZUELA") ):
        return "Plazuela"
    elif (nombreVia.__contains__("BULEVAR") ):
        return "Bulevar"
    elif (nombreVia.__contains__("ESCALINATA") ):
        return "Escalinata"
    elif (nombreVia.__contains__("JARDÍN") | nombreVia.__contains__("JARDIN") | nombreVia.__contains__("JARDINES")):
        return "Jardin"
    elif (nombreVia.__contains__("PARTICULAR") ):
        return "Particular"
    elif (nombreVia.__contains__("POLÍGONO") | nombreVia.__contains__("POLIGONO")):
        return "Poligono"
    elif (nombreVia.__contains__("ACCESO") ):
        return "Acceso"
    elif (nombreVia.__contains__("POBLADO")):
        return "Poblado"
    elif (nombreVia.__contains__("PASADIZO")):
        return "Pasadizo"
    elif (nombreVia.__contains__("TRASERA")):
        return "Trasera"
    elif (nombreVia.__contains__("SENDA")):
        return "Senda"
    elif (nombreVia.__contains__("GALERÍA") | nombreVia.__contains__("GALERIA")):
        return "Galeria"
    elif (nombreVia.__contains__("ARROYO")):
        return "Arroyo"
    elif (nombreVia.__contains__("VALLE")):
        return "Valle"
    elif (nombreVia.__contains__("AEROPUERTO")):
        return "Aeropuerto"
    else:
        return nombreViaIni



with open("AccidentesBicicletas_2019.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=";")
    listaPrep = []
    listaPrep.__init__()
    for row in csvreader:
        posiblePrep = findall('\s[A-z]{1,4}\s', row[3])#.strip().lower()
        for prep in posiblePrep:
            if(not(listaPrep.__contains__(prep))):
                #print(prep)
                print(row[3])
                listaPrep.append(prep)
    print(listaPrep)
# Preposiciones y conjunciones posibles:
# callesTranquilas1 - row[7]: ' del ', ' de ', ' y ', ' las ', ' la ', ' los ', ' a ', ' por ', ' con '
# ciclocarriles1 - row[1]: ' de ', ' El ', ' y ', ' el ', ' la ', ' los ', ' a ', ' por ', ' con '
# callejeroMadrid1 - row[3]: ' A ', ' DE ', ' Y ', ' DEL ', ' EN ', ' LA ', ' O ', ' LAS ', ' I ', ' AL ', ' LOS ', ',', ' POR '
# callejeroMadrid1 - row[4]: ' A ', ' DE ', ' Y ', ' DEL ', ' EN ', ' LA ', ' O ', ' LAS ', ' I ', ' AL ', ' EL ', ' LOS ', ',', ' POR '
# accidentesBicicleta_2019 - row[3]: ' DE ', ' DEL ', ' EL ', ' A ', ' CON ', ' LA ', ' LOS ', ' LAS ', ' Y ', ' EN '

listFinal = []
listFinal.__init__()
list = [' del ', ' de ', ' y ', ' las ', ' la ', ' los ', ' a ', ' por ', ' con ',
        ' de ', ' El ', ' y ', ' el ', ' la ', ' los ', ' a ', ' por ', ' con ',
        ' A ', ' DE ', ' Y ', ' DEL ', ' EN ', ' LA ', ' O ', ' LAS ', ' I ', ' AL ', ' LOS ', ',', ' POR ',
        ' A ', ' DE ', ' Y ', ' DEL ', ' EN ', ' LA ', ' O ', ' LAS ', ' I ', ' AL ', ' EL ', ' LOS ', ',', ' POR ',
        ' DE ', ' DEL ', ' EL ', ' A ', ' CON ', ' LA ', ' LOS ', ' LAS ', ' Y ', ' EN ' ]
for elem in list:
    if(not(listFinal.__contains__(elem.upper()))):
        listFinal.append(elem.upper())
print(listFinal)
# ListFinal = [' DEL ', ' DE ', ' Y ', ' LAS ', ' LA ', ' LOS ', ' A ', ' POR ', ' CON ', ' EL ', ' EN ', ' O ', ' I ', ' AL ', ',']



# print(getTipoVia(row[3]))
# print(unicodedata.normalize('NFKD', row[7]).encode('ASCII', 'ignore').strip().lower())
# print("------" + row[7].strip().lower())
# print("------" + row[7])

# a = findall('Calle' + '\s', row[7])
#unicodedata.normalize('NFKD', string).encode('ASCII', 'ignore').strip().lower()