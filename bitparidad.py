def hasErrores(cadena, paridad):
    print(cadena)
    ## Primero Verificar es binarios
    binario = isBinario(cadena)
    #print(str(binario))

    if binario:
        ## Ver si es par o impar
        paridadVerdadera = getParidad(cadena)

        ## Ver si el ultimo bit es igual a lo que la variable de par o impar
        if(paridad == paridadVerdadera):
            print("La cadena es " + str(paridad) + " y no hay errores")
        else:
            print("La cadena es " + str(paridad) + " y hay un error con el bit de paridad")

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
        return "PAR"
    return "IMPAR"


if __name__== "__main__":
    hasErrores([1,0,0,0,1,0], "IMPAR")