from datetime import datetime

def menu_calculadora():
    print("Menu calculadora")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicacão")
    print("4 - Divisão")


def ola_nome(nome):
    print("Ola", nome)


def calcula_idade(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade

def exibir_idade(idade):
    print("A sua idade é", idade, "anos")

# menu_calculadora()

#ola_nome("Luciano")
#ola_nome("Lucas")

def solicita_ano_nascimento():
    while True:
        try:
            ano_nascimento = int(input("Digite o ano de nascimento: "))
            if ano_nascimento < datetime.now().year:
                return ano_nascimento
            else:
                print("Digite um ano menor que o atual")
        except ValueError:
            print("Digite somente numeros. Ex: 1997")

solicita_ano_nascimento()
#exibir_idade(calcula_idade(ano_nascimento))



