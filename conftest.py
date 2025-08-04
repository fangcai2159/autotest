import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # 可去掉 headless 查看浏览器动作
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# def wait_for_element(driver, by, value, timeout=10):
#     """等待元素出现的通用方法"""
#     if not isinstance(by, tuple):
#         by = (by, value)
#     if not isinstance(value, str):
#         value = str(value)
#     if not isinstance(timeout, (int, float)):
#         timeout = 10
#     try:
#         WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))
#     except TimeoutException:
#         pytest.fail(f"Element {value} not found within {timeout} seconds")
#     return driver.find_element(by, value)
