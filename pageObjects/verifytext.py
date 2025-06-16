from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

class VerifyText:
    def __init__(self, driver):
        self.driver = driver
        
    def verify_text(self):
        driver = self.driver
        
        wait = WebDriverWait(driver, 10)
        
        verify_text_url = wait.until(EC.visibility_of_element_located((By.XPATH, "//div/h3/a[.='Verify Text']")))
        verify_text_url.click()
        time.sleep(2)
        
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div/span[normalize-space(.)= 'Welcome UserName!']")))
        element = driver.find_element(By.XPATH, "//div/span[normalize-space(.)= 'Welcome UserName!']")
        
        assert element.is_displayed(), "Element with expected text not found or not visible."
        print("Text verified successfully: ", element.text)
        time.sleep(2)