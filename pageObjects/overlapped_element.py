from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


class OverlappedElements:
    def __init__(self, driver):
        self.driver = driver
        
    def overlappedelems(self, name):
        driver = self.driver
        
        wait = WebDriverWait(driver, 10)
        overlapped_element_url = wait.until(EC.element_to_be_clickable((By.XPATH, "//div/h3/a[.='Overlapped Element']")))
        overlapped_element_url.click()
        time.sleep(2)
        
        name_input_box = driver.find_element(By.ID, "name")
        driver.execute_script("arguments[0].scrollIntoView(true);",name_input_box )
        time.sleep(1)
        
        name_input_box.click()
        time.sleep(0.5)
        name_input_box.send_keys(name)
        
        assert name_input_box.get_attribute("value") == "Sri", "❌Incorrect name"
        
        time.sleep(3)
        