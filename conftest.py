from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

@pytest.fixture(scope = "class")
def setup(request):
        driver = webdriver.Chrome()
        print("Testing started .. ")
        driver.get("http://uitestingplayground.com/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        wait = WebDriverWait(driver, 10)
        request.cls.driver = driver
        yield driver
        print("Testing ended ..")
        
        