from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


class Bot:
    def __init__(self):
        self.driver = webdriver.Firefox(
            executable_path='/home/davi/Projetos/Personal/Auto_send_wpp_BOT/src/assets/geckodriver'
        )

    def __openArchive(self, archivePath='/home/davi/Projetos/Personal/Auto_send_wpp_BOT/src/texts/sas.txt', splitText=True):
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
              isArchive=False,
              passedText='Auto_Send_BOT',
              splitText=False,
              repeatTimes=100):

        driver = self.driver
        driver.get('http://web.whatsapp.com')

        if isArchive:
            text = self.__openArchive(archivePath, splitText)
        else:
            if splitText:
                text = passedText.split(' ')
            else:
                text = passedText

        print('Antes de iniciar a execução do bot, abra a conversa que você deseja mandar as mensagens e depois precione \'Enter\'')
        print('Aguardando a conexão do whatsapp web...')
        input('Assim que conectado pressione ENTER para iniciar a execução do chatBot')

        chat_box = driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
        chat_box.click()
        chat_box.clear()

        try:
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

        except KeyboardInterrupt:
            print('\nServiço parado!')
            print('\nObrigado por usar o whatsapp auto_send WebBot!')


bot = Bot()
bot.start(interval=100)
