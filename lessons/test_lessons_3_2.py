from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class Test_Proverka(unittest.TestCase):
    def test_registr_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome(executable_path='C:\\Users\\Home\PycharmProjects\\resource\\chromedriver.exe')
        browser.get(link)



        first_name = browser.find_element(By.XPATH, '//input[@placeholder="Input your first name"]')
        first_name.send_keys('Piter')

        last_name = browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
        last_name.send_keys('Parker')

        email = browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
        email.send_keys('555@mail.ru')

        # phone = browser.find_element(By.XPATH, '//input[@placeholder="Input your phone:"]')
        # phone.send_keys('7595656565')
        #
        # address = browser.find_element(By.XPATH, '//input[@placeholder="Input your address:"]')
        # address.send_keys('New-York')

        # Отправляем заполненную форму
        button = browser.find_element(By.XPATH, '//button[@class="btn btn-default"]')
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Fuck")


        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(3)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_registr_2(self):
        self.link = "http://suninjuly.github.io/registration2.html"
        self.browser = webdriver.Chrome(
            executable_path='C:\\Users\\Home\PycharmProjects\\resource\\chromedriver.exe')
        self.browser.get(self.link)

        self.first_name = self.browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[1]/input')
        self.first_name.send_keys('Piter')

        self.last_name = self.browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
        self.last_name.send_keys('Parker')

        self.email = self.browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
        self.email.send_keys('555@mail.ru')

        # self.phone = self.browser.find_element(By.XPATH, '//input[@placeholder="Input your phone:"]')
        # self.phone.send_keys('7595656565')
        #
        # self.address = self.browser.find_element(By.XPATH, '//input[@placeholder="Input your address:"]')
        # self.address.send_keys('New-York')

        # Отправляем заполненную форму
        self.button = self.browser.find_element(By.XPATH, '//button[@class="btn btn-default"]')
        self.button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        self.welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        self.welcome_text = self.welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", self.welcome_text, "Fuck")

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(3)
        # закрываем браузер после всех манипуляций
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()