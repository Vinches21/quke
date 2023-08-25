import time
import math
import os
import pyperclip
import pytest


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import  Options


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(executable_path='C:\\Users\\Home\PycharmProjects\\resource\\chromedriver.exe', chrome_options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, link):
    url = f'https://stepik.org/lesson/{link}/step/1'
    browser.get(url)
    vxod = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@id="ember33"]')))
    vxod.click()

    email = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="id_login_email"]')))
    email.send_keys('')

    password = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//input[@id="id_login_password"]')))
    password.send_keys('')

    button_vxod = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@class="sign-form__btn button_with-loader "]')))
    button_vxod.click()


    answer = math.log(int(time.time()))
    print(answer)
    text = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.textarea')))
    print('YES')
    text.send_keys(answer)

    button_submit = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@class="submit-submission"]')))
    button_submit.click()

    message = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='smart-hints__hint']")))

    values_message = message.text
    assert values_message == 'Correct!', message.text
    print(message.text)







# url = 'https://stepik.org/lesson/236895/step/1'

# """Getters"""
#
# browser = webdriver.Chrome(executable_path='C:\\Users\\Home\PycharmProjects\\resource\\chromedriver.exe')
# browser.get(url)
# browser.maximize_window()
#
# vxod = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//a[@id="ember33"]' )))
# vxod.click()
#
# email = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="id_login_email"]')))
# email.send_keys('Vinches2193@yandex.ru')
#
# password = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="id_login_password"]')))
# password.send_keys('cwbkf2193')
#
# button_vxod = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="sign-form__btn button_with-loader "]')))
# button_vxod.click()

