import os
from bot import whatsappBot
from functions import functions


# diretorio = input('Digite o diretório onde está a pasta principal do Bot: ')

bot = whatsappBot.Bot(os.getcwd() + '/assets/geckodriver')


archivePath = functions.getText()
passedText = functions.getArchive()

splitText = False

interval = functions.getInterval()

repeatTimes = 0

try:
    bot.start(interval=interval,
              archivePath='/home/davi/Projetos/Personal/Auto_send_wpp_BOT/src/assets/texts/sas.txt',
              splitText=True)
except KeyboardInterrupt:
    print('\nServiço parado!')
    print('\nObrigado por usar o whatsapp auto_send WebBot!')

except UnboundLocalError:
    print('\nO arquivo de texto informado não existe!')
