if __name__ == '__main__':
	print("Ingrese el valor de sueldo base:", end="")
	sueldo_base = float(input())
	ley_de_politica_habitacional = sueldo_base*0.01
	seguro_social = sueldo_base*0.04
	seguro_de_desempleo = sueldo_base*0.005
	caja_de_ahorro = sueldo_base*0.05
	monto_total_a_pagar = sueldo_base-ley_de_politica_habitacional-seguro_social-seguro_de_desempleo-caja_de_ahorro
	print("Valor de caja de ahorro: ",caja_de_ahorro)
	print("Valor de ley de politica habitacional: ",ley_de_politica_habitacional)
	print("Valor de monto total a pagar: ",monto_total_a_pagar)
	print("Valor de seguro de desempleo: ",seguro_de_desempleo)
	print("Valor de seguro social: ",seguro_social)
    