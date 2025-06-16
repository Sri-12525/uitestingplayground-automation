from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import os

class Alerts:
    def __init__(self, driver):
        self.driver = driver
        
    def check_alerts(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        
        #launching the alerts test url
        alerts_url = wait.until(EC.element_to_be_clickable((By.XPATH, "//div/h3/a[.='Alerts']")))
        alerts_url.click()
        time.sleep(2)
        
        
        alertbttn = wait.until(EC.element_to_be_clickable((By.ID, "alertButton")))
        print("Successfully launched the alerts url ..")
        alertbttn.click()
        time.sleep(2)
        print("Clicked on the alert button..")
        
        alert =  driver.switch_to.alert
        # self.take_screenshots(alert)
        #get the text from the alert box
        alert_text = alert.text
        print(f"The alert says : {alert_text}")
        
        
        #accept the alert
        alert.accept()
        
        time.sleep(4)
        
        #######click on the confirm button
        confirmbttn = wait.until(EC.element_to_be_clickable((By.ID, "confirmButton")))
        confirmbttn.click()
        print("Clicked on the confirm button..")
        confirm_alert = driver.switch_to.alert
        time.sleep(3)
        confirm_alert_text = confirm_alert.text
        print(f"The confirm alert says : {confirm_alert_text}")
        confirm_alert.dismiss()
        time.sleep(4)
        alert2 = driver.switch_to.alert
        print(f"The next alert says {alert2.text}")
        alert2.accept()
        time.sleep(3)
        
        #######click on the prompt button
        promptbttn = wait.until(EC.element_to_be_clickable((By.ID, "promptButton")))
        promptbttn.click()
        print("Clicked on the prompt button..")
        promptbttn_alert = driver.switch_to.alert
        # wait.until(EC.alert_is_present())
        promptbttn_alert.send_keys("Hello!")
        promptbttn_alert.accept()
        time.sleep(2)
        
        try:
            prompt_reply_alert = driver.switch_to.alert
            time.sleep(1)
            print(f"The reply of the prompt alert is : {prompt_reply_alert.text}")
            prompt_reply_alert.accept()
        except:
            print("✅ No follow-up alert appeared.")
        