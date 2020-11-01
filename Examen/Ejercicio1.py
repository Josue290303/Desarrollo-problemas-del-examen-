if __name__ == '__main__':
	print("Ingrese nota 1ra Unidad:")
	nota1 = float(input())
	print("Ingrese nota 2da Unidad")
	nota2 = float(input())
	print("Ingrese nota 3ra Unidad")
	nota3 = float(input())
	print("Ingrese nota Trabajo Final")
	trabajofinal = float(input())
	notafinal = 0.1*nota1+0.15*nota2+0.25*nota3+0.5*trabajofinal
	print("Nota Final:",notafinal)

