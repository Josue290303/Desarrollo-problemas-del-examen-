if __name__ == '__main__':
	pago_por_todo = 0
	print("Ingrese el valor de n:", end="")
	n = float(input())
	for i in range(1,n+1):
		print("PROCESO ",i)
		print("Ingrese el valor de precio:", end="")
		precio = float(input())
		descuento = precio*0.1
		if precio>=200:
			descuento = precio*0.15
		if precio>100 and precio<200:
			descuento = precio*0.12
		costo = precio-descuento
		pago_por_todo = pago_por_todo+costo
		print("Valor de costo: ",costo)
		print("Valor de descuento: ",descuento)
		print("")
	print("Valor de pago por todo: ",pago_por_todo)