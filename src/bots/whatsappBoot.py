from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


class Bot:
    def __init__(self):
        self.driver = webdriver.Firefox(
            executable_path="/home/davi/Projetos/Personal/Auto_send_wpp_BOT/src/assets/geckodriver")

    def __openArchive(self):
        try:
            file = open(
                '/home/davi/Projetos/Personal/Auto_send_wpp_BOT/src/texts/sas.txt', 'r')

            text = file.read()
            text = text.split(" ")

        except Exception:
            print("Error ao abrir arquivo!")

        file.close()

        return text

    def start(self, interval):
        driver = self.driver
        driver.get("http://web.whatsapp.com")

        text = self.__openArchive()

        print("Aguardando a conexão do whatsapp web...")
        input("Assim que conectado pressione ENTER")

        chat_box = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
        chat_box.click()
        chat_box.clear()

        try:
            for word in text:
                if "-" in word:
                    word = word.strip("-")

                if "," in word:
                    word = word.rstrip(",")

                time.sleep(interval/1000)

                chat_box.send_keys("BOT" + "\n")

                # chat_box.send_keys(word + "\n")

        except KeyboardInterrupt:
            print("\nServiço parado!")
            print("\nObrigado por usar o whatsappWebBot!")


bot = Bot()
bot.start(interval=100)
