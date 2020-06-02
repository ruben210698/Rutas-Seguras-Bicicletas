def quitarPalabrasConflicto(nombreVia = ""):
    nombreVia = nombreVia.upper()
    if(nombreVia == ""):
        return ""
    if(nombreVia.__contains__("\"")):
        nombreVia = nombreVia.replace("\"", "")
    nombreVia = quitarTextoEntreParentesis(nombreVia)

    listaPalabrasQuitar = ["CRUCE", "CALLE", "PASEO", "PLAZA", "GLORIETA", "CAMINO", "PISTA",
                           "AUTOVIA", "CARRETERA", "CUESTA", "AVENIDA", "VIA", "PASARELA",
                           "PASAJE", "COSTANILLA", "COLONIA", "POLIGONO", "CARRERA", "PLAZUELA", "BULEVAR",
                           "ESCALINATA", "JARDIN", "PARTICULAR",  "ACCESO", "POBLADO",
                           "PASADIZO", "TRASERA", "SENDA", "GALERIA", "VALLE",
                           "PASO_ELEVADO", "SENDA_CICLABLE", "ANILLO", "TRAVESIA", "ESTACION_FERROCARRIL",
                           "CAÑADA", "AUTOPISTA", "RONDA", "AEROPUERTO", "PUENTE", "CALLEJON",
                           "COLPB.", "INS.", "IDB."]

    for a in listaPalabrasQuitar:

        if(nombreVia.__contains__(a)):
            existePalQuit = False
            if (nombreVia.__contains__(' ' + a + ' ')):
                existePalQuit = True
                arr = nombreVia.split()

            elif (  # Para evitar que pertenezca a una palabra
            (findall('([A-z, 0-9, \s, À-ÿ]{1})' + a, nombreVia) == [] or findall('([A-z, 0-9, \s, À-ÿ]{1})' + a, nombreVia) == [' '])
            and (findall(a + '([A-z, 0-9,\s, À-ÿ]{1})', nombreVia) ==[] or findall(a + '([A-z, 0-9,\s, À-ÿ]){1}', nombreVia) ==[' '] )):
                #Para evitar errores por ejemplo en SegoVIA
                #Para evitar errores por ejemplo en PUENTECESURES
                arr = nombreVia.split()
                existePalQuit = True


            if (existePalQuit and arr.index(a) == 0): # Para evitar suprimir Gran VIA p.ej. (que este al inicio) ó FRANCISCO JOSÉ ARROYO
                nombreVia = nombreVia.replace(a, ' ')
            if (existePalQuit and nombreVia.__contains__('/') and findall('[A-z, À-ÿ]{1}' + '/', nombreVia) == []):
                if (arr.index(a) == arr.index('/') + 1):  # Para cuando es un cruce
                    nombreVia = nombreVia.replace(a + ' ', ' ')


        # Podria ser M11 por ejemplo
    if(nombreVia.replace(" ", "") != "" and nombreVia.strip()[0] == '/'):
        # Para eliminar descripciones al inicio y su / p.ej. SENDA_CICLABLE / AV.ROSALES / CARRET.VILLAV. A VALLECA
        nombreVia = nombreVia.replace('/', '', 1)
    return nombreVia

