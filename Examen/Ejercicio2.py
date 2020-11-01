if __name__ == '__main__':
	print("Ingrese Salario mínimo:")
	salario = float(input())
	print("Ingrese puntos:")
	puntos = input()
	if puntos<=50 and puntos<=100:
		bono = salario*0.1
	else:
		if puntos<=101 and puntos<=150:
			bono = salario*0.5
		else:
			if puntos>=151:
				bono = salario*0.8
	print("Bono:",bono)