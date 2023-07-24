import time
from pages.form_page import FormPage

def test_login_form(browser):
    form_page = FormPage(browser)

    form_page.visit()
    assert not form_page.modal_dialog.exist()
    time.sleep(2)
    form_page.first_name.send_keys('tester')
    form_page.last_name.send_keys('testerovich')
    form_page.user_email.send_keys('test@ttt.tt')
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys('9992223344')
    form_page.hobbies.click_force()
    form_page.current_address.send_keys('street')
    time.sleep(2)
    form_page.btn_submit.click_force()
    time.sleep(2)
    assert form_page.modal_dialog.exist()
    form_page.btn_close_modal.click_force()

# дз 9* МОЗГ ВЫШЕЛ ИЗ ЧАТА :((
#
# def test_full_field(browser):
#     form_page = FormPage(browser)
#
#     form_page.visit()
#     form_page.state.find_element()
#     form_page.state.click()
#     for element in form_page.state_choose.find_element():
#         if element == 'NCR':
#             form_page.state.click()
#             break
#         if element == 'Uttar Pradesh':
#             form_page.state.click()
#             break
#         if element == 'Haryana':
#             form_page.state.click()
#             break
#         if element == 'Rajastan':
#             form_page.state.click()
#             break
