import datetime
class Base:
    def __init__(self, driver):
        self.driver = driver



    """Method get current url """

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Current url {get_url}')

    """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result, "URL не совпадают"
        print('URL совпадают')

    """Method assert word"""

    def assert_word(self, word, result):  # Добавляем 3 обязательных атрибута
        value_word = word.text  # считываем текст
        assert value_word == result  # сравниваем значения
        print('Good value word')

    """Method Screenshot"""

    def get_screenshot(self):
        # now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        now_date = str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
        name_screenshot = f'screenshot {now_date} .png'
        self.driver.save_screenshot('C:\\Users\\Home\\PycharmProjects\\quke\\screen\\' + name_screenshot)



