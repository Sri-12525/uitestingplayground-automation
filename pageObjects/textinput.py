from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

class TextInput:
    def __init__(self, driver):
        self.driver = driver
        
    def text_input(self, input_text):
        driver = self.driver
        
        print("Launching text input url")
        
        wait = WebDriverWait(driver, 10)
        
        textinput_url = wait.until(EC.element_to_be_clickable((By.XPATH, "//div/h3/a[.='Text Input']")))
        textinput_url.click()
        
        input_box = wait.until(EC.element_to_be_clickable((By.ID, "newButtonName")))
        print("Text Input page is successfully loaded !! ")
        input_box.click()
        print("Clicked on the input box successfully!")
        input_box.send_keys(input_text)
        time.sleep(2)
        button = wait.until(EC.element_to_be_clickable((By.ID, "updatingButton")))
        button.click()
        print(button.text)
        
        time.sleep(2)
        