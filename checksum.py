''' https://es.wikipedia.org/wiki/Suma_de_verificaci%C3%B3n '''

def checksum(cadena1, cadena2, cadena3):
    # suma de arrays
    cadenaSumada = sumar(cadena1, cadena2, cadena3)
    print(bin(cadenaSumada))
    # complemento de cadenaSumada
    cadenaComplemento = complemento(cadenaSumada)
    print(bin(cadenaComplemento))

    status = chequeo(cadena1, cadena2, cadena3, cadenaComplemento)

    if status:
        print("CheckSum: " + bin(cadena1) + " - " + bin(cadena2) + " - " + bin(cadena3) + " - " + bin(cadenaComplemento) + " = " + bin(cadena1+cadena2+cadena3+cadenaComplemento))


def sumar(cadena1, cadena2, cadena3):
    return (cadena1 + cadena2 + cadena3)


def complemento(cadenaSumada):
    #No Funciona
    return -((cadenaSumada) - int('1111111111111111',2))


def chequeo(cadena1, cadena2, cadena3, cadenaComplemento):
    
    return True

if __name__== "__main__":
    A = int('0110011001100110',2)
    B = int('0101010101010101',2)
    C = int('0000111100001111',2)
    D = int('0011010100110101',2)
    print(bin(A+B+C+D))
    checksum(A, B, C)