from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    button_magic = browser.find_element_by_css_selector(".btn-primary")
    button_magic.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    field = browser.find_element_by_id("answer")
    field.send_keys(y)

    button_submit = browser.find_element_by_css_selector(".btn-primary")
    button_submit.click()

finally:
    time.sleep(10)
    browser.quit()
