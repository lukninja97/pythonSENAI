# O while repete tudo que esta dentro dele
while True:
    # O try vai tentar executar esse bloco de codigo
    try:
        idade = int(input("Digite sua idade: "))

        # O if verifica se idade é valida
        if idade > 0 and idade <= 100:
            print("Idade:", idade)
            # O break sai do while
            break
        else:
            print("Idade invalida")
    except ValueError:
        # Caso der erro executa aqui
        print("Digite sua idade em numero. Ex: 26")
