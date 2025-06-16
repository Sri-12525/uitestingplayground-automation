from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pyperclip
import os

class ShadowElements:
    def __init__(self, driver):
        self.driver = driver
        
    def expand_shadow_element(self, element):
        driver = self.driver
        return driver.execute_script("return arguments[0].shadowRoot", element)
    
    def shadow_elements_test(self):
        driver = self.driver
        
        wait = WebDriverWait(driver, 10)
        
        #launching the shadow elements test url
        shadowDOM_url = wait.until(EC.element_to_be_clickable((By.XPATH, "//div/h3/a[.='Shadow DOM']")))
        shadowDOM_url.click()
        time.sleep(2)
        
        #access the shadow host(guid generator)
        shadow_host = driver.find_element(By.CSS_SELECTOR, "guid-generator")
        
        #access the shadow root
        shadow_root = self.expand_shadow_element(shadow_host)
        
        #1.click the generate button
        generate_button = shadow_root.find_element(By.ID, "buttonGenerate")
        print("The Shadow DOM page is opened now -- ")
        generate_button.click()
        print("✅Clicked on the settings button.")
        time.sleep(1)
        
        #click the copy to clipboard button
        copy_button = shadow_root.find_element(By.ID, "buttonCopy")
        copy_button.click()
        print("✅Clicked on the copy button.")
        #wait for a second to check what happens
        time.sleep(1)
        
        #wait for a second to check what happens
        time.sleep(1)
        guid_box = shadow_root.find_element(By.ID, "editField")
        guid_box_value = guid_box.get_attribute("value")
        print(f"Generated GUID :{guid_box_value}")
        
        #take screenshots
        screenshots_dir = "shadow_elements_screenshots"
        os.makedirs("shadow_elements_screenshots", exist_ok = True)
        
        timestamp = time.strftime("%y_%m_%d-%H-%M-%S")
        filename = f"shadow_elements_screenshots/screenshot-{timestamp}.png"
        image = shadow_root.find_element(By.ID, "editField")
        image.screenshot(filename)
        
        time.sleep(2)
        
        clipboard_value = pyperclip.paste()
        print(f"The cipboard value : {clipboard_value}")

        assert guid_box_value == clipboard_value, "❌No, values don't match"

        time.sleep(2)
        
        
        