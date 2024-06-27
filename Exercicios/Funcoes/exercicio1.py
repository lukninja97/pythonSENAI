from datetime import datetime


def solicita_nome():
    nome = input('Qual o seu nome? ')
    return nome


def define_saudacao(hora_atual):
    if hora_atual >= 0 and hora_atual <= 5:
        saudacao = "Boa madrugada "
    elif hora_atual <= 12:
        saudacao = "Bom dia "
    elif hora_atual <= 19:
        saudacao = "Boa tarde "
    else:
        saudacao = "Boa noite "

    return saudacao


def exibir_mensagem(nome, saudacao):
    print(saudacao + nome)


exibir_mensagem(solicita_nome(), define_saudacao())
