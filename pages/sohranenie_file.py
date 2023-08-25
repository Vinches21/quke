import time
import math
import os

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url= "http://suninjuly.github.io/file_input.html"





try:
    driver = webdriver.Chrome(executable_path='C:\\Users\\Home\PycharmProjects\\resource\\chromedriver.exe')
    driver.get(url)

    f_name = driver.find_element(By.XPATH, '//input[@name="firstname"]')
    f_name.send_keys('Bruse')

    l_name = driver.find_element(By.XPATH, '//input[@name="lastname"]')
    l_name.send_keys('Wane')

    email = driver.find_element(By.XPATH, '//input[@name="email"]')
    email.send_keys('gotam@gmail.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "test7.txt"
    file_path = os.path.join(current_dir, file_name)
    element = driver.find_element(By.CSS_SELECTOR, "[type='file']")
    # file_name = 'C:\\Users\Home\\PycharmProjects\\quke\\files\\test555.txt'
    # element.send_keys(file_name)
    element.send_keys(file_path)

    button = driver.find_element(By.XPATH, '//button[@class="btn btn-primary"]').click()
    # email.send_keys('gotam@gmail.com')

    alert = driver.switch_to.alert
    print(alert.text)
    # print(driver.switch_to.alert.text.split()[-1])




finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    driver.quit()


# не забываем оставить пустую строку в конце файла