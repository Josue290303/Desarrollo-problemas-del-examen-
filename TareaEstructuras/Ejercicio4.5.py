if __name__ == '__main__':
	ahorro_anual = 0
	for i in range(1,366):
		print("PROCESO ",i)
		ahorro_anual = ahorro_anual+0.01*(3)**(i)
		ahorro_diario = ahorro_anual
		print("Valor de ahorro diario: ",ahorro_diario)
		print("")
	print("Valor de ahorro anual: ",ahorro_anual)
