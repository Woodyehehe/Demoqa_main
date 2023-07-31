from pages.base_page import BasePage
from components.components import WebElement

class ModalDialogs(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btn_all = WebElement(driver, 'div:nth-child(3) > div > ul > li')
        self.icon = WebElement(driver, 'header > a > img')
        self.btn_small = WebElement(driver, '#showSmallModal')
        self.btn_large = WebElement(driver, '#showLargeModal')
        self.modal_window = WebElement(driver, '.show > div > div')
        self.btn_close_small = WebElement(driver, '#closeSmallModal')
        self.btn_close_large = WebElement(driver, '#closeLargeModal')

