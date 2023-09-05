from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
class BasePage:

	def __init__(self, driver):
		self.driver = driver
		self.base_url = "https://mortgage.finuslugi.ru/"


	def find_element(self, locator, time=10):
		try:
			element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'Cant find element by locator {locator}')
		except:
			logging.exception('Find element exception')
			element = None
		return element


	def go_to_site(self):
		try:
			start_browsing = self.driver.get(self.base_url)
		except:
			logging.exception('Exception with open site')
			start_browsing = None
		return start_browsing
