from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
Скрипт отвечает за навигацию по субменю в разделе аккордеона "Задачи".
В качестве аргументов принимает драйвер и запрашиваемый раздел.
"""
class TasksSectionSelector:

	def __init__(self, driver, section):
		self.driver = driver
		self.section = section

	def tasks_section_selector(self):
		if self.section == "Задачи на мне":
			WebDriverWait(self.driver, 10).until(
		        EC.presence_of_element_located(
		        	(By.CLASS_NAME, "NavigationPanels-SubMenu__headTitle.NavigationPanels-SubMenu__title-with-separator.NavigationPanels-Accordion__prevent-default")
		        	)
		        ).click()
		else:
			f_sect = WebDriverWait(self.driver, 10).until(
				EC.presence_off_all_elements_located(
					(By.CSS_SELECTOR, ".NavigationPanels-SubMenu__lvl-3")
					)
				)
			for el in f_sect:
				if self.section in el.text:
					el.click()
					break