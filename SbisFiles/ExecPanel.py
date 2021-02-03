from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

"""
Скрипт предоставляет доступ к основным элементам на панелях типа "Выполнить план":
	.button_executed_click() нажимает кнопку "План выполнен"
	.button_not_executed_click() нажимает кнопку "План не выполнен"
	.remap_button_click() нажимает кнопку "Переназначить"
	.button_close_panel() закрывает панель
	.text_enter_area() в качестве аргумента принимает текст и вводит его в текстовое поле на панели
"""
class ControlExecPanel:

	def __init__(self, driver):
		self.driver = driver
		self.buttons = WebDriverWait(self.driver, 10).until(
		        EC.presence_of_all_elements_located(
		        	(By.CSS_SELECTOR, ".NavigationPanels-Accordion__title_level-1")
		        	)
		        )

	def button_executed_click(self):
		for el in self.buttons:
			if "План выполнен" in el.text:
				el.click()
				break

	def button_not_executed_click(self):
		for el in self.buttons:
			if "План не выполнен" in el.text:
				el.click()
				break

	def remap_button_click(self):
		for el in self.buttons:
			if "Переназначить" in el.text:
				el.click()
				break

	def button_close_panel(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(
				(By.CLASS_NAME, "controls-Button__close__wrapper.controls-Button__close_toolButton.controls-Button__close_toolButton-theme_default.controls-Button__close_toolButton_transparent-theme_default")
			)
		).click()

	def text_enter_area(self, text):
		text_area = WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(
				(By.CLASS_NAME, "controls-Field.controls-InputBase__nativeField_theme_default.controls-Area__realField.controls-InputBase__nativeField_caretFilled_theme_default.controls-InputBase__nativeField_hideCustomPlaceholder")
				)
			)
		text_area.send_keys(text)