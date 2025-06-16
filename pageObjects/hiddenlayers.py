from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

class HiddenLayers:
    def __init__(self, driver):
        self.driver = driver
        
    def hidden_layers(self):
        driver = self.driver
        
        wait = WebDriverWait(driver, 10)
        
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='row']/div/h3/a[.='Hidden Layers']")))
        driver.find_element(By.XPATH, "//div[@class='row']/div/h3/a[.='Hidden Layers']").click()
        
        print("Clicking on the button for the 1st time ..")
        button = wait.until(EC.visibility_of_element_located((By.XPATH, "//div/button")))
        button.click()
        
        time.sleep(1)
        
        #after clicking for the first time, the button turns blue, so--
        clicked_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div/button[@id='blueButton']")))
        print("Clicking on the button for a 2nd time ..")
        clicked_button.click()
        print("Successfully clicked on the already clicked button !")
        time.sleep(5)