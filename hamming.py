''' VERIFICA SOLO CADENAS DE 7 BITS '''
''' https://es.wikipedia.org/wiki/C%C3%B3digo_Hamming '''
def hamming(cadena):
    print(cadena)
    ## Primero Verificar es binarios y si tiene  7 bits 
    binario = isBinario(cadena)

    if binario:
        ## Obtener los 4 bits de paridad
        copyCadena = cadena.copy()
        copyCadena.pop(2)
        copyCadena.pop(4)
        print(copyCadena)
        p1 = getParidad(copyCadena)
        
        copyCadena = cadena.copy()
        copyCadena.pop(4)
        copyCadena.pop(1)
        print(copyCadena)
        p2 = getParidad(copyCadena)

        copyCadena = cadena.copy()
        copyCadena.pop(6)
        copyCadena.pop(5)
        copyCadena.pop(4)
        copyCadena.pop(0)
        print(copyCadena)
        p3 = getParidad(copyCadena)

        copyCadena = cadena.copy()
        copyCadena.pop(3)
        copyCadena.pop(2)
        copyCadena.pop(1)
        copyCadena.pop(0)
        print(copyCadena)
        p4 = getParidad(copyCadena)

        ## Agregar bits de paridad en la cadena
        cadenaHamming = juntarCadena(cadena, p1, p2, p3, p4)
        print(cadenaHamming)
 
def isBinario(cadena):
    binario = False
    i = 0
    for i in range (len(cadena)):

        if(cadena[i] == 1 or cadena[i] == 0):
            #print("Es binario")
            binario = True
        else:
            #print("No es binario")
            return False
        i = i+1
    return binario

def getParidad(cadena):
    unos = 0
    i = 0
    for i in range (len(cadena)):
        if(i < len(cadena)):
            if(cadena[i] == 1):
                unos = unos + 1
    if(unos % 2 == 0):
        return 0
    return 1

def juntarCadena(cadena, p1, p2, p3, p4):
    cadenaFinal = [p1, p2, cadena[0], p3, cadena[1], cadena[2], cadena[3], p4, cadena[4], cadena[5], cadena[6]]
    return cadenaFinal

if __name__== "__main__":
    hamming([0,1,1,0,1,0,1])