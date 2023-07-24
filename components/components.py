from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

class WebElement:
    def __init__(self, driver, locator=''):
        self.driver = driver
        self.locator = locator

    def click(self):
        self.find_element().click()

    def click_force(self): #используем в кранйем случае, если знаем, что перекрывает кнопку
        self.driver.execute_script("arguments[0].click();", self.find_element())

    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def find_elements(self):  # пользуемся, когда надо посчитать кол-во эл-ов или надо сделать цикличную проверку
                                # (один тест, но для каждого эл-та)
        return self.driver.find_elements(By.CSS_SELECTOR, self.locator)

    def check_count_elements(self, count: int) -> bool:
        if len(self.find_elements()) == count:
            return True
        return False

    def exist(self):
        try:
            self.find_element() #поиск для конкретного элемента
        except NoSuchElementException:
            return False
        return True

    def get_text(self):
        return self.find_element().text

    def visible(self):
        return self.find_element().is_displayed()

    def send_keys(self, text: str):
        self.find_element().send_keys(text)

    def clear(self):
        self.find_element().send_keys(Keys.CONTROL + 'a')
        self.find_element().send_keys(Keys.DELETE)


