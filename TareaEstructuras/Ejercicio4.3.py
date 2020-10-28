if __name__ == '__main__':
	cantidades_cero = 0
	menores_a_cero = 0
	mayores_a_cero = 0
	print("Ingrese el valor de n:", end="")
	n = float(input())
	for i in range(1,n+1):
		print("PROCESO ",i)
		print("Ingrese el valor de cantidad:", end="")
		cantidad = input()
		if cantidad==0:
			cantidades_cero = cantidades_cero+1
		if cantidad<0:
			menores_a_cero = menores_a_cero+1
		if cantidad>0:
			mayores_a_cero = mayores_a_cero+1
		print("")
	print("Valor de cantidades cero: ",cantidades_cero)
	print("Valor de menores a cero: ",menores_a_cero)
	print("Valor de mayores a cero: ",mayores_a_cero)

