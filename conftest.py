import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import  Options

@pytest.fixture()
def set_up():
    print('Start test')
    yield
    print('Finish test')

@pytest.fixture(scope="function")
def driver():
    print("\nStart browser for test..")
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\Home\PycharmProjects\\resource\\chromedriver.exe', chrome_options=options)
    yield driver
    print("\nQuit browser..")
    # driver.quit()