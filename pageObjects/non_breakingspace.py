from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import pytest
import os


class NonBreakingSpace:
    def __init__(self, driver):
        self.driver = driver
        
    def nonbreakingspace_test(self):
        driver = self.driver
        
        wait = WebDriverWait(driver,10)
        
        non_breakingspace_url = wait.until(EC.element_to_be_clickable((By.XPATH, "//div/h3/a[.='Non-Breaking Space']")))
        non_breakingspace_url.click()
        time.sleep(2)
        print("We are on the Non-Breaking Space page --")
        
        button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='My Button']")))
        button.click()
        print("Clicked on the 'My Button' button")
        time.sleep(2)