if __name__ == '__main__':
	focos_verdes = 0
	focos_blancos = 0
	focos_rojos = 0
	print("Ingrese el valor de n:", end="")
	n = float(input())
	for i in range(1,n+1):
		print("PROCESO ",i)
		print("Seleccione el valor de color.")
		print("    1.- verde")
		print("    2.- blanco")
		print("    3.- rojo")
		print("    :", end="")
		while True:# no hay 'repetir' en python
			color = input()
			if color<1 or color>3:
				print("Valor incorrecto. Ingréselo nuevamente.: ", end="")
			if color>=1 and color<=3: break
		if color==1:
			focos_verdes = focos_verdes+1
		if color==2:
			focos_blancos = focos_blancos+1
		if color==3:
			focos_rojos = focos_rojos+1
		print("")
	print("Valor de focos verdes: ",focos_verdes)
	print("Valor de focos blancos: ",focos_blancos)
	print("Valor de focos rojos: ",focos_rojos)