import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_exist(browser):
    browser.get(link)
    # time.sleep(30)
    bttn = browser.find_element_by_css_selector('button.btn.btn-lg.btn-primary.btn-add-to-basket')
    assert bttn, "Button 'Add to basket' doesn't exist"