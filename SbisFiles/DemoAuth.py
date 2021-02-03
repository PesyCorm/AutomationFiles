from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

"""
Скрипт переходит в нужный сервис на странице https://online.sbis.ru/auth/?ret=%2F&tab=demo
В качестве аргументов передается драйвер и строковое значение сервиса (с соблюдением регистра).
Если при попытке войти появляется поле капчи, страница перезагружается и пытается войти в сервис еще раз;
    *перезагружается не более 3-ех раз
    *если кол-во перезагрузок достигло 3-ех — возбуждается исключение
"""
class AuthPage:

    def __init__(self, driver, requested_page):

        self.driver = driver
        self.requested_page = requested_page

    def page_selection(self):

        try:
            counter_reload = 0
            while True:

                services = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_all_elements_located(
                        (By.CLASS_NAME, "demo-Auth__item-title")
                    )
                )

                for el in services:
                    if self.requested_page in el.text:
                        el.click()
                        break
                time.sleep(2)

                if counter_reload == 2:
                    print(f"Пытались открыть страницу {counter_reload + 1} раз(а), мешает поле капчи. Попробуйте позже")
                    raise SystemExit("the captcha field interferes")

                elif self.driver.find_elements_by_name("input"):
                    print("На странице поле капчи! Обновление...")
                    self.driver.refresh()
                    counter_reload += 1
                else:
                    break

        except Exception as e:
            raise e