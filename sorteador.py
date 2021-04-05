from selenium.webdriver import Firefox
import time
import random

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = Firefox()

    def ComentarEmFoto(self):
        browser = self.driver
        browser.get("https://www.instagram.com")
        time.sleep(3)
        email = browser.find_element_by_name("username")
        email.click()
        email.send_keys(self.username)

        senha = browser.find_element_by_name("password")
        senha.click()
        senha.send_keys(self.password)
        login_button_ = browser.find_element_by_css_selector(".sqdOP > .Igw0E")
        login_button_.click()

        time.sleep(3)
        browser.get("link da postagem")


        users = ['@user']
        contador = 0
        while(contador < 10):
          for user in users:
            comentar = browser.find_element_by_css_selector(".X7cDz .\_8-yf5")
            comentar.click()
            time.sleep(1)

            texto = browser.find_element_by_css_selector(".Ypffh")
            texto.send_keys(user)

            publicar = browser.find_element_by_css_selector(".sqdOP:nth-child(4)")

            time.sleep(1)
            publicar.click()
            time.sleep(3)
        contador += 1

jhonatanBot = InstagramBot("seuUsuario", "suaSenha")
jhonatanBot.ComentarEmFoto()