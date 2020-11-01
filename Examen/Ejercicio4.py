if __name__ == '__main__':
	print("Ingrese el primer numero:")
	a = float(input())
	print("Ingrese el segundo numero:")
	b = float(input())
	print("Ingrese el signo")
	signo = input()
	if signo=="+":
		resultado = a+b
	else:
		if signo=="-":
			resultado = a-b
		else:
			if signo=="*":
				resultado = a*b
			else:
				if signo=="/":
					resultado = a/b
				else:
					if signo=="^":
						resultado = a**b
					else:
						resultado = 0
	print("El resultado es: ",resultado)

