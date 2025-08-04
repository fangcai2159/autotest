from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class BaiduHomePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.search_input = (By.ID, "kw")
        self.search_button = (By.ID, "su")

    def load(self):
        self.driver.get("https://www.baidu.com")

    def enter_search_text(self, text):
        self.driver.find_element(*self.search_input).send_keys(text)

    def click_search(self):
        self.driver.find_element(*self.search_button).click()
