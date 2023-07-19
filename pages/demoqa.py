from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from components.components import WebElement

class DemoQa(BasePage): #создаем класс из род.класса

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        self.icon = WebElement(driver, locator='#app > header > a')
        self.btn_elements = WebElement(driver, locator='#app > div > div > div.home-body > div > div:nth-child(1)')
        super().__init__(driver, self.base_url)


    # def exist_icon(self):
    #     try:
    #         self.icon.find_element() #поиск для конкретного элемента
    #     except NoSuchElementException:
    #         return False
    #     return True

    # def click_on_the_icon(self):
    #     return self.find_element(locator='#app > header > a').click()
    #
    # def click_on_the_btn_something(self):
    #     return self.find_element(locator='#app > div > div > div.home-body > div > div:nth-child(1)').click()

