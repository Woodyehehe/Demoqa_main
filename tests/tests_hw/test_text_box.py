import time
from pages.text_box import TextBox

def test_text_box(browser):
    text_box = TextBox(browser)

    text_box.visit()
    text_box.full_name.send_keys('Testerov')
    text_box.current_address.send_keys('street Vyazov, 13')
    text_box.btn_submit.click_force()
    time.sleep(2)
    text_box.name.exist()
    time.sleep(2)
    text_box.address.exist()
    time.sleep(2)
    assert text_box.name.get_text() == 'Name:Testerov'
    assert text_box.address.get_text() == 'Current Address :street Vyazov, 13'

