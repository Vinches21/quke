import time
import math

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url= "https://SunInJuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome(executable_path='C:\\Users\\Home\PycharmProjects\\resource\\chromedriver.exe')
    driver.get(url)

    x_element = driver.find_element(By.XPATH, '//span[@id="input_value"]')
    x= x_element.text
    print(x)
    y = calc(x)
    pole_text = driver.find_element(By.XPATH, '//input[@id="answer"]')
    pole_text.send_keys(y)

    driver.execute_script("window.scrollBy(0, 100);")

    check_im = driver.find_element(By.XPATH, '//input[@id="robotCheckbox"]').click()
    # check_im.click()


    # driver.execute_script("return arguments[0].scrollIntoView(true);", button_sub)



    rule = driver.find_element(By.XPATH, '//input[@id="robotsRule"]').click()
    # rule.click()

    button_sub = driver.find_element(By.XPATH, '//button[@class="btn btn-default"]')
    # driver.execute_script("return arguments[0].scrollIntoView(true);", button_sub)

    # driver.execute_script("return arguments[0].scrollIntoView(true);", button_sub)
    button_sub = driver.find_element(By.XPATH, '//button[@class="btn btn-default"]').click()
    # button_sub.click()

    print(driver.switch_to.alert.text.split()[-1])




finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(8)
    # закрываем браузер после всех манипуляций
    driver.quit()


# не забываем оставить пустую строку в конце файла