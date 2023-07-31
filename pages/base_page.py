import logging
import requests
from components.components import WebElement

from selenium.webdriver.common.by import By
import time

class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url # 'https://demoqa.com/'
        self.metaView = WebElement(driver, 'head > meta')

    def visit(self):
        return self.driver.get(self.base_url)

    # def find_element(self, locator):
    #     time.sleep(3)
    #     return self.driver.find_element(By.CSS_SELECTOR, locator)

    def back(self):
        return self.driver.back()

    def forward(self):
        return self.driver.forward()

    def refresh(self): # обновление страницы, без сбрасывания кэша
        return self.driver.refresh()

    def get_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title #если отрибут, то скобки не нужны

    def equal_url(self):
       if self.get_url() == self.base_url:
            return True
       return False

    def alert(self):
        try:
            return self.driver.switch_to.alert # этот метод позволяет подтвердить что алерт открыт
        except Exception as ex:
            logging.log(1, ex)
            return False

    def code_status(self): # проверка статуса страницы
        resp = requests.get(self.base_url)
        return resp.status_code == 200 # лучше сделать переменную

