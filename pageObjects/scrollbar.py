from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

class Scrollbar:
    def __init__(self, driver):
        self.driver = driver

    def scrollbar_test(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        
        scrollbars_url = wait.until(EC.element_to_be_clickable((By.XPATH, "//div/h3/a[.='Scrollbars']")))
        scrollbars_url.click()
        time.sleep(2)
        
        #wait for the scrollable div to load
        scroll_box = wait.until(EC.presence_of_element_located((By.XPATH, "(//div)[3]")))
        
        
        #locate the hidden button and scroll into view
        hiding_button = driver.find_element(By.ID, "hidingButton")
        driver.execute_script("arguments[0].scrollIntoView();", hiding_button)
        
        #wait for it to become clickable
        wait.until(EC.element_to_be_clickable((By.ID, "hidingButton")))
        print("Clicking on the hiding button")
        hiding_button.click()
        time.sleep(2)