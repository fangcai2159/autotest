import pytest
from pages.baidu_home import BaiduHomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

@pytest.mark.parametrize("keyword", ["Selenium", "Python", "ChatGPT"])
def test_baidu_search(driver, keyword):
    home = BaiduHomePage(driver)
    home.load()
    home.enter_search_text(keyword)
    home.click_search()
    
    # 简单断言：检查标题是否包含关键字
    try:
      wait = WebDriverWait(
          driver,
          timeout=30,
          poll_frequency=0.5,  # 每0.5秒检查一次
          ignored_exceptions=[NoSuchElementException]  # 忽略这些异常
      )

      wait.until(EC.title_contains(keyword))
    except TimeoutException:
        pytest.fail("Timeout waiting for Baidu search results")
    assert keyword.lower() in driver.title.lower()
