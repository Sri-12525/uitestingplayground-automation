from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os

class AnimatedButton:
    def __init__(self, driver):
        self.driver = driver
    
    def animatedbutton_test(self):
        driver = self.driver
        
        wait = WebDriverWait(driver, 10)
        
        animatedbttn_url = wait.until(EC.visibility_of_element_located((By.XPATH, "//div/h3/a[.='Animated Button']")))
        animatedbttn_url.click()
        
        time.sleep(2)
        
        #click on the start animation button
        start_animationbttn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@onclick='startAnimation()']")))
        start_animationbttn.click()  
        
        time.sleep(2)
        
        #wait for the 'Moving Target' button to stop spinning
        #this means waiting until the class 'spin' is removed
        def wait_for_animation_to_end(driver):
            button = driver.find_element(By.ID, "movingTarget")
            return "spin" not in button.get_attribute("class")
        
        WebDriverWait(driver, 15).until(wait_for_animation_to_end)
        print("✅Animation ended. Button is stable.")
        
        #step 3: click on the 'Moving Target' button
        moving_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-primary']")))
        moving_button.click()
        print("✅Clicked on 'Moving Target'.")

        #step 4: validate that the class at the time of click did not include 'spin'
        final_class = moving_button.get_attribute("class")
        assert "spin" not in final_class, f"❌Button still has animation class: {final_class}" 
        print("✅Test passed: Button was clicked without animation.")       
        
        image = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "container")))
        screenshots_dir = "animated_button_screenshots"
        os.makedirs(screenshots_dir, exist_ok= True)
        timestamp = time.strftime("%y_%m_%d-%H-%M-%S")
        filename = f"{screenshots_dir}/screenshot_{timestamp}.png"
        image.screenshot(filename)
        time.sleep(2)