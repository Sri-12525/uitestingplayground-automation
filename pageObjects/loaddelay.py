from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

class LoadDelay:
    def __init__(self, driver):
        self.driver = driver
        
    def load_delays(self):
        driver = self.driver
        
        print("Launching load delay url")
        
        wait = WebDriverWait(driver, 10)
        
        load_delay_url = wait.until(EC.element_to_be_clickable((By.XPATH, "//div/h3/a[.='Load Delay']")))
        load_delay_url.click()
        
        
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary")))
        print("Load Delay page is successfully loaded !! ")
        
        button.click()
        print("Successfully clicked on the button !! ")