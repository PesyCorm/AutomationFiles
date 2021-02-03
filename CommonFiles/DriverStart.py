from selenium import webdriver

class DriverStarter:

	def __init__(self, url):
		self.url = url

	def __enter__(self):
		self.driver = webdriver.Chrome()
		self.driver.get(self.url)
		return self.driver

	def __exit__(self, type, value, traceback):
		self.driver.quit()