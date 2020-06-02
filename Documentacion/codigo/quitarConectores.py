def quitarConectores(nombreVia = ""):
    nombreVia = nombreVia.upper()
    listaPosibles = ['DEL', 'DE', 'Y', 'LAS', 'LA', 'LOS', 'A', 'POR', 'CON',
                     'EL', 'EN', 'O', 'I', 'AL', ',', '-', 'S/N', 'JUNTO', '_', 'SOBRE',
                     'ENTRE', 'FRENTE']
    for a in listaPosibles:
        if(nombreVia.__contains__(a)):
            if(nombreVia.__contains__(' ' + a + ' ')):
                nombreVia = nombreVia.replace(' ' + a + ' ', " ")
            elif( # Para evitar que pertenezca a una palabra
            (findall('([A-z, 0-9, \s, À-ÿ]{1})' + a, nombreVia) == [] or findall('([A-z, 0-9, \s, À-ÿ]{1})' + a, nombreVia) == [' '])
            and (findall(a + '([A-z, 0-9,\s, À-ÿ]{1})', nombreVia) == [] or findall(a + '([A-z, 0-9,\s, À-ÿ]){1}', nombreVia) == [' '] )):
                nombreVia = nombreVia.replace(a, " ")
    return nombreVia
