import  time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger
import allure

class Main_page(Base):
    url = 'https://quke.ru'

    def __init__(self, driver):
        super(). __init__(driver)

    #Locators_menu

    smartfony = '/html/body/nav/div/div[2]/div/ul/li[1]/a'
    planchety = '/html/body/nav/div/div[2]/div/ul/li[2]/a'
    noutbuki = '/html/body/nav/div/div[2]/div/ul/li[3]/a'
    smartfony_apple = '/html/body/nav/div/div[2]/div/ul/li[4]/a'
    smartfony_xiomi = '/html/body/nav/div/div[2]/div/ul/li[5]/a'

    #Getters_menu

    def get_smartfony(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.smartfony)))
    def get_planchety(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.planchety)))
    def get_noutbuki(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.noutbuki)))
    def get_smartfony_apple(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.smartfony_apple)))
    def get_smartfony_xiomi(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.smartfony_xiomi)))

    # Actions
    def select_smartfony(self):
        with allure.step('Select smartfony'):
            Logger.add_start_step(method='select_smartfony')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_smartfony().click()
            print('Кликнули на раздел Смартфоны')
            self.get_current_url()
            Logger.add_end_step(url=self.driver.current_url, method='select_smartfony')



    # Methods

    def section_smartphony(self):
        with allure.step('Select smartphony'):
            self.select_smartfony()
            self.get_current_url()
            time.sleep(5)
            self.driver.back()
            time.sleep(3)


