import time
import math
import os

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url= "http://suninjuly.github.io/redirect_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))



try:
    driver = webdriver.Chrome(executable_path='C:\\Users\\Home\PycharmProjects\\resource\\chromedriver.exe')
    driver.get(url)

    button = driver.find_element(By.XPATH, '//button[@class="trollface btn btn-primary"]')
    button.click()

    new_vindow = driver.window_handles[1]
    driver.switch_to.window(new_vindow)

    x_element = driver.find_element(By.XPATH, '//span[@id="input_value"]')
    x = x_element.text
    print(x)
    y = calc(x)
    pole_text = driver.find_element(By.XPATH, '//input[@id="answer"]')
    pole_text.send_keys(y)
    button_sub = driver.find_element(By.XPATH, '//button[@class="btn btn-primary"]')
    button_sub.click()
    alert = driver.switch_to.alert
    print(alert.text.split()[-1])
    # print(driver.switch_to.alert.text.split()[-1])




finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    driver.quit()


# не забываем оставить пустую строку в конце файла