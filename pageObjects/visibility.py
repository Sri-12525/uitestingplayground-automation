from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
import os

class Visibility:
    def __init__(self, driver):
        self.driver = driver
        
    def visibility_test(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        
        visibility_url = wait.until(EC.element_to_be_clickable((By.XPATH, "//div/h3/a[.='Visibility']")))
        visibility_url.click()
        time.sleep(2)

        hide_button = wait.until(EC.element_to_be_clickable((By.ID,"hideButton")))
        hide_button.click()
        print("Clicked on the hide button !")
        
        time.sleep(2)
        
        buttons_to_check = {
            "removedButton":"removedButton",
            "zeroWidthButton":"zero_width_button",
            "overlappedButton":"overlapped_button",
            "transparentButton":"opacity_button",
            "invisibleButton":"visibility_button",
            "notdisplayedButton":"display_button",
            "offscreenButton":"offscreen_button"      
        }
        

        for btn_id, label in buttons_to_check.items():
            try:
                button = driver.find_element(By.ID, btn_id)
                if button.is_displayed():
                    print(f"❌{label} is VISIBLE.")
                else:
                    print(f"✅{label} is NOT VISIBLE (but still present in DOM).")
            except Exception as e:
                print(f"✅{label} has been removed from the DOM.")
                    
        time.sleep(2)
        
        #take screenshots
        screenshots_dir = "visibility_feature_screenshots"
        os.makedirs("visibility_feature_screenshots", exist_ok=True)
        
        timestamp = time.strftime("%y_%m_%d-%H_%M_%S")
        filename = f"visibility_feature_screenshots/screenshot{timestamp}.png"
        
        image = driver.find_element(By.XPATH, "//tbody")
        image.screenshot(filename)
        print(f"Screenshots saved as {filename} in visibility_feature_screenshots")
        time.sleep(2)

