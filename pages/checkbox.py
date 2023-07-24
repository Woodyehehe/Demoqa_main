from pages.base_page import BasePage
from components.components import WebElement

class CheckBox(BasePage): #создаем класс из род.класса
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/checkbox'
        super().__init__(driver, self.base_url)

        self.btn_checkbox = WebElement(driver, 'span.rct-text')
        self.btn_plus_checkbox = WebElement(driver, '.rct-option-expand-all')

