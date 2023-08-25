import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver import ActionChains, Keys
from utilities.logger import Logger
import allure

class Forms(Base):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    region = '/html/body/div[1]/div/div[2]/a'
    krasnodar = '//*[@id="fancybox-container-1"]/div[2]/div[4]/div/div/div/div[3]/div[2]/div[2]/div[1]/a'
    gorod = '//*[@id="region2__form-input"]'
    gorod_iz_spiska = '/html/body/div[13]/div[2]/div[4]/div/div/div/div[2]/form/ul'
    close = '//*[@id="fancybox-container-1"]/div[2]/div[4]/div/div/a'
    poisk = '//*[@id="main-search-input"]'

    title = '/html/body/main/div[1]/div[1]/div/h1'

    # Getters_menu
    def get_region(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.region)))

    def get_krasnodar(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.krasnodar)))

    def get_gorod(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.gorod)))

    def get_gorod_iz_spiska(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.gorod_iz_spiska)))

    def get_close(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.close)))

    def get_poisk(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.poisk)))

    def get_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.title)))

    # Actions

    def click_region(self):
        self.driver.execute_script("arguments[0].click();", self.get_region())
        print('Кликнули на регион')
        # self.get_region().click()

    def select_region(self):
        self.driver.execute_script("arguments[0].click();", self.get_krasnodar())
        print('Выбираем Краснодар')
        # self.get_region().click()


    def input_gorod(self, gorod):
        self.get_gorod().send_keys(gorod)
        self.driver.execute_script("arguments[0].click();", self.get_gorod_iz_spiska())
        self.get_close().click()
        # self.get_gorod_iz_spiska().click()

    def input_poisk(self, poisk):
        self.get_poisk().send_keys(poisk)
        self.get_poisk().send_keys(Keys.RETURN)
        print('Ввели значение в поиск')


    #Methods
    def select_region(self):
        with allure.step('Select region'):
            self.click_region()
            self.select_region()

        # self.get_gorod_iz_spiska().click()

    def select_poisk(self):
        with allure.step('Select_poisk'):
            Logger.add_start_step(method='select_poisk')
            self.input_poisk('Xiaomi redmi note 11')
            self.get_screenshot()
            self.assert_word(self.get_title(), 'Результаты поиска: «Xiaomi redmi note 11»')
            Logger.add_end_step(url=self.driver.current_url, method='select_poisk')