import linecache
import sys
from termcolor import cprint
from art import text2art
from rich.console import Console
from selenium.webdriver import ChromeOptions
from selenium import webdriver
from time import sleep




def switch_to_window_title(driver, title):
    for _ in range(40):
        windows = driver.window_handles
        desired_window_title = title
        for window in windows:
            # Переключение на окно
            driver.switch_to.window(window)
            # Проверка заголовка окна
            if driver.title == desired_window_title:
                return
        sleep(0.5)


def get_chromedriver():
    options = ChromeOptions() 
    options.add_argument("--disable-blink-features=AutomationControlled") # отключаем режим webdriver
    options.add_argument("--log-level=3") # отключаем вывод логов webdriver
    options.add_extension('Compass Wallet for Sei 0.9.2.0.crx')
    # options.add_argument('--disable-gpu')
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(90)
    return driver

def get_error_message():
    exc_type, exc_value, exc_traceback = sys.exc_info()
    file_name = exc_traceback.tb_frame.f_code.co_filename
    line_number = exc_traceback.tb_lineno
    line = linecache.getline(file_name, line_number).strip()
    return f"{exc_type.__name__}\nФайл: {file_name}, строка {line_number}: {line}"

def print_welcome():
    cprint(text2art("SLON", space=10), 'green', end='')
    cprint('##########################################################', 'white')
    cprint(' #############', 'white', end='')
    cprint(' https://t.me/SlonSoftware ', 'green', end='')
    cprint('################ ', 'white')
    cprint('##########################################################', 'white', end='\n\n')


if __name__ == '__main__':
    print_welcome()