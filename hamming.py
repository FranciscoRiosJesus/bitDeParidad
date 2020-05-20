''' VERIFICA SOLO CADENAS DE 7 BITS '''
def hamming(cadena):
    print(cadena)
    ## Primero Verificar es binarios y si tiene  7 bits 
    binario = isBinario(cadena)

    if binario:
        ## Obtener los 4 bits de paridad
		copyCadena = cadena.copy()
		copyCadena.pop(2)
		copyCadena.pop(5)
		print(copyCadena)
		p1 = getParidad(copyCadena)
        
		## Agregar bit de paridad en la cadena
 
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
    hamming([1,0,0,0,1,0,1])