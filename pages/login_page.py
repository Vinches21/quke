import  time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger
import allure

class Login_page(Base):
    def __init__(self,driver):
        super().__init__(driver)

    #Locators

    entry = '/html/body/div[1]/div/div[5]/a[2]/span' #click
    registr = '//*[@id="fancybox-container-1"]/div[2]/div[4]/div/div/div/div[1]/ul/li[2]' #click
    name = '//input[@id="reg-name"]'
    email = '//input[@id="reg-email"]'
    password = '//input[@id="reg-pass"]'
    password_replay = '//input[@id="reg-pass-conf"]' #send
    consent = '//*[@id="reg-form"]/div[5]/div/label[1]' #click
    close = '//*[@id="fancybox-container-1"]/div[2]/div[4]/div/div/button'
    #button_registr = '//*[@id="reg-form"]/div[6]/button'

    #Getters

    def get_entry(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.entry)))

    def get_registr(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.registr)))

    def get_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_password_replay(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password_replay)))

    def get_consent(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.consent)))

    #def get_button_registr(self):
        # return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_registr)))

    def get_close(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.close)))
    #Actions

    def click_entry(self):
        self.get_entry().click()
        print('Входим в регистрацию')

    def click_registr(self):
        self.get_registr().click()
        print('Выбираем Регистрация')

    def input_name(self, name):
        self.get_name().send_keys(name)
        print('Вводим имя')

    def input_email(self, email):
        self.get_email().send_keys(email)
        print('Вводим email')

    def input_password(self, password):
        self.get_password().send_keys(password)
        print('Вводим password')

    def input_password_replay(self, password_replay):
        self.get_password_replay().send_keys(password_replay)
        print('Подтверждаем password')


    def click_consent(self):
        self.get_consent().click()
        print('Соглашаемся с условиями')


    # #def click_button_registr(self):
    #     self.get_button_registr().click()
    #     print('Нажимаем на кнопку Регистрация')

    def click_close(self):
        self.get_close().click()
        print('Закрываем окно')

    # Methods

    def authorization(self):
        with allure.step('Authorization'):
            Logger.add_start_step(method='authorization')
            self.click_entry()
            time.sleep(2)
            self.click_registr()
            self.input_name('Oleg')
            self.input_email('test4854545@mail.ru')
            self.input_password('74554545')
            self.input_password_replay('74554545')
            self.click_consent()
            self.click_close()
            self.click_close()
            Logger.add_end_step(url=self.driver.current_url, method='authorization')





