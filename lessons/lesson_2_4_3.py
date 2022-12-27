import time
import math
import os

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url= "http://suninjuly.github.io/wait1.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))



try:
    driver = webdriver.Chrome(executable_path='C:\\Users\\Home\PycharmProjects\\resource\\chromedriver.exe')
    driver.get(url)

    driver.implicitly_wait(5)
    button = driver.find_element(By.XPATH, '//button[@id="verify"]')
    button.click()

    word = driver.find_element(By.XPATH, '//div[@id="verify_message"]')
    assert 'successful' in word.text
    print('Good')


    # alert = driver.switch_to.alert
    # print(alert.text.split()[-1])
    # print(driver.switch_to.alert.text.split()[-1])




finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    driver.quit()


# не забываем оставить пустую строку в конце файла