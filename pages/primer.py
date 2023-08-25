from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

try: 
    url = "https://www.mosoboi.ru/catalog/floralia/"
    driver = browser = webdriver.Chrome(executable_path='C:\\Users\\Home\PycharmProjects\\resource\\chromedriver.exe')
    driver.get(url)
    driver.maximize_window()


    elements = driver.find_elements(By.XPATH, '//a[@class="btn__cart in_basket add2basket"]')
    print(len(elements))
    for elem in elements:
        elem.click()

    time.sleep(5)


    # button_order = driver.find_elements(By.CSS_SELECTOR, '[href="/personal/order/make/"]')
    button_order = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[href="/personal/order/make/"]')))
    button_order.click()
    time.sleep(3)





finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()