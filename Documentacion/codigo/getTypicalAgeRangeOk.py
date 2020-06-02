def getTypicalAgeRangeOk(txtOld = ""):
    if(txtOld.replace(" ", "") == ""):
        return ""
    if(txtOld.upper().__contains__("DESCONOCIDA")):
        return ""
    arrPal = txtOld.split()
    # "DE 30 A 34 AÑOS"
    try:
        fIni = arrPal[1]
        fFin = arrPal[3]
        if (fIni > fFin):
            fIni, fFin = fFin, fIni
        txtFin = fIni + "-" + fFin
    except IndexError:
        txtFin = ""
        print("Distinto formato Rango Edad: ", txtOld)
    # En caso de que no siga el formato estandar
    if(findall('([0-9]{1})-([0-9]{1})', txtFin) == []):
        fIni = -1
        fFin = -1
        i = 1
        for elem in arrPal:
            if(fIni == fFin and findall('([0-9]{1})', elem) != []):
                if (fIni == -1):
                    fIni = elem
                fFin = elem
        if(fIni != fFin):
            if(fIni > fFin):
                fIni, fFin = fFin, fIni
            return fIni + "-" + fFin
        else:
            return ""
    return txtFin

