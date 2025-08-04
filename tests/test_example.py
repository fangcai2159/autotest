import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

from conftest import driver
# def test_google_search(driver):
#     driver.get("https://www.google.com")
#     search_box = driver.find_element("name", "q")
#     search_box.send_keys("pytest selenium")
#     search_box.submit()
#     try:
#       wait = WebDriverWait(
#           driver,
#           timeout=10,
#           poll_frequency=0.5,  # 每0.5秒检查一次
#           ignored_exceptions=[NoSuchElementException]  # 忽略这些异常
#       )

#       wait.until(EC.title_contains("pytest selenium"))
#       wait.until(EC.element_located_to_be_selected((By.NAME, "q")))
#     except TimeoutException:
#         pytest.fail("Timeout waiting for Google search results")
#     assert "pytest selenium" in driver.title


def test_python_home_download(driver):
    driver.get("https://www.python.org/")
    wait = WebDriverWait(driver, 10)
    # Step 1: 定位 Downloads 菜单
    downloads_menu = wait.until(
        EC.visibility_of_element_located((By.XPATH, '//li[@id="downloads"]/a[@href="/downloads/"and text()="Downloads"]'))
    )
    # Step 2: 鼠标悬停
    actions = ActionChains(driver)
    actions.move_to_element(downloads_menu).perform()

    # Step 3: 等待下拉菜单中的第一个选项出现
    
    first_dropdown_item = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#downloads ul.menu li a"))
    )

    # Step 4: 点击第一个选项
    first_dropdown_item.click()

    # 可选：检查是否跳转到 All Releases 页面
    assert "Download Python | Python.org" in driver.title