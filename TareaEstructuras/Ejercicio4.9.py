if __name__ == '__main__':
	total = 0
	print("Ingrese el valor de n:", end="")
	n = float(input())
	for i in range(1,n+1):
		print("PROCESO ",i)
		print("Ingrese el valor de cantidad 01 enero:", end="")
		cantidad_01_enero = float(input())
		print("Ingrese el valor de cantidad 02 febrero:", end="")
		cantidad_02_febrero = float(input())
		print("Ingrese el valor de cantidad 03 marzo:", end="")
		cantidad_03_marzo = float(input())
		print("Ingrese el valor de cantidad 04 abril:", end="")
		cantidad_04_abril = float(input())
		print("Ingrese el valor de cantidad 05 mayo:", end="")
		cantidad_05_mayo = float(input())
		print("Ingrese el valor de cantidad 06 junio:", end="")
		cantidad_06_junio = float(input())
		print("Ingrese el valor de cantidad 07 julio:", end="")
		cantidad_07_julio = float(input())
		print("Ingrese el valor de cantidad 08 agosto:", end="")
		cantidad_08_agosto = float(input())
		print("Ingrese el valor de cantidad 09 septiembre:", end="")
		cantidad_09_septiembre = float(input())
		print("Ingrese el valor de cantidad 10 octubre:", end="")
		cantidad_10_octubre = float(input())
		print("Ingrese el valor de cantidad 11 noviembre:", end="")
		cantidad_11_noviembre = float(input())
		print("Ingrese el valor de cantidad 12 diciembre:", end="")
		cantidad_12_diciembre = float(input())
		intereses = total*0.1
		total = total+intereses+cantidad_01_enero+cantidad_02_febrero+cantidad_03_marzo+cantidad_04_abril+cantidad_05_mayo+cantidad_06_junio+cantidad_07_julio+cantidad_08_agosto+cantidad_09_septiembre+cantidad_10_octubre+cantidad_11_noviembre+cantidad_12_diciembre
		inversion_final = total
		print("Valor de intereses: ",intereses)
		print("Valor de inversion final: ",inversion_final)
		print("")
	print("Valor de total: ",total)
