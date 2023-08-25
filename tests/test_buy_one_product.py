import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.smartfon_page import Smartfon_page
from pages.cartocka_page import Cartochka_page
from pages.basket_page import Basket_page
import allure


"""Тестируем покупку одного товара"""
@allure.description('Test buy one product 1')
def test_buy_one_product(driver):
    # options = Options()
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # driver = webdriver.Chrome(executable_path='C:\\Users\\Home\PycharmProjects\\resource\\chromedriver.exe', chrome_options=options)
    print('Start Test buy_one_product')

    mp = Main_page(driver)
    mp.select_smartfony()

    sp = Smartfon_page(driver)
    sp.filter()

    cp = Cartochka_page(driver)
    cp.curt_buy()

    bp = Basket_page(driver)
    bp.oform()
    print('Finish Test buy_one_product')

"""Тестируем покупку 3-х товаров"""
@pytest.mark.skip
@allure.description('Test buy multiple product')
def test_buy_multiple_product(driver):
    url = 'https://quke.ru/shop/smartfony'
    # options = Options()
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # driver = webdriver.Chrome(executable_path='C:\\Users\\Home\PycharmProjects\\resource\\chromedriver.exe', chrome_options=options)
    print('Start Test multiple_product')
    # driver.get(url)
    # driver.maximize_window()

    # lp = Login_page(driver)
    # lp.authorization()

    mp = Main_page(driver)
    mp.select_smartfony()

    sp = Smartfon_page(driver)
    sp.multiple()

    bp = Basket_page(driver)
    bp.oform()
    print('Finish Test multiple_product')