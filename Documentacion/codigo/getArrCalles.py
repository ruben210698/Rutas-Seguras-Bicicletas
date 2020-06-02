def getArrCallesRec(nombreDataset = ""):
    listaNombres = []
    if (nombreDataset.__contains__('/')):
        n1 = nombreDataset.split().index('/')
        txtRestante = " ".join(nombreDataset.split()[n1 + 1:])
        nombre = " ".join(nombreDataset.split()[0:n1])
        elemRecursiv = getArrCallesRec(txtRestante)
        listaNombres = [nombre, elemRecursiv]
    else:
        listaNombres = [nombreDataset]

    return listaNombres

def getArrCalles(nombreDataset = ""):
    list1 = getArrCallesRec(nombreDataset)
    txt = list1.__str__().replace('[', '').replace(']', '')
    list3 = []
    nombre=""

    for elem in txt.split():
        if(elem.__contains__("'") and nombre != ""):
            nombre = nombre + " " + elem.replace("'", "").replace(",", "")
            list3.append(nombre)
            nombre = ""
        elif (elem.__contains__("'") and nombre == "" and elem.replace("'", "", 1).__contains__("'")):
            nombre = elem.replace("'", "").replace(",", "")
            list3.append(nombre)
            nombre = ""
        elif (elem.__contains__("'") and nombre == ""):
            nombre = elem.replace("'", "").replace(",", "")
        else:
            nombre = nombre + " " + elem
    return list3


