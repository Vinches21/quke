import  time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger
import allure
from selenium.common.exceptions import TimeoutException


class Cartochka_page(Base):

    def __init__(self, driver):
        super(). __init__(driver)

    #Locators

    button_buy = '/html/body/main/div[2]/div[6]/div[3]/div[1]/div[6]/a[1]'
    button_place_an_order = '//button[@class="btn main__btn"]'
    name_model = '/html/body/main/div[2]/div[2]/div/h1/span'


    #Getters

    def get_button_buy(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_buy)))

    def get_button_place_an_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_place_an_order)))

    def get_name_model(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_model)))


    # Actions
    def click_button_buy(self):

        self.get_button_buy().click()
        print('Нажимаем на кнопку купить')

    def nazvanie_name_model(self):
        value_name_model = self.get_name_model().text
        print(value_name_model) # Считываем название модели

    def click_button_place_an_order(self):
        self.driver.execute_script("arguments[0].click();", self.get_button_place_an_order())
        # self.get_button_place_an_order().click()
        print('Нажимаем на кнопку Оформить заказ')




    # Methods

    def curt_buy(self):
        with allure.step('Curt buy'):
            Logger.add_start_step(method='curt_buy')
            self.get_current_url()
            self.nazvanie_name_model()
            self.click_button_buy()
            time.sleep(2)
            try:
                self.click_button_place_an_order()
            except TimeoutException:
                print('Кнопка Оформить заказ не нашлась')
            self.get_current_url()
            self.assert_url('https://quke.ru/order')
            Logger.add_end_step(url=self.driver.current_url, method='curt_buy')



