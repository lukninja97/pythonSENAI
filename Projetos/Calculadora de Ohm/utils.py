def solicita_tensao():
    while True:
        try:
            tensao = float(input("Digite a tensão em volts: "))
            if tensao > 0:
                return tensao
        except ValueError:
            print("Valor inválido, Digite um número utilizando o ponto como separador. Ex: 1.0")