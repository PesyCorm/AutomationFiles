from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .Common.ClickElem import waiting_for_clickability as WC

"""
В качестве аргументов принимает драйвер и запрашиваемый из "аккордеона" раздел (с соблюдением регистра).
Не отвечает за навигацию по субменю.
"""
class AccordSectionSelector:

    def __init__(self, driver, selection):
        self.driver = driver
        self.selection = selection

    def accord_section_selector(self):

        accord_list = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, ".NavigationPanels-Accordion__title_level-1")
            )
        )

        for el in accord_list:
            if self.selection in el.text:
                WC(el, 30)
                break
