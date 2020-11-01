if __name__ == '__main__':
	anos = 6
	salario_inicial = 1400
	porcentajeincremento = 1.1
	for i in range(1,anos+1):
		print("PROCESO ",i)
		ano = i
		salario_recibido = salario_inicial*(porcentajeincremento)**(ano)
		print("Valor de salario inicial: ",salario_inicial)
		print("Valor de salario recibido: ",salario_recibido)
		print("Valor de año: ",ano)
		print("")
		if i==6:
			salario_final = salario_recibido
	print("Salario Final:",salario_final)

