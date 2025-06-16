from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import pytest
import os


class MouseOver:
    def __init__(self, driver):
        self.driver = driver
        
    def mouseover_test(self, count):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        actions = ActionChains(driver)
        clickcount = 0
        
        mouseover_url = driver.find_element(By.XPATH, "//div/h3/a[.='Mouse Over']")
        mouseover_url.click()
        time.sleep(2)
        
        
        for i in range(2):
            #hover again before every click (to get the latest element)
            target = wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Click me']")))
            actions.move_to_element(target).perform()
            time.sleep(0.5) #let DOM update
            fresh_target = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Click me']")))
            fresh_target.click()
            
        #verify count for first link
        click_text = driver.find_element(By.XPATH, "//a[text()='Click me']").text
        print(f"first link clicked : {click_text.strip()}")
        
        
        #take screenshots
        screenshots_dir = "mouseover_screenshots"
        os.makedirs("mouseover_screenshots", exist_ok=True)
        
        #set the file name pattern for the screenshots
        timestamp = time.strftime("%y_%m_%d-%H-%M-%S")
        filename = f"mouseover_screenshots/screenshot{timestamp}.png"
        
        image = driver.find_element(By.XPATH, "(//div[@class='container'])[1]")
        image.screenshot(filename)
        
        #second section : 'link button'
        print("Handling second link ('Link Button')")
        
        for i in range(2):
            #hover o
            target2 = driver.find_element(By.XPATH, "//a[text()='Link Button']")
            actions.move_to_element(target2).perform()
            time.sleep(0.5)
            fresh_target2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Link Button']")))
            fresh_target2.click()
            
        #verify count for 2nd link
        click_text2 = driver.find_element(By.ID, "clickButtonCount").text
        print(f"Second link clicked for {click_text2.strip()} times.")
        
        time.sleep(2)
        
        #take screenshots
        screenshots_dir = "mouseover_screenshots"
        os.makedirs("mouseover_screenshots", exist_ok=True)
        
        #set the file name pattern for the screenshots
        timestamp = time.strftime("%y_%m_%d-%H-%M-%S")
        filename = f"mouseover_screenshots/screenshot{timestamp}.png"
        
        image = driver.find_element(By.XPATH, "(//div[@class='container'])[1]")
        image.screenshot(filename)
        
        time.sleep(2)