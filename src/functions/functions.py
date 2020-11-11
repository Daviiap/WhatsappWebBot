def getInterval():
    interval = 0

    print(
        'Você deseja uma cadência alta[10 msg/s] ou baixa[1 msg/s] para envio das mensagens? ')

    print('ALTA(1) | BAIXA(2) | DEFINIR CADÊNCIA(Qualquer caractere)')
    option = input()

    if option == '1':
        interval = 100
    elif option == '2':
        interval = 1000
    else:
        print('Digite a quantidade de mensagens por segundo que você deseja enviar')
        msg_quantity = int(input())

        if msg_quantity <= 0:
            interval = 1000
        else:
            interval = 1000/msg_quantity

    return interval


def getText():
    return ''


def getArchive():
    return ''
