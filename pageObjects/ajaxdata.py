from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

class AJAXData:
    def __init__(self, driver):
        self.driver = driver
        
    def ajax_data(self):
        driver = self.driver
        
        print("Launching ajax data url")
        
        wait = WebDriverWait(driver, 10)
        
        ajaxdata_url = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='row']/div/h3/a[.='AJAX Data']")))
        ajaxdata_url.click()
        
        
        button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='ajaxButton']")))
        print("AJAX data url is successfully loaded !! ")
        
        button.click()
        print("Successfully clicked on the button !! ")
        
        wait = WebDriverWait(driver, 30)
        success_mssg = wait.until(EC.visibility_of_element_located((By.XPATH, "//div/p[@class='bg-success']")))
        print(success_mssg.text)