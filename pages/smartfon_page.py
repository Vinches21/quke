import  time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from base.base_class import Base
from selenium.webdriver import ActionChains, Keys
from utilities.logger import Logger
import allure
from selenium.common.exceptions import TimeoutException



class Smartfon_page(Base):

    def __init__(self, driver):
        super().__init__(driver)


    # Locators

    price_min = '/html/body/main/div[3]/div[2]/div/div/div[2]/div/div/form/div[2]/div[2]/div/div[1]/div[1]/input'

    price_max = '/html/body/main/div[3]/div[2]/div/div/div[2]/div/div/form/div[2]/div[2]/div/div[1]/div[2]/input'

    v_nalici = '//*[@id="f-form"]/div[1]/div[2]/div[2]/label/span'
    polzunok_price = '//*[@id="f-form"]/div[2]/div[2]/div/div[2]/span/span[6]'

    brand_xiaomi = '//*[@id="f-form"]/div[3]/div[2]/div/div[1]/label'
    proc_qualcomm = '//*[@id="f-form"]/div[5]/div[2]/div/div[1]/label'
    storage = '/html/body/main/div[3]/div[2]/div/div/div[2]/div/div/form/div[6]/div[2]/div/div/div[1]/div[1]/input'
    camera = '/html/body/main/div[3]/div[2]/div/div/div[2]/div/div/form/div[7]/div[2]/div/div/div[1]/div[1]/input'
    date_anons = '//*[@id="f-form"]/div[8]/div[2]/div/div/div[1]/div[1]/input'
    color_blue = '//*[@id="f-form"]/div[9]/div[2]/div/div[2]/label'
    screen_gc = '//*[@id="f-form"]/div[10]/div[2]/div/div/div[1]/div[1]/input'

    screen_gc_2 = '//*[@id="f-form"]/div[10]/div[2]/div/div[3]/label'

    button_show = '//*[@id="f-form"]/div[12]/button'
    button_buy = "//a[@data-id='105064']"
    button_place_an_order = '//*[@id="fancybox-container-1"]/div[2]/div[4]/div/div/div[2]/div[3]/button'
    tovar_xiaomi = '//a[@class="b-card2-v2__name"]'

    # Locators 2

    tovar_1 = '/html/body/main/div[3]/div[2]/div/div/div[3]/div[3]/div[1]/div/div[3]/div[3]/div[2]/div[2]/a'
    tovar_2 = '/html/body/main/div[3]/div[2]/div/div/div[3]/div[3]/div[7]/div/div[3]/div[3]/div[2]/div[2]/a'
    tovar_3 = '/html/body/main/div[3]/div[2]/div/div/div[3]/div[3]/div[17]/div/div[3]/div[3]/div[2]/div[2]/a'

    button_continue_shopping = '//a[@class="main__continue"]'

    button_arrange_order = '/html/body/div[13]/div[2]/div[4]/div/div/div[2]/div[3]/button'



    #Getters

    def get_price_min(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price_min)))

    def get_price_max(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price_max)))

    # def get_polzunok_price(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.polzunok_price)))
    # def get_v_nalici(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.v_nalici)))

    def get_brand_xiaomi(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.brand_xiaomi)))

    def get_proc_qualcomm(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.proc_qualcomm)))

    def get_storage(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.storage)))

    def get_camera(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.camera)))

    def get_date_anons(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.date_anons)))

    def get_color_blue(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.color_blue)))

    def get_screen_gc(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.screen_gc)))

    def get_screen_gc_2(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.screen_gc_2)))

    def get_button_show(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_show)))

    def get_tovar_xiaomi(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.tovar_xiaomi)))

    # Getters 2

    def get_tovar_1(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.tovar_1)))

    def get_tovar_2(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.tovar_2)))

    def get_tovar_3(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.tovar_3)))

    def get_button_continue_shopping(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_continue_shopping)))

    def get_button_arrange_order(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_arrange_order)))

    # Actions

    def input_price_min(self, price_min):
        self.get_price_min().clear()
        self.get_price_min().send_keys(price_min)
        print('Ввод минимальной цены')

    def input_price_max(self, price_max):
        self.get_price_max().send_keys(Keys.BACKSPACE * 6)# На сайте баг в поле максимальной цены, поэтому пришлось очистить поле
        self.get_price_max().send_keys(price_max)
        print('Ввод максимальной цены')

    def click_v_nalici(self):
        self.get_v_nalici().click()
        print('Кликаем')

    def click_polzunok_price(self):
        action = ActionChains(self.driver)
        action.click_and_hold(self.get_polzunok_price()).move_by_offset(50,0).release().perform()
        print('Кликаем')

    def click_brand_xiaomi(self):
        self.driver.execute_script("arguments[0].click();", self.get_brand_xiaomi())
        # self.get_brand_xiaomi().click()
        print('Выбираем бренд Xiaomi')


    def click_proc_qualcomm(self):
        # self.driver.execute_script('window.scrollTo(0, 800)')
        self.driver.execute_script("arguments[0].click();", self.get_proc_qualcomm())
        # self.get_proc_qualcomm().click()
        print('Выбираем процессор Qualcom')
        time.sleep(2)

    def input_storage(self, storage):
        # action = ActionChains(self.driver)
        # action.move_to_element(self.get_camera()).perform()
        self.driver.execute_script('window.scrollTo(0, 900)')
        self.get_storage().clear()
        self.get_storage().send_keys(storage)
        print('Выбираем память')

    def click_camera(self):
        # action = ActionChains(self.driver)
        # action.move_to_element(self.get_date_anons())
        # self.driver.execute_script('window.scrollTo(0, 1100)')
        self.driver.execute_script("arguments[0].click();", self.get_camera())
        # self.get_camera().click()
        print('Выбираем 3 камеры')

    def input_date_anons(self, date_anons):
        self.driver.execute_script('window.scrollTo(0, 1300)')
        self.get_date_anons().send_keys(date_anons)
        print('Вводим дату анонсирования')

    def click_color_blue(self):
        self.driver.execute_script("arguments[0].click();", self.get_color_blue())
        # self.driver.execute_script('window.scrollTo(0, 1500)')
        # self.get_color_blue().click()
        print('Выбираем синий цвет')

    def input_screen_gc(self, screen_gc):
        self.driver.execute_script('window.scrollTo(0, 1700)')
        self.get_screen_gc().send_keys(screen_gc)
        print('Вводим частоту обновления экрана')

    def click_screen_gc_2(self):
        self.driver.execute_script('window.scrollTo(0, 1700)')
        self.get_screen_gc_2().click()
        print('Выбираем 120')

    def click_button_show(self):
        self.driver.execute_script("arguments[0].click();", self.get_button_show())
        # self.driver.execute_script('window.scrollTo(0, 2500)')
        # self.get_button_show().click()
        print('Нажимаем на кнопку Показать')

    def click_tovar_xiaomi(self):
        # self.driver.execute_script('window.scrollTo(0, 300)')
        self.driver.execute_script("arguments[0].click();", self.get_tovar_xiaomi())
        # self.get_tovar_xiaomi().click()
        print('Нажимаем на товар Xiaomi')

    # Actions number 2

    def buy_tovar_1(self):
        # self.driver.execute_script('window.scrollTo(0, 300)')
        self.driver.execute_script("arguments[0].click();", self.get_tovar_1())
        # self.get_tovar_xiaomi().click()
        print('Добавляем в корзину первый товар')

    def buy_tovar_2(self):
        # self.driver.execute_script('window.scrollTo(0, 300)')
        self.driver.execute_script("arguments[0].click();", self.get_tovar_2())
        # self.get_tovar_xiaomi().click()
        print('Добавляем в корзину второй товар')

    def buy_tovar_3(self):
        # self.driver.execute_script('window.scrollTo(0, 300)')
        self.driver.execute_script("arguments[0].click();", self.get_tovar_3())
        # self.get_tovar_xiaomi().click()
        print('Добавляем в корзину третий товар')

    def click_continue(self):
        # self.driver.execute_script('window.scrollTo(0, 300)')
        self.driver.execute_script("arguments[0].click();", self.get_button_continue_shopping())
        # self.get_tovar_xiaomi().click()
        print('Нажимаем Продолжить покупки')

    def click_arrange_order(self):
        self.driver.execute_script("arguments[0].click();", self.get_button_arrange_order())
        # self.get_arrange_order().click()
        print('Нажимаем Оформить заказ')

    #Methods

    def filter(self):
        with allure.step('Filter'):
            Logger.add_start_step(method='filter')
            try:
                self.input_price_min('15000')
                self.input_price_max('50000')
                self.click_brand_xiaomi()
                self.click_proc_qualcomm()
                self.input_storage('128')
                self.click_camera()
                self.input_date_anons('2020')
                self.click_color_blue()
                self.input_screen_gc('120')
                #self.click_screen_gc_2()
                self.click_button_show()
                time.sleep(2)
                self.click_tovar_xiaomi()
            except TimeoutException:
                print('Накрылось')
            Logger.add_end_step(url=self.driver.current_url, method='filter')

    def multiple(self):
        with allure.step('Multiple'):
            Logger.add_start_step(method='multiple')
            self.buy_tovar_1()
            self.click_continue()
            self.buy_tovar_2()
            self.click_continue()
            self.buy_tovar_3()
            time.sleep(2)
            self.click_arrange_order()
            self.assert_url('https://quke.ru/order')
            Logger.add_end_step(url=self.driver.current_url, method='multiple')


    def vvod_price(self):
        with allure.step('Vvod price'):
            self.input_price_min('15000')
            self.input_price_max('50000')
            time.sleep(2)


    def vvv(self):
        with allure.step('Vvv'):
            self.click_v_nalici()
            time.sleep(3)

    def polzunok(self):
        with allure.step('Polzunok'):
            self.click_polzunok_price()
            time.sleep(3)

