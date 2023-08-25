



from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait



driver = webdriver.Firefox(executable_path='C:\\Users\\Home\PycharmProjects\\resource\\geckodriver.exe')
driver.get("https://stepik.org/lesson/25969/step/8")














# def func_decorator(func):
#     def wrapper(*args, **kwargs): # *args, **kwargs - универсальный метод, если аргументов не будет, то ошибка не всплывёт
#         print("----что-то делаем перед вызовом фнкции -----")
#         func(*args, **kwargs)
#         print("----что-то делаем после вызова функции -----")
#     return wrapper
#
# def some_func():
#     print("аррарар")
#
# some_func = func_decorator(some_func)
# some_func()

# text = "This message is so long that it requires" \
#         "more than lines" \
#         "And more lines may be needed."
#
# print(text)