from selenium import webdriver
import time
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    field1 = browser.find_element_by_name("firstname")
    field1.send_keys("Lapim")

    field2 = browser.find_element_by_name("lastname")
    field2.send_keys("Jabenok")

    field3 = browser.find_element_by_name("email")
    field3.send_keys("Lapim.Jabenok@pim.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'jabenok.txt')

    element = browser.find_element_by_id("file")
    element.send_keys(file_path)

    button = browser.find_element_by_css_selector(".btn-primary")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
