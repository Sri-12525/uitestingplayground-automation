from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time, os


class AutoWait:
    def __init__(self, driver):
        self.driver = driver
        
    def auto_wait_test(self, element, applyTime):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        
        #launching the auto wait feature url
        autowait_url = wait.until(EC.element_to_be_clickable((By.XPATH, "//div/h3/a[.='Auto Wait']")))
        autowait_url.click()
        
        #check if page is successfully launched
        wait.until(EC.element_to_be_clickable((By.ID, "element-type")))
        comboBox = Select(driver.find_element(By.ID, "element-type"))
        print("Successfully launched the auto wait url--")
        comboBox.select_by_visible_text("Input")
        print("Selected 'Input' from dropdown..")
        
        
        #check a checkbox to set the behaviour of the element selected
        checkboxes = driver.find_elements(By.XPATH, "//ul[@class='list-unstyled indented-right']/li")
        print("checkboxes list is created..")
        # for elem in checkboxes:
        #     print(elem.text)
            
            
        for elem in checkboxes:
            elem_label = elem.find_element(By.XPATH, ".//label")
            if element in elem_label.text:
                checkbox = elem.find_element(By.XPATH, ".//input")
                checkbox.click()
                print(f"Selected the option: {element}")
                time.sleep(2)
                
                if applyTime == 3:
                    applybttn = wait.until(EC.element_to_be_clickable((By.ID, "applyButton3")))
                elif applyTime == 5:
                    applybttn = wait.until(EC.element_to_be_clickable((By.ID, "applyButton5")))
                else :
                    applybttn = wait.until(EC.element_to_be_clickable((By.ID, "applyButton10")))   
                applybttn.click()
                time.sleep(1)
                
                #check for the 'Target' message
                target_mssg = wait.until(EC.visibility_of_element_located((By.ID, "opstatus")))
                
                print(f"The message displayed after clicking on the apply button : {target_mssg.text}")
                time.sleep(1)
                
                #check if we are able to provide values to the input box
                try:
                    time.sleep(applyTime)
                    inputBox = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='target']")))
                    # inputBox.click()
                    inputBox.send_keys("Hello World !! ")
                except Exception as e:
                    print(f"Element is not interactable: {e}")
                    
                
                time.sleep(1)
                
                #take screenshots
                image = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "section")))
                screenshots_dir = "autowait_screenshots"
                os.makedirs(screenshots_dir, exist_ok = True)
                timestamp = time.strftime("%y_%m_%d-%H-%M-%S")
                filename = f"{screenshots_dir}/screenshot_{timestamp}.png"
                image.screenshot(filename)
                break
                
        time.sleep(2)
        
        
        
        