import time
import math
import os
import pyperclip

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url= "http://suninjuly.github.io/explicit_wait2.html"
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    driver = webdriver.Chrome(executable_path='C:\\Users\\Home\PycharmProjects\\resource\\chromedriver.exe')
    driver.get(url)

    price = WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.XPATH, '//h5[@id="price"]'), '100'))

    button_book = WebDriverWait(driver, 12).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="book"]')))
    button_book.click()

    x_element = driver.find_element(By.XPATH, '//span[@id="input_value"]')
    x = x_element.text
    print(x)
    y = calc(x)
    pole_text = WebDriverWait(driver, 12).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="answer"]')))
    pole_text.send_keys(y)
    driver.execute_script('window.scrollTo(0, 150)')
    button_sub = WebDriverWait(driver, 12).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="solve"]')))
    button_sub.click()
    alert = driver.switch_to.alert
    print(alert.text.split()[-1])
    alert_text = alert.text
    addToClipBoard = alert_text.split(' ')[-1]
    pyperclip.copy(addToClipBoard)



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    driver.quit()


# не забываем оставить пустую строку в конце файла