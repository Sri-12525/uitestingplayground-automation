from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
import os

class ProgressBar:
    def __init__(self, driver):
        self.driver = driver
        
    def progressbar_test(self, stopvalue):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        
        progressbar_url = wait.until(EC.element_to_be_clickable((By.XPATH, "//div/h3/a[.='Progress Bar']")))
        progressbar_url.click()
        time.sleep(2)
        
        
        start_button = wait.until(EC.visibility_of_element_located((By.ID, "startButton")))
        print("Successfully launched Progress Bar url --")
        start_button.click()
        print("Clicked on the start button ..")
        time.sleep(2)
        
        progress = driver.find_element(By.ID, "progressBar")

        #loop to watch for stopvalue
        current = 0
        
        while True:
            value = progress.get_attribute("aria-valuenow")
            if value:
                current = int(value)
                print(f"Progress: {current}%")
                if current >= stopvalue:
                    break
            time.sleep(0.01)  #keep it light and fast
            
            
        stop_button = wait.until(EC.element_to_be_clickable((By.ID, "stopButton")))
        stop_button.click()
        print(f"Clicked on stop button at {current}%")
        time.sleep(2)
        
        result = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='content']/p[@id='result']")))
        print(f"The result is as below : {result.text}")
        
        time.sleep(2)
        
        #take screenshots of current progress
        screenshots_dir = "screenshots"
        os.makedirs("screenshots", exist_ok= True)
        timestamp = time.strftime("%Y_%m_%d-%H_%M_%S")
        image = driver.find_element(By.CLASS_NAME, "container")
        filename = f"screenshots/progress_bar{timestamp}.png"
        image.screenshot(filename)
        print(f"Screenshot of the progress saved as {filename}")
        
        time.sleep(2)
        
