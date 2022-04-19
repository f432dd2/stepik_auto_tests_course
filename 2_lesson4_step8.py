from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    price = browser.find_element_by_id("price")
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element_by_id("book").click()
    x_element = browser.find_element_by_id("input_value")
    x = calc(x_element.text)
    input_1 = browser.find_element_by_id("answer")
    input_1.send_keys(x)
    button = browser.find_element_by_id("solve").click()
finally:
    time.sleep(10)
    browser.quit()
