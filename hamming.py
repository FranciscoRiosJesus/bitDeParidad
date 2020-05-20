
cadena = 1100101

def autocompletar(cadena):
  ''' Buscamos las posiciones de los datos de paridad '''
	# convertimos la cadena en lista
	cadena = list(cadena)

	x = posicion = 0	
	while posicion < len(cadena):
		posicion = 2 ** x
		# insertamos el valor de paridad
		if posicion < len(cadena):
			cadena.insert(posicion-1, "*")
		else:
			break
		x += 1

	cadena = "".join(cadena)
	return cadena