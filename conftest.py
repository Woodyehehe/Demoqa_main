import pytest
from selenium import webdriver
from pages.accordion import Accordion
from pages.alerts import Alerts
from pages.demoqa import DemoQa
from pages.browser_tab import BrowserTab
import time

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    driver.set_window_size(width=1000, height=1000)
    yield driver
    driver.quit()

@pytest.mark.parametrize("pages", [Accordion, Alerts, DemoQa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert page.get_title() == 'DEMOQA'
