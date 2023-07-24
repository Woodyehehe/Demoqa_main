from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage

def test_check_title_demo(browser):
    demo_qa_page = DemoQa(browser)

    demo_qa_page.visit()
    assert demo_qa_page.get_title() == 'DEMOQA'
