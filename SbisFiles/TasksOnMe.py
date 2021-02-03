from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
Не универсальный скрипт, нажимает "Выполнить план" для Главного Сергея. На вход принимает драйвер.
Предварительно закрывает все всплывающие уведомления на странице.
"""
class TasksPageManagement:

	def __init__(self, driver):
		self.driver = driver

	def close_blocks(self):
		try:
			block_close = WebDriverWait(self.driver, 10).until(
				EC.presence_of_all_elements_located(
					(By.CLASS_NAME, "controls-Button__close__icon_link-theme_default")
					)
				)
			if block_close:
				for el in block_close:
					el.click()
		except:
			pass

	def exec_plan_click(self):
		plan_click = self.driver.find_elements_by_tag_name("span")
		for el in plan_click:
			if "Выполнить" in el.text:
				el.click()
				break