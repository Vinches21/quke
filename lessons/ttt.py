from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


def calc(): #решалка задания
    driver.find_element(By.CLASS_NAME, 'form-control').send_keys(
        str(math.log(abs(12 * math.sin(int(
            driver.find_element(By.ID, 'input_value').text))))))
    driver.find_element(By.ID, "solve").click()


def returnTextInElement(time, element, text): #ждем когда текст будет 100 в прайсе
        return WebDriverWait(driver, time).until(EC.text_to_be_present_in_element((By.ID, element), text))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    driver = webdriver.Chrome(executable_path='C:\\Users\\Home\PycharmProjects\\resource\\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get(link)

    returnTextInElement(15, 'price', '100')
    driver.find_element(By.ID, 'book').click()
    calc()

finally:
    time.sleep(5)
    driver.quit()