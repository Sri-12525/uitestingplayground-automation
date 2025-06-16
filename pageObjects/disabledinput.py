from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os


class DisabledInput:
    def __init__(self, driver):
        self.driver = driver
        
    def disabled_input(self):
        driver = self.driver
        
        wait = WebDriverWait(driver, 10)
        
        #launching the disabled input url
        disabled_input_url = wait.until(EC.element_to_be_clickable((By.XPATH, "//div/h3/a[.='Disabled Input']")))
        disabled_input_url.click()
        
        time.sleep(2)
        
        enabled_button = wait.until(EC.element_to_be_clickable((By.ID, "enableButton")))
        self.take_screenshots("before-click")
        enabled_button.click()
        time.sleep(1)
        #take screenshots
        self.take_screenshots("after-click")
        
        input_Box = wait.until(EC.element_to_be_clickable((By.ID, "inputField")))
        print("The disabled input feature page has loaded successfully ...")
        input_Box.click()
        input_Box.send_keys("Hello World -- testing input field...")
        time.sleep(1)
        #take screenshots
        self.take_screenshots("after-input")
        
        time.sleep(2)
        
    def take_screenshots(self,name):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        
        #take screenshots
        image = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "section")))
        screenshots_dir = "disabled_input_screenshots"
        os.makedirs(screenshots_dir, exist_ok = True)
        timestamp = time.strftime("%y_%m_%d-%H-%M-%S")
        filename = f"{screenshots_dir}/{name}_{timestamp}.png"
        image.screenshot(filename)