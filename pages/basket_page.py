import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver import ActionChains, Keys
from utilities.logger import Logger
import allure
from selenium.common.exceptions import TimeoutException

class Basket_page(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    uslugi = '//div[@class="order-basket__add-services order-basket__add-services--closed"]'
    paket = '//*[@id="item-117807"]/div[2]/div/div[5]/form/ul/li[3]/table/tbody/tr/td[2]/label'
    dostavka = '//*[@id="order-form"]/div[2]/div[1]/div[1]/div'
    mkad = '//*[@id="order-form"]/div[2]/div[1]/div[1]/div/ul/li[2]'
    email = '//input[@id="order_mail"]'
    name = '//input[@id="order_name_person"]'
    mobile = '//input[@id="order_tel_name"]'
    promokod = '//input[@id="discount_promocode"]'
    comment = '//textarea[@id="adr_name"]'

    # Getters

    def get_uslugi(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.uslugi)))

    def get_paket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.paket)))

    def get_dostavka(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.dostavka)))

    def get_mkad(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mkad)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name)))

    def get_mobile(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mobile)))

    def get_promokod(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.promokod)))

    def get_comment(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.comment)))

    # Actions
    def click_uslugi(self):
        self.get_uslugi().click()
        print('Кликнули на Доп. Услуги')

    def click_paket(self):
        self.get_paket().click()
        print('Выбрали Пакет')


    def click_dostavka(self):
        self.driver.execute_script('window.scrollTo(0, 1400)')
        self.driver.execute_script("arguments[0].click();", self.get_dostavka())
        # self.get_dostavka().click()
        print('Выбираем способ доставки')


    def select_mkad(self):
        self.driver.execute_script("arguments[0].click();", self.get_mkad())
        # self.get_mkad().click()
        print('Выбираем в пределах МКАД')

    def input_email(self, email):
        self.get_email().send_keys(email)
        print('Вводим емэйл')

    def input_name(self, name):
        self.get_name().send_keys(name)
        print('Вводим имя')

    def input_mobile(self, mobile):
        # self.driver.execute_script('window.scrollTo(0, 1600)')
        self.get_mobile().send_keys(mobile)
        print('Вводим номер телефона')

    def input_promokod(self, promokod):
        self.get_promokod().send_keys(promokod)
        print('Вводим промокод')

    def input_comment(self, comment):
        self.get_comment().send_keys(comment)
        print('Вводим комментарий')


    # Methods

    def oform(self):
        with allure.step('Oform'):
            Logger.add_start_step(method='oform')
            self.click_uslugi()
            self.click_paket()
            self.click_dostavka()
            self.select_mkad()
            self.input_email('4815162342@rambler.ru')
            self.input_name('Fantomas')
            self.input_mobile('79001002020')
            self.input_promokod('test2022')
            self.input_comment('Текстовый текст')
            Logger.add_end_step(url=self.driver.current_url, method='oform')

