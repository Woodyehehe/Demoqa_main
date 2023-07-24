import time
from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage

def test_size_demoqa(browser):
    demo_qa_page = DemoQa(browser)

    demo_qa_page.visit()
    browser.set_window_size(1000, 300)
    time.sleep(2)
    browser.set_window_size(1000, 1000)

def test_visible_nav_bar(browser):
    elements = ElementsPage(browser)

    elements.visit()
    assert not elements.element_mobile.visible()
    browser.set_window_size(767, 1000)
    elements.element_mobile.visible()
    browser.set_window_size(1000, 1000)

