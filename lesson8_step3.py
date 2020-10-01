from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id('num1')
    num2 = browser.find_element_by_id('num2')
    x = int(num1.text)
    y = int(num2.text)
    sum = str(x + y)

    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_value(sum)

    button = browser.find_element_by_css_selector(".btn-default")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
