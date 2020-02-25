from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time, math

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id("num1").text
    y = browser.find_element_by_id("num2").text
    sum =  str(int(x) + int(y))
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(sum)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
