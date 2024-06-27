from utils import solicita_tensao

def solicita_corrente():
    while True:
        corrente = float(input("Digite a corrente em amperes: "))
        if corrente > 0:
            return corrente


print("Calculadora de Ohm")
print("")
print("0 - Sair")
print("1 - Resistência")
print("2 - Tensão")
print("3 - Corrente")
print("4 - Resistência necessária para um resistor")
print("")

opcao = int(input("Digite o número da escolha desejada: "))

while opcao != 0:

    if opcao == 1:
        print("Resistencia")
        print("")

        tensao = solicita_tensao()

        corrente = solicita_corrente()

        resistencia = tensao / corrente

        print(f"A resistência é de {resistencia} Ω")

    elif opcao == 2:
        print("Tensão")
        print("")

        resistencia = float(input("Digite a resistência em ohms: "))
        corrente = float(input("Digite a corrente em amperes: "))

        tensao = resistencia * corrente

        print(f"A tensão é de {tensao} volts")

    elif opcao == 3:
        print("Corrente")
        print("")

        tensao = float(input("Digite a tensão em volts: "))
        resistencia = float(input("Digite a resistência em ohms: "))

        corrente = tensao / resistencia

        print(f"A corrente é de {corrente} amperes")

    elif opcao == 4:
        print("Ressistencia resistor")
        print("")
        tensao_fonte = float(input("Digite a tensão da fonte em volts: "))
        tensao_dispositivo = float(input("Digite a tensão do dispositivo em volts: "))
        corrente = float(input("Digite a corrente em amperes: "))

        resistencia_resistor = (tensao_fonte - tensao_dispositivo) / corrente

        print(f"A resistencia necessária desse resistor é de {resistencia_resistor} Ω")
    else:
        print("Opção inválida")

    print("")
    print("Escolha outra opção")
    print("0 - Sair")
    print("1 - Resistência")
    print("2 - Tensão")
    print("3 - Corrente")
    print("4 - Resistência necessária para um resistor")
    print("")

    opcao = int(input("Digite o número da escolha desejada: "))
