while True:
    try:
        #
        idade = int(input("Digite sua idade: "))
        if idade < 0 or idade > 100:
            print("Idade invalida")
        else:
            print("Idade:", idade)
            # sai do while de verificação
            break
    except ValueError:
        #caso der erro executa aqui
        print("Digite sua idade em numero. Ex: 26")

while True:
    try:
        idade = int(input("Digite sua idade: "))
        if idade > 0 and idade <= 100:
            print("Idade:", idade)
            break
        else:
            print("Idade invalida")
    except ValueError:
        #caso der erro executa aqui
        print("Digite sua idade em numero. Ex: 26")
