import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_in_basket_search(browser):
    browser.get(link)
    browser.maximize_window()
    time.sleep(5)
    button_basket = browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')
    assert len(button_basket.text) > 0, "Проблема с кнопкой"

