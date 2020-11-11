from whatsappBoot import Bot


# '/home/davi/Projetos/Personal'

diretorio = input('Digite o diretório onde está a pasta principal do Bot: ')

bot = Bot(diretorio + '/Auto_send_wpp_BOT/src/assets/geckodriver')

try:
    bot.start(interval=100,
              archivePath='/home/davi/Projetos/Personal/Auto_send_wpp_BOT/src/texts/sas.txt',
              splitText=True)
except KeyboardInterrupt:
    print('\nServiço parado!')
    print('\nObrigado por usar o whatsapp auto_send WebBot!')
