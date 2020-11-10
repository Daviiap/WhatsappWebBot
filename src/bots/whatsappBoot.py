from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


class Bot:
    def __init__(self, executable_path):
        self.driver = webdriver.Firefox(
            executable_path=executable_path
        )

    def __openArchive(self, archivePath, splitText):
        try:
            file = open(
                archivePath, 'r'
            )

            text = file.read()

            if splitText:
                text = text.split(' ')

        except Exception:
            print('Error ao abrir arquivo!')

        file.close()

        return text

    def start(self,
              interval=100,
              archivePath='',
              passedText='Auto_Send_BOT',
              splitText=False,
              repeatTimes=100):

        driver = self.driver
        driver.get('http://web.whatsapp.com')

        if archivePath != '':
            isArchive = True
        else:
            isArchive = False

        if isArchive:
            text = self.__openArchive(archivePath, splitText)
        else:
            if splitText:
                text = passedText.split(' ')
            else:
                text = passedText

        print('Antes de iniciar a execução do bot,\n' +
              'abra a conversa que você deseja mandar\n' +
              'as mensagens e depois precione \'Enter\'.')
        print('\nAguardando a conexão do whatsapp web...')
        input(
            '\n\n\n' +
            'Assim que conectado e aberta a conversa\n' +
            'pressione \'ENTER\'\n')

        try:
            chat_box = driver.find_element_by_xpath(
                '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
            chat_box.click()
            chat_box.clear()

            if splitText:
                for word in text:
                    if '-' in word:
                        word = word.strip('-')

                    if ',' in word:
                        word = word.rstrip(',')

                    time.sleep(interval/1000)

                    chat_box.send_keys(word + '\n')
            else:
                for i in range(repeatTimes):
                    time.sleep(interval/1000)

                    chat_box.send_keys(text + '\n')

        except Exception:
            print('Não foi realizada a conexão do WhatsApp Web, tente novamente...')
            driver.close()


bot = Bot('/home/davi/Projetos/Personal/Auto_send_wpp_BOT/src/assets/geckodriver')

try:
    bot.start(interval=100,
              archivePath='/home/davi/Projetos/Personal/Auto_send_wpp_BOT/src/texts/sas.txt',
              splitText=True)
except KeyboardInterrupt:
    print('\nServiço parado!')
    print('\nObrigado por usar o whatsapp auto_send WebBot!')
