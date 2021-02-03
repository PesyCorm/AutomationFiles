from SbisFiles import AuthPage, \
	AccordSectionSelector as AccSelector, \
	TasksSectionSelector as TsSelector, \
	TasksPageManagement as TsManage, \
	ControlExecPanel as CPanel

from ApiFiles.GetAPI import ReqAPI
from CommonFiles import DriverStarter
import time

"""
Скрипт - пример автоматизации определенного пути:
	1)Запуск драйвера для браузера Chrome и переходим на страницу "https://online.sbis.ru/auth/?ret=%2F&tab=demo"
	2)Переходим в сервис "Отчетность"
		Страница перезагружается до 3-ех раз, если есть капча
	3)Открываем субменю для раздела "Задачи"
	4)Переходим в "Задачи на мне"
	5)Закрываем блоки уведомлений и нажимает "Выполнить план"
		Открывается панель выполнения
	6)Вводим в поле панели текст полученный по API с https://fakerapi.it/api/v1/
	7)Нажимаем "План выполнен"
	8)Браузер закрывается
Более подробно функции описаны внутри своих файлов.
"""
class TestSbis:

	def __init__(self, driver):
		self.driver = driver
		self.text_from_api = ReqAPI("texts", 1, "ru_RU", _characters=250).get_method()

	def test_method(self):
		AuthPage(self.driver, "Отчетность").page_selection()

		time.sleep(3)
		AccSelector(self.driver, "Задачи").accord_section_selector()

		TsSelector(self.driver, "Задачи на мне").tasks_section_selector()

		TsManage(self.driver).close_blocks()
		TsManage(self.driver).exec_plan_click()

		CPanel(self.driver).text_enter_area(self.text_from_api[0]["content"])
		CPanel(self.driver).button_executed_click()


if __name__ == "__main__":
	with DriverStarter("https://online.sbis.ru/auth/?ret=%2F&tab=demo") as DS:
		TestSbis(DS).test_method()