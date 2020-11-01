if __name__ == '__main__':
	print("Ingrese Edad:")
	edad = input()
	print("Ingrese Sexo:")
	sexo = input()
	if edad>70:
		print("Vacuna Tipo C")
	else:
		if edad<16:
			print("Vacuna Tipo A")
		else:
			if edad>=16 and edad<=69 and sexo=="F":
				print("Vacuna Tipo B")
			else:
				if edad>=16 and edad<=69 and sexo=="M":
					print("Vacuna Tipo A")
				else:
					print("Valores incorrectos")

