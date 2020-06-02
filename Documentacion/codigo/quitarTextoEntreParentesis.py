def quitarTextoEntreParentesis(nombreVia = ""):
    if(nombreVia.__contains__("(") and nombreVia.__contains__(")")):
        posIni = nombreVia.index("(")
        posFin = nombreVia.index(")")
        txtElim = nombreVia[posIni:posFin+1]
        return nombreVia.replace(txtElim, "")
    if (nombreVia.__contains__("(")):
        posIni = nombreVia.index("(")
        txtElim = nombreVia[posIni:]
        return nombreVia.replace(txtElim, "")
    else:
        return nombreVia
