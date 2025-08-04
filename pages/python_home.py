from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains

class PythonHomePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.download_button = (By.XPATH, '//li[@id="downloads"]/a[@href="/downloads/"and text()="Downloads"]')

    def load(self):
        self.driver.get("https://www.python.org/")

    def enter_search_text(self, text):
        self.ele = self.driver.find_element(*self.download_button)

    def hover_download_button(self, element):
        ActionChains(self.driver).move_to_element(element).click().perform()
