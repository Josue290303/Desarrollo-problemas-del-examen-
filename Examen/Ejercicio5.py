
def incrementoAlSalarioDeUnProfesor():
    for i in range(1,7):
        print("PROCESO ",i)
        salario_inicial = 1400
        ano = i
        salario_recibido = salario_inicial*(1.1)**(ano)
        print("Valor de salario inicial: ",salario_inicial)
        print("Valor de salario recibido: ",salario_recibido)
        print("Valor de año: ",ano)
        print("")
incrementoAlSalarioDeUnProfesor()