from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os

class Click:
    def __init__(self, driver):
        self.driver = driver
        
    def clicktest(self):
        driver = self.driver
        
        wait = WebDriverWait(driver, 10)
        click_url = wait.until(EC.element_to_be_clickable((By.XPATH, "//div/h3/a[.='Click']")))
        click_url.click()
        
        #######click on the button on the page
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary")))
        print("Successfully launched the click feature page...")
        button.click()
        time.sleep(1.5)
        
        #######verify color change
        color = driver.execute_script("return window.getComputedStyle(arguments[0]).backgroundColor;", button)
        print(f"Button color after click: {color}")
        time.sleep(1)
        
        #######assert to check if its the color we expect
        assert color == "rgb(33, 136, 56)", "The colors don't match ❌"
        
        
        #######take screenshot to see what happens when we click on this button
        image = driver.find_element(By.TAG_NAME, "section")
        screenshots_dir = "click_screenshots"
        os.makedirs(screenshots_dir, exist_ok = True)
        
        timestamp = time.strftime("%y_%m_%d-%H:%M:%S")
        filename = f"{screenshots_dir}/screenshots_{timestamp}.png"
        image.screenshot(filename)
        
        